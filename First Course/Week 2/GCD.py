import sys

def gcd(a,b):
  
    if a == b or b == a:
        return a 
    elif a == 1 :
        return 1
    elif   b ==1:
        return 1
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
    for i in range(2 , max(a,b)):
        c = arr[i - 2] % arr[i - 1]
        arr.append(c)
        if c == 0 :
            break
    return arr[i-1]
             
if __name__ == "__main__":
    input = sys.stdin.read()
    # a , b = 18,35
    a, b = map(int, input.split())
    print(gcd(a, b))



# def gcd(a, b): 

  

#     # Everything divides 0 

#     if (a == 0): 

#         return b 

#     if (b == 0): 

#         return a 

  

#     # base case 

#     if (a == b): 

#         return a 

  

#     # a is greater 

#     if (a > b): 

#         return gcd(a-b, b) 

#     return gcd(a, b-a) 

  
# # Driver program to test above function 

# a = int(input())

# b = int(input())

# print(gcd(a,b)) 