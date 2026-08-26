"""[LEARNING LOGS] A-E-I-O-U"""
def main():
    """[LEARNING LOGS] A-E-I-O-U"""
    text = input().lower()
    dataList = []
    for i in text:
        if i in ("a","e","i","o","u"):
            dataList.append(i)
    for j in ("a","e","i","o","u"):
        count = dataList.count(j)
        if count > 0:
            print(f"{j} : {count}")
main()
