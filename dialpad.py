def print_number(number):
    digit_to_alpha = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    idxs = [0]*(len(number))
    while True:
        for i in range(len(idxs)):
            idxs[i] += 1
            maxAIndx = len(digit_to_alpha[ord(number[i]) - ord("1") + 1])
            if idxs[i] == maxAIndx:
                if i == len(number) - 1:
                    return
                idxs[i] = 0
            else:
                print repr(idxs)
                break

print_number("234")
