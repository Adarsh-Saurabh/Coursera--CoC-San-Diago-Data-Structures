def max_pairwise_product(numbers):
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
    
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
