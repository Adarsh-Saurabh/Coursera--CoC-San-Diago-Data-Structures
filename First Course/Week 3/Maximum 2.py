
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
                # print(1 , " " , value , " " , weights , " " , capacity , " " , ratio)
                if len(weights) == 1:
                    return value
            elif  capacity == weights[i]:
                capacity = capacity - weights[i]
                value += weights[i] * ratio[i]
                # print(weights[i])
                if capacity == 0 :
                    # print(2)
                    return value
                elif weights[i] == [0]:
                    # print(3)
                    return value
            elif capacity < weights[i]:
                # print(weights[i] , " " , capacity)
                y = capacity / weights[i]
                capacity = (capacity) - (y * weights[i])
                value += weights[i] * ratio[i] * y
                # print(4)
                return value                   
            ratio.remove(ratio[i])
            weights.remove(weights[i])
            values.remove(values[i])

def get(capacity , weights , values):
    
    
    

    









if __name__ == "__main__":
    # # weights = [20,50,30]
    # # values = [60,100,120]
    # # weights = [20,50,30,10,50,40]
    # # values = [60,100,120,110,160,50]
    # weights = [20]
    # values = [100]
    # capacity = 5
    # print(get_optimal_value(capacity, weights, values))
    
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
