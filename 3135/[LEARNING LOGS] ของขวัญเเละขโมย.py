"""[LEARNING LOGS] ของขวัญเเละขโมย"""
def main():
    """[LEARNING LOGS] ของขวัญเเละขโมย"""
    n , k , t = map(int,input().split())
    position = 1
    check = 1
    while True:
        position = (position - 1 + k) % n + 1
        if position == 1 or t == 1:
            break
        check += 1
        if position == t:
            break
    print(check)
main()
