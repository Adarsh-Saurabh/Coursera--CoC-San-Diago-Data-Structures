# python3
import sys


# def compute_min_refills(distance, tank, stops):
#     num_refills = 0
#     current_refills = 0
#     while current_refills<= len(stops):
#         last_refill = current_refills
#         while (current_refills <= len(stops) and stops[current_refills + 1] - stops[last_refill] <= tank):
#             current_refills += 1
#         if current_refills == last_refill:
#             return -1
#         elif current_refills <= len(stops):
#             num_refills += 1
#     return num_refills



# def compute_min_refills(distance , tank , stops):
#     trav_dist = 0
#     num_refills = 0
#     for i in range(len(stops)+1):
#         if stops[i+1] - stops[i] > tank:
#             # print('s)')
#             return -1
#         else:
#             random =[]
#             for j in range(len(stops)+1):
#                 while ( trav_dist + tank >= stops[j]):
#                     random.append(trav_dist + tank - stops[j])
#                 trav_dist += tank - min(random)
#                 num_refills += 1
#                 if trav_dist == distance:
#                     return num_refills
#             return num_refills

def compute_min_refills(distance , tank , stops):
    length , refill = 0,0
    stops.append(distance)
    z = 0
    stops.insert(0,z)
    stops.sort()

    # print(stops)
    for i in range(len(stops) - 1):
        if stops[i+1] - stops[i] > tank:
            # print(23)
            return -1
    if tank >= distance:
        return 0
    i = 0
    # for i in range(len(stops)):
    while length < stops[-1]:
        # print(stops)
        random = []
        refill += 1
        # print(len(stops))
        # print(i)
        # for j in range(len(stops)):
        #     if distance <= stops[j]:
        #         refill = refill -1
        #         break
        while length + tank >= stops[i]:
            random.append(stops[i])
            # print(i)
            i += 1
            if i == len(stops) :
                break
        # print(i)
        length += tank
        x = max(random)
        # print(length)
        if distance <= stops[i-1]:
            refill -= 1
        if x == stops[-2]:
            return refill
    return refill     
                




if __name__ == '__main__':
    distance, tank, _, *stops = map(int, sys.stdin.read().split())
    # print(compute_min_refills(d, m, stops))

    # distance = 240
    # tank = 50
    # stops = [50,100 , 190]
    print(compute_min_refills(distance, tank, stops))