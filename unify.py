from add import add
from sub import sub

def main():
    """Uses addition and subtraction for demonstration."""
    a = 1
    b = 2
    print('%d plus %d is %d' % (a, b, add(a, b)))
    print('%d minus %d is %d' % (a, b, sub(a, b)))


if __name__ == '__main__':
    main()
