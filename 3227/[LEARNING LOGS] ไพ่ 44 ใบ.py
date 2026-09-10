"""[LEARNING LOGS] ไพ่ 44 ใบ"""
def main():
    """[LEARNING LOGS] ไพ่ 44 ใบ"""
    text = input().upper()
    point = text[:-1]
    group = text[-1]

    pointDict = {
        "A" : "ace",
        "J" : "jack",
        "Q" : "queen",
        "K" : "king"
    }

    groupDict = {
        "D" : "diamonds",
        "H" : "hearts",
        "S" : "spades",
        "C" : "clubs"
    }

    front = pointDict.get(point,point)
    back = groupDict.get(group)

    print(f"{front} of {back}")
main()
