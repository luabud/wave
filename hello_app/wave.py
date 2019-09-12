from math import cos, radians

def make_dot_string(x):
    rad = radians(x) 
    c = abs(round(cos(rad),2))
    numspaces = int((9 *1/c  - 9)) 
    return numspaces

def print_wave(y=1800):
    for i in range(0, y, 3):
        numspaces= make_dot_string(i)
        print(' ' * numspaces + 'o')

if __name__ == '__main__':
    import sys
    num=int(sys.argv[1])

    print_wave(num)