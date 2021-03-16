def solution():
    S1, S2 = map(int, input().split())

    for i in range(S1):
        a, b = map(int, input().split())
        if a != b:
            print("Wrong Answer")
            return

    for i in range(S2):
        a, b = map(int, input().split())
        if a != b:
            print("Why Wrong!!!")
            return
    print("Accepted")

def main():
    solution()

if __name__ == "__main__":
    main()
