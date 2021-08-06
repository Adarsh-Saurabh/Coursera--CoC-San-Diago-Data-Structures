
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

def get(capacity , weights , values):  
    opt_value = 0
    items = list(zip(values, weights))
    print(items)
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    for value, weight in zip(values, weights):
        if capacity == 0:
            return round(opt_value, 4)
        min_weight = min(weight, capacity)
        opt_value += min_weight * (value / weight)
        weight -= min_weight
        capacity -= min_weight

    return round(opt_value, 4)


if __name__ == "__main__":
    # # weights = [20,50,30]
    # # values = [60,100,120]
    # # weights = [20,50,30,10,50,40]
    # # values = [60,100,120,110,160,50]
    # weights = [20]
    # values = [100]
    # capacity = 5
    # print(get_optimal_value(capacity, weights, values))
    
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # opt_value = get_optimal_value(capacity, weights, values)
    # print("{:.10f}".format(opt_value))
    import random
    while True:
        n = random.randint(1,10)
        wei = []
        val = []
        for i in range(n):
            wei.append(random.randint(1,100000))
            val.append(random.randint(1,100000))
        weights = wei
        values = val
        capacity = random.randint(10 , 1000)
        if get(capacity , weights , values) != get_optimal_value(capacity, weights, values) :
            print( get(capacity, weights, values) ,  get_optimal_value(capacity, weights, values)  )
            print(weights )
            print(values)
            print(capacity)
            break
