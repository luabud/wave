from math import cos, radians

def make_dot_string(x,div=1800):
    rad = radians(x)  
    c = abs(round(cos(rad),2))
    if c == 0:
        return 0
    numspaces = int((10 *1/c - 10)) 
    return numspaces

def print_wave(y=1800):
    div = y
    for i in range(0, y, 10):
        numspaces= make_dot_string(i,div)
        print(' ' * numspaces + 'o')

if __name__ == '__main__':
    import sys
    if(len(sys.argv) > 1):
        num=int(sys.argv[1])
    else:
        num=1800
    print_wave(num)