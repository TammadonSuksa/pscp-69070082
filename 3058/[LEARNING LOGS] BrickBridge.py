"""[LEARNING LOGS] BrickBridge"""
def main():
    """[LEARNING LOGS] BrickBridge"""
    BrickA = int(input())
    BrickB = int(input())
    goal = int(input())
    MaxB = goal // 5
    if BrickB >= MaxB:
        MaxB *= 5
    elif BrickB < MaxB:
        MaxB = BrickB * 5

    Remain = goal - MaxB
    if BrickA < Remain:
        print(-1)
    else:
        print(Remain)
main()
