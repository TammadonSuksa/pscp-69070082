"""[LEARNING LOGS] BigFrame"""
def main():
    """[LEARNING LOGS] BigFrame"""
    word = []
    for _ in range(5):
        word.append(input())

    clean_word = []
    for i in word:
        clean_word.append(i.strip())

    max_len = 0
    for i in clean_word:
        if len(i) > max_len:
            max_len = len(i)

    for i in range(7):
        if not i or i == 6:
            print("*" * (max_len + 4))
        else:
            text = clean_word[i-1]
            space = " " * (max_len - len(text))
            print("* " + text + space + " *")
main()
