

def max_pairwise_product(input_numbers):

    n = len(input_numbers)
    input_numbers = input_numbers.sort()

    

    return input_numbers[n-1]*input_numbers[n-2]








if __name__ == '__main__':
    input_n = int(input())
    input_numbers = input().split()
    print(max_pairwise_product(input_numbers))
