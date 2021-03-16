def main():
    inp = input()
    conts = {
        'A' : 'A',
        'E' : '3',
        'H' : 'H',
        'I' : 'I',
        'M' : 'M',
        'O' : 'O',
        'S' : '2',
        'T' : 'T',
        'U' : 'U',
        'V' : 'V',
        'W' : 'W',
        'X' : 'X',
        'Y' : 'Y',
        'Z' : '5',
        
        'b' : 'd',
        'd' : 'b',
        'i' : 'i',
        'l' : 'l',
        'm' : 'm',
        'n' : 'n',
        'o' : 'o',
        'p' : 'q',
        'q' : 'p',
        'r' : '7',
        'u' : 'u',
        'v' : 'v',
        'w' : 'w',
        'x' : 'x',
        
        '0' : '0',
        '1' : '1',
        '2' : 'S',
        '3' : 'E',
        '5' : 'Z',
        '7' : 'r',
        '8' : '8',
        }

    size = len(inp)
    sel = [0, 0, 0, False]
    for i in range(size):
        count = 0
        second = 0
        if inp[i] in conts and conts[inp[i]] == inp[i]:
            second = i
            for j in range(size//2+1):
                if (i-j) >= 0 and (i+j) < size:
                    a, b = inp[i-j].lower(), inp[i+j].lower()
                    A, B = inp[i-j].upper(), inp[i+j].upper()
                    if a in conts:
                        if conts[a] == b:
                        elif conts[a] == B:
                        else:
                            break
                    elif b in conts:
                        if conts[a] == b:
                        elif conts[a] == B:
                        else:
                            break

                        
                        conts[b] == b:
                        count += 1
                    else:
                        break
                else:
                    break
                    
        elif (i+1) < size and inp[i] in conts and conts[inp[i]] == inp[i+1]:
            second = i+1
            for j in range(size//2+1):
                if (i-j) >= 0 and (i+1+j) < size:
                    if inp[i+1+j] in conts and conts[inp[i+1+j]] == inp[i-j]:
                        count += 1
                    else:
                        break
                else:
                    break

        if sel[2] < count:
            if (i+count) == size:
                sel = [i, second, count, False]
            elif i-count == 0:
                sel = [i, second, count, True]
                

            

    if sel[3]:   
        for i in range(count, size):
            if inp[sel[1] + i] in conts:
    else:   
        for i in range(count, size):
            if inp[sel[0] - i] in conts:
                
        
        

    
    print(sel)

if __name__ == "__main__":
    main()

