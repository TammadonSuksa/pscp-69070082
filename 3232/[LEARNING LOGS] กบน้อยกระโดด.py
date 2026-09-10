"""[LEARNING LOGS] กบน้อยกระโดด"""
def main():
    """[LEARNING LOGS] กบน้อยกระโดด"""
    x , y = map(int,input().split())
    count = 0
    step = 0
    while x >= 1:
        count += x
        x -= 2
        step += 1
        if count >= y:
            break
    if count < y:
        print(-1)
    else:
        print(step)
main()
