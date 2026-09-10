"""[LEARNING LOGS] สลากกินแบ่ง"""
def main():
    """[LEARNING LOGS] สลากกินแบ่ง"""
    a = input().split()
    b = input().split()
    reward = 0
    if a == b:
        reward = 1000000
    elif a[1] == b[1]:
        reward = 100000
    elif a[1][2:5] == b[1][2:5] and a[0] == b[0]:
        reward = 2000
    elif a[1][3:5] == b[1][3:5] and a[0] == b[0]:
        reward = 1000
    elif a[1][2:5] == b[1][2:5] and a[0] != b[0]:
        reward = 200
    elif a[1][3:5] == b[1][3:5] and a[0] != b[0]:
        reward = 100
    elif a[0] == b[0]:
        reward = 20
    print(reward)
main()
