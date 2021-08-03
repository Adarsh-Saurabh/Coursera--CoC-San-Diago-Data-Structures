# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    ratio = []
    # weights.sort()
    # values.sort()
    for i in range(len(weights)):
        i = values[i] / weights[i]
        ratio.append(i)
    
    return ratio
     

if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # opt_value = get_optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))

    weights = [20,50,30]
    values = [60,100,120]
    capacity = 50
    print(get_optimal_value(capacity, weights, values))