def gcd(a,b):
    if a > b:
        arr = [a,b]
    elif a == 0:
        return b
    elif b == 0:
        return a
    else :
        arr = [b,a]
    for i in range(2 , min(a,b)):
        c = arr[i - 2] % arr[i - 1]
        arr.append(c)
        if c == 0 :
            break
    return arr[i-1]
             
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(gcd(a,b))

