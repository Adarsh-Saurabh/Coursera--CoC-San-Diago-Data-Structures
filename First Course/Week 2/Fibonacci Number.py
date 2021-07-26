def fastfib(n):
    a = [0,1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    return a[n]

if __name__ == '__main__':
    n = int(input())
    print(fastfib(n))