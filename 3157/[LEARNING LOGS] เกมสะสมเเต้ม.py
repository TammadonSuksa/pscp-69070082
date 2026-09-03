"""[LEARNING LOGS] เกมสะสมแต้ม"""
def main():
    """[LEARNING LOGS] เกมสะสมแต้ม"""
    n = int(input())
    point = 0
    for _ in range(n):
        do = input()
        if do == "+":
            point += 10
        else:
            point -= 5
    print(point)
main()
