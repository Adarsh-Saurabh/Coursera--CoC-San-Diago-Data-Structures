import sys

def compute_min_refills(distance , tank , stops):
    length , refill = 0,0
    stops.append(distance)
    z = 0
    stops.insert(0,z)
    stops.sort()
    for i in range(len(stops) - 1):
        if stops[i+1] - stops[i] > tank:
            return -1
    if tank >= distance:
        return 0
    i = 0
    while length < stops[-1]:
        array = []
        refill += 1
        while length + tank >= stops[i]:
            array.append(stops[i])
            i += 1
            if i == len(stops) :
                break
        length += tank
        x = max(array)
        if distance <= stops[i-1]:
            refill -= 1
        if x == stops[-2]:
            return refill
    return refill     
                
                
if __name__ == '__main__':
    # distance, tank, _, *stops = map(int, sys.stdin.read().split())
    # print(compute_min_refills(distance, tank, stops))

    distance = 240
    tank = 50
    stops = [50,100 ,150, 190]
    print(compute_min_refills(distance, tank, stops))