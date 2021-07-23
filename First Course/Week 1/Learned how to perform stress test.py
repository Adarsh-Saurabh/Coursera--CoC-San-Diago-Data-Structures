import random
#this is the first and better algorithm which we were going to debug

def max_pairwise_product_fast(numbers):
    first = 0
    second = 0
    first = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] == first:
            continue
        else:
            second = max(second,numbers[i])
    place = numbers.count(first)
    if place ==1:
        return first*second
    else:
        return first*first
    
# This is the 2nd algorithm for testing the first one

def max_pairwise_product(numbers):
    n = len(numbers)
    product = 0
    for first in range(n):
        for second in range(first + 1, n):
            product = max(product,numbers[first] * numbers[second])                
    return product
# Main function
if __name__ == '__main__':

# Making a infinite loop 
# Making a random input genertor


    while True:
        n = random.randint(2,100)
        print(n)
        a = []
        for z in range(n+1):
            a.append(random.randint(0,10))
        print(a)
        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_fast(a)
        if res1 == res2:
            print("OK")
        else:
            print(res1,"",res2)
            break
        
# Traditional input 


    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

# Our final code will be something like this

# def max_pairwise_product_fast(numbers):
#     first = 0
#     second = 0
#     first = max(numbers)
#     for i in range(len(numbers)):
#         if numbers[i] == first:
#             continue
#         else:
#             second = max(second,numbers[i])
#     place = numbers.count(first)
#     if place ==1:
#         return first*second
#     else:
#         return first*first
    



# if __name__ = '__main__':
#     input_n = int(input())
#     input_numbers = [int(x) for x in input().split()]
#     print(max_pairwise_product(input_numbers))


