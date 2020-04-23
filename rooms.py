import csv
import itertools

input = "5,8,10:30,11:30"
a = input.split(",")
mem = a[0]
floor = a[1]
timings_from = a[2]
timings_till = a[3]

def meeting_room(mem,floor,timings_from, timings_till):
    print(timings_from + timings_till)
    members = []
    floors = []
    rooms = []
    length = []
    count=0
    time = []
    allocate=False
    diff = 0
    last_diff = 1
    fl=0
    rm=0
    with open('rooms.txt', newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        for i in your_list:
            timings = []
            length.append(len(i))
            x=i[0].split(".")
            floors.append(x[0])
            rooms.append(x[1])
            members.append(i[1])
            for j in range(2,len(i)):
                timings.insert(count,i[j])
                count = count+1
            time.append(timings)
    count=0
    for i in members:
        if mem > i:
            print("Room "+rooms[count]+" with floor "+floors[count]+" not available for "+members[count])
        else:
            allocate=True
        count=count+1
    count=0
    for (i,j,k,l) in itertools.zip_longest(floors,rooms,members,time):
        if timings_from in l and timings_till in l:
            if mem <= k:
                if floor == i:
                    print("Hello, "+i + j + timings_from + timings_till)
                    fl=i
                    rm=j
                else:
                    diff = abs(int(int(floor) - int(i)))
                    if diff <= last_diff:
                        last_diff = diff
                        fl=i
                        rm=j    
        count=count+1
    print(str(fl)+"."+str(rm))
meeting_room(mem, floor, timings_from,timings_till)

