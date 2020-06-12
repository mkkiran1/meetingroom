"""
This program needs to be run where we have rooms.txt is accessible.
rooms.txt has the meeting rooms data with the rooms availability
The input is given in this program itself for which the meeting room availability need to be checked.
Input : For 5 team members, search for the room located on the 8th floor, with the meeting start time 10:30 and end time 11:30
NOTE: code written with python 3.8.2 
"""

from datetime import datetime

def timediff(time1, time2):
    timea = datetime.strptime(time1, "%H:%M")
    timeb = datetime.strptime(time2, "%H:%M")
    if timea >= timeb:
        newtime = timea - timeb
        return int(newtime.seconds / 60)
    else:
        newtime = timea - timeb
        return int(-newtime.seconds / 60)


def getclosest(lst, K):
    num = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
    return num

input1 = "7,7,11:00,11:30"
ipcapacity, ipfloor, ipstart, ipend = input1.split(",")
#print("ipcapacity:" + ipcapacity + "\nipfloor:" + ipfloor + "\nipstart:" + ipstart + "\nipend:" + ipend)
availablerooms = []

roomsfile = open('C:\\workspace\\ConferenceRoom\\rooms.txt', 'r')
while True:
    # Reading next line from file
    line = roomsfile.readline()

    # if line is empty
    # End of file is reached
    if not line:
        break
    #To strip the line for all white spaces and split it with comma
    x = line.strip().split(",")
    #For further the first string from above split to get floor and room details
    floor = x[0].split('.')[0]
    room = x[0].split('.')[1]
    capacity = x[1]
    #To check the capacity of meeting room
    if capacity >= ipcapacity:
        for i in range(2, len(x), 2):
            #check the starting time and its availability 
            checkStarttime = timediff(ipstart, x[i])
            if checkStarttime >= 0:
                checkEndtime = timediff(x[i + 1], ipend)
                # check meeting end time availability if starting time available as per the duration of meeting
                if checkEndtime >= 0:
                    #collect info for all available meeting room 
                    availablerooms.append(x[0])


roomsfile.close()
if not availablerooms:
    #if no room is available as per the requirement 
    print("Sorry, no meeting available to meet your requirement")
else:
#   converting list of available meeting rooms into dict
    floorrooms = {int(fr.split('.')[0]): int(fr.split('.')[1]) for fr in availablerooms}
#   sorting the dict on floor and picking the closest floor
#   same logic could be use to get the nearest meeting room in case needed
    closestfloor = getclosest(sorted(floorrooms), int(ipfloor))
    print("{0}.{1}".format(closestfloor, floorrooms[closestfloor]))