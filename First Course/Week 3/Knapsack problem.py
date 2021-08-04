import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    ratio = []
    for i in range(len(weights)):
        ratio.append(values[i] / weights[i])
    for l in range(len(ratio)):
        if len(ratio) > 0:
            i = ratio.index(max(ratio))
            if capacity > weights[i] :
                capacity = capacity - weights[i]
                value += weights[i] * ratio[i]
                if len(weights) == 1:
                    return round(value , 4)                   
            elif  capacity == weights[i]:
                capacity = capacity - weights[i]
                value += weights[i] * ratio[i]
                if capacity == 0 :
                    return round(value , 4)                   
                elif weights[i] == [0]:
                    return round(value , 4)                   
            elif capacity < weights[i]:
                y = capacity / weights[i]
                capacity = (capacity) - (y * weights[i])
                value += weights[i] * ratio[i] * y
                return round(value , 4)                   
            ratio.remove(ratio[i])
            weights.remove(weights[i])
            values.remove(values[i])
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

