

def to_signed16(x):
    if x >= 1<<15:
        x -= 1<<16

    return x

def check_data(din, dout, configure):
    shift = configure.get('shift', 0)
    width = configure.get('width', 24)
    pos_limit = 0x7fff
    neg_limit = to_signed16(0x8000)
    if din >= 1<<(width-1):
        din -= 1<<width
    
    x = din >> shift
    
    if x > pos_limit:
        x = pos_limit
        
    if x < neg_limit:
        x = neg_limit


    x = x & 0xffff

    if x != dout:
        print('check failed', hex(x), hex(dout))


def check_file(fdata, configure):
    for line in fdata:
        before,after = line.split()
        check_data(int(before, 16), int(after, 16), configure)

def main():
    fdata_name_list = ["fin.data"]
    configure = {'shift': 0}
    for fdata_name in fdata_name_list:
        check_file(open(fdata_name), configure)

if __name__ == '__main__':
    main()
