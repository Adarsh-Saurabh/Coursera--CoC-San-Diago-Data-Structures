import sys
def fastfib(n,m):  

    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        a = [0,1]
        for i in range(2, n+1):
            a.append(a[-1] + a[-2])
        c = a[n]
        return c % m




if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # n , m  = 1000 , 100
    print(fastfib(n, m))