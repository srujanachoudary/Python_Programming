def numbertoword(n):
    digits=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
    for i in str(n):
        print(digits[int(i)],end=" ")
numbertoword(111)