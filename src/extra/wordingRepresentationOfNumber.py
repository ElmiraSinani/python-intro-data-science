numListDict = {
    'numbers': ["zero","one","two","three","four","five","six","seven","eight","nine",
                "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"],
    'decades': ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
}

def getNumber(n):
    return numListDict['numbers'][n]

def getDecades(n):
    firstN = n//10
    secondN = n%10
    result = ""
    if firstN>1:  #20-99
        if secondN==0:
            result = numListDict['decades'][firstN]
        else:
            result = numListDict['decades'][firstN] + "-" + numListDict['numbers'][secondN]
    return result

def getHundred(n):
    firstN = n // 100
    secondN = n % 100
    if firstN>0:
        result = numListDict['numbers'][firstN] + " hundred "
    result += getDecades(secondN)
    return result

def getThousand(n):
    firstN = n // 1000
    secondN = n % 1000
    result = ""
    if firstN > 0:
        if len(str(firstN))<=2:
            if firstN<20:
                result = getNumber(firstN) + " thousand "
            else:
                result = getDecades(firstN) + " thousand "
        elif len(str(firstN))==3:
            result = getHundred(firstN)
            if firstN%100>0 and firstN%100<20:
                result += getNumber(firstN%100)+" "
            else:
                result += " "
            result += "thousand "
    if secondN>0:
        result += getHundred(secondN)

    return result

def getNumWordingRepresentation(num):
    num_len = len(str(num))
    if num_len<=2: #0-99
        if num < 20:
            return getNumber(num)
        else:
            return getDecades(num)
    if num_len==3: #100-999
        return getHundred(num)
    if num_len>=4 and num_len<=6: #1.000-999.999
        return getThousand(num)
    return "Sorry, max supported number is 999.999"

print(getNumWordingRepresentation(5)) #five
print(getNumWordingRepresentation(67)) #sixty-seven
print(getNumWordingRepresentation(100)) #one hundred
print(getNumWordingRepresentation(150)) #one hundred fifty
print(getNumWordingRepresentation(101789)) #one hundred one thousand seven hundred eighty-nine
print(getNumWordingRepresentation(100000)) #one hundred thousand
print(getNumWordingRepresentation(154789)) #one hundred fifty-four thousand seven hundred eighty-nine
print(getNumWordingRepresentation(1547890)) #Sorry, max supported number is 999.999
