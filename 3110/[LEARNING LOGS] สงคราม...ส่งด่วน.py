"""[LEARNING LOGS] สงคราม...ส่งด่วน"""
def main():
    """[LEARNING LOGS] สงคราม...ส่งด่วน"""
    start , destination = map(str ,input().split())
    weight = float(input())
    result = 0
    if start == "BKK" and destination == "CNX":
        result = 10 + (weight*30)
    elif start == "CNX" and destination == "UBP":
        result = 15 + (weight*40)
    elif start == "UBP" and destination == "BKK":
        result = 20 + (weight*40)
    elif start == "BKK" and destination == "PKT":
        result = 25 + (weight*50)
    elif start == "PKT" and destination == "CNX":
        result = 30 + (weight*60)
    elif start == "UBP" and destination == "PKT":
        result = 40 + (weight*70)
    else:
        print("Error")
        return
    print(f"{result:.2f}")
main()
