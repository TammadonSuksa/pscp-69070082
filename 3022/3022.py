"""Temperature"""
def main():
    """Temperature"""
    temp = float(input())
    unit = input()
    transferUnit = input()
    c = 0
    result = 0

    if unit == "C":
        c = temp
    elif unit == "F":
        c = (temp - 32) * 5 / 9
    elif unit == "K":
        c = temp - 273.15
    elif unit == "R":
        c = temp * 5 / 9 - 273.15

    if transferUnit == "C":
        result = c
    elif transferUnit == "F":
        result = c * 9 / 5 + 32
    elif transferUnit == "K":
        result = c + 273.15
    elif transferUnit == "R":
        result = (c + 273.15) * 9 / 5

    print(f"{result:.2f}")

main()
