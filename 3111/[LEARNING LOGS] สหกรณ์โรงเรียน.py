"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
import decimal
def main():
    """[LEARNING LOGS] สหกรณ์โรงเรียน"""
    isMember = input()
    items = int(input())
    sumPrice = decimal.Decimal("0")
    for _ in range(items):
        sumPrice += decimal.Decimal(input())
    if isMember == "Y":
        sumPrice = sumPrice - sumPrice * decimal.Decimal("0.05")
    elif isMember == "N" and sumPrice >= 500:
        sumPrice = sumPrice - sumPrice * decimal.Decimal("0.03")
    result = sumPrice.quantize(decimal.Decimal("0.01") , rounding=decimal.ROUND_HALF_UP)
    print(result)
main()
