n = int(input(""))
seats = []
for i in range(n):
    seats.append(int(input()))
num = 0

seats_1 = []
seats_2 = []
count = 0
for j in range(int(len(seats)/2)):
    seats_1.append(seats[j])
    count += 1

for k in range(int(len(seats)/2)):
    seats_2.append(seats[count])
    count += 1

for l in range(len(seats_1)):
    if seats_1[l] == seats_2[l]:
        num += 2

print(num)

