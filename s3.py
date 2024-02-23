n = int(input())
arrays = []
for a in range(2):
    arrays.append(list(map(int, input().split())))
possible = False
search = False
output = []


def find_action(array_a, array_b):
    new_array = array_b
    can_solve = False
    action = []
    target_value = -1
    left_bound = -1
    right_bound = -1
    left_swipe = False
    right_swipe = False

    for i in range(len(array_a)):
        if array_a[i] == array_b[i]:
            continue
        else:
            if array_a[i] > array_b[i]:
                target_value = array_b[i]
                right_swipe = True
                left_bound = i-1
            else:
                target_value = array_b[i]
                left_swipe = True
                left_bound = i
            break
    
    if left_swipe:
        for j in range(len(array_a)):
            if array_a[j] == target_value:
                right_bound = j
                break

    elif right_swipe:
        start_check = False
        for j in range(len(array_b)):
            if array_b[j] == target_value:
                start_check = True
            if start_check == True:
                if array_b[j] != target_value:
                    right_bound = j
                    break
        if right_bound == -1:
            right_bound = len(array_b)-1

    one_swipe_check = False

    for k in range(left_bound, right_bound):
        if array_b[k] == target_value:
            one_swipe_check = True
            continue
        else:
            one_swipe_check = False

    if one_swipe_check:
        can_solve = True
    
    if can_solve:
        if right_swipe:
            action.append("R")
        elif left_swipe:
            action.append("L")
        action.append(left_bound)
        action.append(right_bound)
        output.append(action)
        
        if right_swipe:
            for b in range(left_bound+1, right_bound+1):
                new_array[b] = array_a[b]
        elif left_swipe:
            for b in range(left_bound, right_bound):
                new_array[b] = array_a[b]

    return new_array, can_solve


if arrays[0] == arrays[1]:
    possible = True
    search = False

if possible == False:
    for x in range(len(arrays[0])):
        if (arrays[0][x] in arrays[1]) == False:
            search = True

if search == True:
    new, can_solve = find_action(arrays[0], arrays[1])
    while can_solve != False and new != arrays[0]:
        new, can_solve = find_action(arrays[0], new)
    if can_solve == False:
        possible = False
    else:
        possible = True

if possible:
    print("YES")
    print(len(output))
    for o in output:
        for a in o:
            print(a, end=" ")
        print("")
else:
    print("NO")
            








