"""หาร 10"""
def main():
    """หาร 10"""
    number = int(input())
    n = number // 10
    for i in range(n,-1,-1):
        if not i:
            print(i * 10 , end="")
        else:
            print(i * 10 , end=" ")
main()
