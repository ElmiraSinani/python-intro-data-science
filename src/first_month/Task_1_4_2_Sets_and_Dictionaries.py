#1. Գրել ծրագիր, որը տրված բառարանում կավելացնի նոր արժեք տրված բանալիով
def addDictValByGivenKey(dict1, key, val):
    dict1[key] = val
    return dict1

dict1 = { "brand": "Ford",  "model": "Mustang",  "year": 1964}
print('#1 ', addDictValByGivenKey(dict1, 'color', 'red'))

#2. Գրել ծրագիր, որը կմիավորի տրված 2 բառարանները
def concatDicts(d1, d2):
    d1.update(d2)
    return d1

d1 = {1:'a', 2: 'b'}
d2 = {3: 'c', 4: 'd', 5: 'e'}
print('#2 ', concatDicts(d1, d2))

#3. Գրել ծրագիր, որը տրված n թվի համար կկառուցի բառարան,  որի բանալիները կլինեն 1֊ից n թվերը, իսկ արժեքները այդ թվերի քառակուսիները
def createDict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i ** 2
    return d

print("#3 ", createDict(10))

#4. Գրել ծրագիր, որը տրված նույն երկարությամբ ցուցակներից կկառուցի բառարան՝ առաջինը օգտագործելով որպես բանալիների բաազմություն, երկրորդը՝ արժեքների
def createDictFromLists(d1, d2):
    if len(d1) != len(d2):
        return "Lists lengths must be the same"
    dict1 = {}
    for i in range(len(d1)):
        dict1[d1[i]] = d2[i]
    return dict1

d1 = [1, 2, 3, 4]
d2 = ['a', 'b', 'c', 'd']
print("#4 ", createDictFromLists(d1, d2))

#5. Գրել ծրագիր, որը տրված բառարանի համար կվերադարձնի ամենամեծ և ամենափոքր արժեքները
def getDictMinAndMaxVals(dict1):
    l1 = list(dict1.values())
    l1.sort()
    return "Min: "+str(l1[0]), "Max: "+str(l1[-1])

dict1 = {1: 25, 3: 14, 4: 33, 2: 11, 0: 55}
print("#5 ", getDictMinAndMaxVals(dict1) )

#6. Գրել ծրագիր, որը տրված 2 բառարանները կմիավորի իրար, այնպես, որ եթե 2֊ում էլ կան նույն բանալիով էլեմենտներ,
# ապա միավորված բառարանի համապատասխան էլեմենտը կլինի տրված բանալիով և որպես արժեք կընդունի այդ 2 էլեմենտների արժեքների գումարը։
def combineDicts(dict1, dict2):
    LongSet = dict1 if len(dict1) > len(dict2) else dict2
    ShortSet = dict1 if len(dict1) < len(dict2) else dict2
    for k, v in LongSet.items():
        if k in ShortSet:
            newVal = int(dict1[k]) + int(dict2[k])
            dict1.update({k: newVal})
        else:
            dict1.update({k: v})
    return dict1

dict1 = {0: 55, 1: 25, 2: 11 }
dict2 = {0: 5, 1: 15, 5: 33, 6: 11, 7: 3, 8: 125}
print("#6 ", combineDicts(dict1, dict2))

#7. Գրել ծրագիր, որը տրված տողի համար կկառուցի բառարան, այնպես, որ բառարանի բանալիները կլինեն տրված տողի սիմվոլները,
# իսկ համապատասխան արժեքները կլինեն տողում այդ սիմվոլի քանակը։
def getDictFromStrElmsAndCount(str1):
    set1 = set(str1)
    newDict = {}
    for x in set1:
        newDict[x] = str1.count(x)
    return newDict

str1 = "aaabbcdeeee"
print("#7 ", getDictFromStrElmsAndCount(str1))



