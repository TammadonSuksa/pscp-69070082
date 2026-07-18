"""ปราสาท"""
def main():
    """ปราสาท"""
    startPosition = int(input())
    FloorAt = 1
    countNumberToPosition = 1
    countPlusTwo = 1
    PositionInRow = 0 #ขึ้นเเถวใหม่ เริ่ม 0 ใหม่
    # Floor เปลี่ยน PositionInRow เริ่ม 0

    if startPosition == 1:
        print(0)
        return

    # หาชั้น หาตำเเหน่งของในชั้นนั้น ค่อยๆไล่เลขไปเรื่อยๆ
    while countNumberToPosition < startPosition:
        FloorAt += 1
        countPlusTwo += 2
        PositionInRow = 0

        for _ in range(countPlusTwo):
            countNumberToPosition += 1
            PositionInRow += 1
            if countNumberToPosition == startPosition:
                break

    if not PositionInRow % 2:
        wallToBreak = countPlusTwo - 2
    else:
        wallToBreak = countPlusTwo - 1

    print(wallToBreak)
main()
