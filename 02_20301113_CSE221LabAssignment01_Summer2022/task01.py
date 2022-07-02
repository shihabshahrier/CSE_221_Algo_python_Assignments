def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return "not a palindrome"
    return "palindrome"
    
def parity(n):
    global odd
    global even
    global nopa
    if "." in n:
        nopa += 1
        return "cannot have parity"
    elif int(n) % 2 == 0:
        even += 1
        return "has odd parity"
    else:
        odd += 1
        return "has odd parity"
        
if __name__ == "__main__":
        
    ifile = open("input01.txt", "r")

    data = ifile.read().split("\n")
    x = []

    ispalin = []
    ofile = open("output01.txt", "w")
    ofile2 = open("record.txt", "w")

    odd = 0
    even = 0
    nopa = 0
    npalin = 0

    for i in data:
        x.append(i.split())
    
    for i in range(len(x)):
        word = x[i][1]
        p = palindrome(word)
    
        eo = parity(x[i][0])
        if p == "palindrome":
            txt = f"{x[i][0]} {eo} and {word} is a palindrome\n"
        else:
            npalin += 1
            txt = f"{x[i][0]} {eo} and {word} is not a palindrome\n"
        #print(txt)
        ofile.write(str(txt))
    
    l = len(x)   
    record = f"Percentage of odd parity: {int((odd/l)*100)}% \nPercentage of even parity: {int((even/l)*100)}% \nPercentage of no parity: {int((nopa/l)*100)}% \nPercentage of palindrome: {int(((l - npalin)/l)*100)}% \nPercentage of non-palindrome: {int((npalin/l)*100)}%\n"
    #print(record)
    ofile2.write(record)
    ifile.close()
    ofile.close()
    ofile2.close()
    print("finish")
        




