"""Season"""
def main():
    """Season"""
    month = int(input())
    day = int(input())

    seasonNum = month / 3
    season = ""

    if not month % 3 and day >= 21:
        if seasonNum < 4 :
            seasonNum += 1
        else:
            seasonNum = 1

    if 0 <= seasonNum <= 1:
        season = "winter"
    elif 1 < seasonNum <= 2:
        season = "spring"
    elif 2 < seasonNum <= 3:
        season = "summer"
    elif 3 < seasonNum <= 4:
        season = "fall"

    print(season)
main()
