import sys

def gcd(a,b):
    if a == b or b == a:
        return a 
    elif a > b:
        if b == 0:
            return a
        else:
            arr = [a,b] 
    else :
        if a == 0:
            return b
        else:    
            arr = [b,a]
    for i in range(2 , max(a,b)+1):
        c = arr[i - 2] % arr[i - 1]
        arr.append(c)
        if c == 0 :
            break
    gcd = arr[i-1]
    min_num = min(a,b)
    max_num = max(a,b)
    lcm = max_num * ( min_num / gcd )
    return int(lcm)
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
