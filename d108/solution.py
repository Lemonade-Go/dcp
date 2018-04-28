def is_shifted(a, b):
    if len(a) != len(b):
        return False
    return b in a+a

def extra_credit(a, b):
    if len(a) != len(b): 
        return False
    if a == b:
        return "Match"
    count = 0
    shift_right = a
    shift_left = a
    while(count < len(a)):
        print(len(a)-count)
        print("Solution: "+b)
        if shift_left == b:
            return "Shifted "+str(count)+" times to the right"
        elif shift_right == b:
            return "Shifted "+str(count)+" times to the left"
        else:
            shift_left = rotate_left(shift_left,1)
            shift_right = rotate_right(shift_right,1)
        count+=1
    return False

def rotate_right(a, d):
    lfirst = a[0:d]
    lsecond = a[d:]
    print("right shift: "+lsecond+lfirst)
    return lsecond+lfirst

def rotate_left(a, d):
    rfirst = a[0 : len(a)-d]
    rsecond = a[len(a)-d :]
    print("left shift: "+rfirst+rsecond)
    return rsecond+rfirst

if __name__ == "__main__":
    a = "abcde"
    b = "eabcd"
    print(is_shifted(a,b))
    print(extra_credit(a,b))
