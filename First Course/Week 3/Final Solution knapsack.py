import sys


def get(capacity , weights , values):
    value = 0
    items = list(zip(values, weights))
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    for value, weight in zip(values, weights):
        if capacity == 0:
            return round(value , 4)
        min_weight = min(weight, capacity)
        value += min_weight * (value / weight)
        weight -= min_weight
        capacity -= min_weight
    return round(value , 4)
if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # value = get(capacity, weights, values)
    # print("{:.10f}".format(value))
    weights = [20,50,30]
    values = [60,100,120]    
    capacity = 50
    print(get(capacity, weights, values))