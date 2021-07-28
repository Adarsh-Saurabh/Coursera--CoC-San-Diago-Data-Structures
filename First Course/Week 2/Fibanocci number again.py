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














  
# # Uses python3
# import sys

# def get_fibonacci_huge_naive(n, m):
#     curr, prev = 1,0
#     for i in range(m*m+1):
# #         print(i)
#         prev,curr =  curr, (curr+prev)%m
#         if (prev, curr) == (0,1):
#             time_period = i+1
# #             print('here',time_period)
#             break
        
#     index = n%time_period
# #     print(index)
#     if index<1:
#         return index
#     prev,curr = 0,1
#     for i in range(2, index+1):
#         prev,curr = curr, (curr+prev)%m
#     return curr

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))
