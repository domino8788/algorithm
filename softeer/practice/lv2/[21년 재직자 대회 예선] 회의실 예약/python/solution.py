import sys

meetingRoomCount, reservationCount = map(int, sys.stdin.readline().split())
meetingInfo={}
for i in range(meetingRoomCount):
    meetingRoomName = sys.stdin.readline().strip();
    meetingInfo[meetingRoomName] = [0 for _ in range(9, 18)] #예약 가능한 시간대 9시~17시 (18시는 마감이므로 예약불가)

for i in range(reservationCount):
    meetingRoomName, startHour, endHour = map(lambda arr: arr[1] if arr[0]==0 else int(arr[1]), enumerate(sys.stdin.readline().split()))
    for j in range(startHour, endHour):
        meetingInfo[meetingRoomName][j-9] = 1
        
for (roomIdx, meetingRoomName) in enumerate(sorted(meetingInfo.keys())):
    doesNotReserved = [];
    startHour = None
    endHour = None
    reservationInfo = meetingInfo[meetingRoomName]
    for hour, reserved in enumerate(reservationInfo):
        if reserved == 0: #예약되지 않았다
            if hour+9 == 17: #예약되지 않은 시간이 17시일 경우 18시는 예약이 불가능하므로 별도로 분기처리가 필요하다.
                if startHour is None:
                    startHour = hour+9
                endHour = hour+9+1
                doesNotReserved.append(f"{startHour:0>2}-{endHour:0>2}")
            elif startHour is None: #startHour가 설정되지 않은 상태일 때
                startHour = hour+9
            else: #startHour가 설정된 상태일 때        
                continue
        else: #예약되었다
            if startHour is None: #startHour가 설정되지 않은 상태이면 계속 예약중인 상태
                continue
            else: #예약 되었으면서 startHour가 설정된 상태. 즉 예약 가능한 시간대의 끝
                endHour = hour+9
                doesNotReserved.append(f"{startHour:0>2}-{endHour:0>2}")
                startHour = None
                endHour = None
    print(f"Room {meetingRoomName}:")
    if len(doesNotReserved) ==0:
        print("Not available")
    else:
        print(f"{len(doesNotReserved)} available:")
        for info in doesNotReserved:
            print(info)
    if roomIdx != meetingRoomCount-1:
        print("-----")

        