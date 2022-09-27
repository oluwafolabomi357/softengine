def main():
    get_input = input("Input:").strip()
    print(shorten(get_input))


def shorten(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    short = ''
    for i in word:
        if i.lower() in vowels:
            continue
        short += i
    return short

def looping(score):
    rows = int(input("Type number of rows:"))
    for i in range(0, rows):
        for j in range(0, rows-i):
            print(" ", end='')
        for k in range(0, i + 1):
            print("#", end="")

def name():
    full_name = input("Input your fullname:")
    return f"Your name is {fullname}"
if __name__ == '__main__':
    main()
