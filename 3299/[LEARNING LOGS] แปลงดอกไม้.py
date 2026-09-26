"""[LEARNING LOGS] แปลงดอกไม้"""
def main():
    """[LEARNING LOGS] แปลงดอกไม้"""
    L , N = map(int,input().split())
    plook = 0
    Line = 1

    while True:
        plook += Line
        if plook >= N:
            break

        Line += 1

    band = (Line + L - 1) // L
    print(band)
main()
