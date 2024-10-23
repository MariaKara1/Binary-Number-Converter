def binaryToDecimal(num):
    starter = [0,0,0,0]
    if num >= 8:
        starter[0] = 1
        num = num - 8
    if num >= 4:
        starter[1] = 1
        num = num - 4
    if num >= 2:
        starter[2] = 1
        num = num-2
    if num >= 1:
        starter[3] = 1
    print(starter)

binaryToDecimal(15)

def decimalToBinary(bin):
    sum = 0
    for n in bin:
        sum = sum + n*(2^(bin.index(n)))*2
        print(sum)

decimalToBinary([1,0,0,1])