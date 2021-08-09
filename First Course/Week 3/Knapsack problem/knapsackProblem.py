# Knapsack problem
import sys
import numpy as np

def get_optimal(capacity, weights, values):
    value = 0.0
    ratio = []
    r = np.zeros(len(weights))
    for i in range (len(weights)):
        ratio.append(values[i]/weights[i])
    ratio.sort()
    for i in range(len(weights)):
        if capacity == 0:
            return value
        a = min(capacity , weights[i])
        value += a * ratio[i]
        weights[i] = weights[i] - a
        r[i] += a
        capacity = capacity - a
        print(r)
        return value 

def get_optimal_value(capacity, weights, values):
    value = 0
    ratio = []
    r = list(range(len(weights)))
    for i in range(1,len(weights)):
        ratio.append(values[i] / weights[i])
    for l in range(len(ratio)):
        if len(ratio) >= 0:
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
    # weights = [20,50,30]
    # values = [60,100,120]
    weights = [20,50,30,10,50,40]
    values = [60,100,120,110,160,50]
    # weights = [20]
    # values = [100]
    capacity = 100
    print(get_optimal(capacity, weights, values) , " " , get_optimal_value(capacity, weights, values))