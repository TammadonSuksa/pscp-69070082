"""Bill"""
def main():
    """Bill"""
    price = int(input())
    result = 0

    serviceCharge = price * 0.1
    if serviceCharge < 50:
        serviceCharge = 50
    elif serviceCharge > 1000:
        serviceCharge = 1000

    result = price + serviceCharge
    vat = result * 0.07
    result += vat
    print(f"{result:.2f}")
main()
