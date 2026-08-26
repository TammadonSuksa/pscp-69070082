"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
def main():
    """จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
    Anum = int(input())
    Bnum = int(input())
    Ddivide = int(input())
    Rremain = int(input())

    count = 0
    for i in range(Anum,Bnum+1):
        if i % Ddivide == Rremain:
            count += 1
    print(count)
main()
