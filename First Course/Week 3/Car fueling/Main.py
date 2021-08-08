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



def compute_min_refills(distance , tank , stops):
    trav_dist = 0
    num_refills = 0
    for i in range(len(stops)+1):
        if stops[i+1] - stops[i] > tank:
            print('s)')
            # return -1
        else:
            random =[]
            for j in range(1,len(stops)):
               
                
                random.append(stops[j] - stops[j-1])
            trav_dist += random[random.index(max(random))]
            if trav_dist > distance:
                print('k')
                # return -1
            else:
                num_refills += 1
    return num_refills



if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    # print(compute_min_refills(d, m, stops))

    distance = 975
    tank = 400
    stops = [0, 200, 375, 550, 750, 950]
    print(compute_min_refills(distance, tank, stops))