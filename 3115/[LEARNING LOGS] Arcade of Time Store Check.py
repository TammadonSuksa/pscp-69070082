"""[LEARNING LOGS] Arcade of Time: Store Check"""
def main():
    """[LEARNING LOGS] Arcade of Time: Store Check"""
    StoreCount , CheckCount = map(int, input().split())
    Store = {}
    for i in range(StoreCount):
        Start , Stop = map(int,input().split())
        Store[f"Store{i}"] = {"Start":Start,"Stop":Stop}

    CheckAtTime = list(map(int, input().split()))
    result = []
    for n in range(CheckCount):
        count = 0
        for j in range(len(Store)):
            if Store[f"Store{j}"]["Start"] <= CheckAtTime[n] < Store[f"Store{j}"]["Stop"]:
                count += 1
        result.append(str(count))

    print(" ".join(result))

main()
