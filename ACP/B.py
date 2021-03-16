def main():
    N = int(input())
    grades = [0] + list(map(int, input().split()))
    MVP = input()
    enums = {'B' : 1, 'S' : 2, 'G' : 3, 'P' : 4, 'D' : 4}
    
    pre = 0
    money = 0 
    for i in range(N):
        if MVP[i] == 'D':
            
            pre = grades[4]
            money += grades[4]
            continue
        pre = grades[enums[MVP[i]]] - 1 - pre
        money += pre
        if pre < 0:
            pre = 0

    print(money)

if __name__ == "__main__":
    main()
