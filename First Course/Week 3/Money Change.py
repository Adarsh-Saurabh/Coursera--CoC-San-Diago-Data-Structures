# Uses python3
import sys

def get_change(m):
    x = m//10
    y = m % 10
    z = m % 5
    a = y // 5
    return a + z + x
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    # m = 10089
    print(get_change(m))
