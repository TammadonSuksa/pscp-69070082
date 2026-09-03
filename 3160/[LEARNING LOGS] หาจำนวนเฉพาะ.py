"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
def main():
    """[LEARNING LOGS] หาจำนวนเฉพาะ"""
    start , end = map(int,input().split())
    isPrimeList = []
    status = False
    for i in range(start,end+1):
        for j in range(2,i):
            if not i % j:
                status = False
                break
            status = True

        if status is True or i == 2:
            isPrimeList.append(i)

    if len(isPrimeList) > 0:
        print(" ".join(str(i) for i in isPrimeList))
    print(f"Total primes: {len(isPrimeList)}")
main()
