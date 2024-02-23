values = list(map(int, input().split()))
letters = []
output = []

for i in range(values[0]):
    letters.append(list(input()))

for x in letters:
    last = ""
    previous = ""
    current = ""
    alternating = True
    duplicates = False
    num = -1

    for y in range(len(x)):
        last = previous
        previous = current
        current = x[y]
        if (current == last):
            num = (y % 2)
            break
    
    if num == -1:
        output.append("F")
        continue 

    temp_heavy = []
    for w in range(len(x)):
        if (w % 2 == num) and ((x[w] in temp_heavy) == False):
            temp_heavy.append(x[w])

    temp_light = []
    for g in range(len(x)):
        if (g % 2 != num):
            if (x[g] in temp_heavy) or (x[g] in temp_light):
                duplicates = True
                break
            temp_light.append(x[g])

    heavy = temp_heavy
    print(heavy)
    print(temp_light)
    
    if duplicates == True:
        output.append("F")
        continue
    
    first_run = True

    for z in range(len(x)):
        if first_run == True:
            if x[z] in heavy:
                num = z
                first_run = False
                if num % 2 == 0:
                    num = 0
                elif num % 2 == 1:
                    num = 1
            else:
                continue

        if z % 2 == num:
            if x[z] in heavy:
                continue
            else:
                alternating = False
                break
        else:
            if x[z] in heavy:
                alternating = False
                break
            else:
                continue

    if alternating == True:
        output.append("T")
    else:
        output.append("F")

for a in output:
    print(a)
