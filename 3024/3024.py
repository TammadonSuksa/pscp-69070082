"""Surprising Vote"""
def main():
    """Surprising Vote"""
    sumOfThree = float(input())
    highest = float(input())

    if sumOfThree > 30:
        print("Error")
        return

    if highest > 10 or highest < 0:
        print("Error")
        return

    if highest > sumOfThree:
        print("Error")
        return

    lowest = sumOfThree - (highest * 2)
    if lowest < 0:
        lowest = 0

    differenceBetween = highest - lowest

    if differenceBetween > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
