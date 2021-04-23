#1. Գրել ծրագիր, որը տրված բառարանում կավելացնի նոր արժեք տրված բանալիով
dict1 = { "brand": "Ford",  "model": "Mustang",  "year": 1964}
dict1["color"] = "red"
print('#1 ', dict1)

#2. Գրել ծրագիր, որը կմիավորի տրված 2 բառարանները
d1 = {1:'a', 2: 'b'}
d2 = {3: 'c', 4: 'd', 5: 'e'}
d1.update(d2)
print('#2 ', d1)

#3. Գրել ծրագիր, որը տրված n թվի համար կկառուցի բառարան,  որի բանալիները կլինեն 1֊ից n թվերը, իսկ արժեքները այդ թվերի քառակուսիները
d3 = {}
n = 10
for i in range(1, n):
    d3[i] = i**2
print("#3 ", d3)

#4. Գրել ծրագիր, որը տրված նույն երկարությամբ ցուցակներից կկառուցի բառարան՝ առաջինը օգտագործելով որպես բանալիների բաազմություն, երկրորդը՝ արժեքների
d1 = [1, 2, 3, 4]
d2 = ['a', 'b', 'c', 'd']
dict1 = {}
for i in range(len(d1)):
    dict1[d1[i]] = d2[i]
print("#4 ", dict1)

#5. Գրել ծրագիր, որը տրված բառարանի համար կվերադարձնի ամենամեծ և ամենափոքր արժեքները
dict1 = {1: 25, 3: 14, 4: 33, 2: 11, 0: 55}
l1 = list(dict1.values())
l1.sort()
print("#5  Min: ", l1[0], '; Max: ',l1[-1] )

#6. Գրել ծրագիր, որը տրված 2 բառարանները կմիավորի իրար, այնպես, որ եթե 2֊ում էլ կան նույն բանալիով էլեմենտներ,
# ապա միավորված բառարանի համապատասխան էլեմենտը կլինի տրված բանալիով և որպես արժեք կընդունի այդ 2 էլեմենտների արժեքների գումարը։
dict1 = {0: 55, 1: 25, 2: 11 }
dict2 = {0: 5, 1: 15, 5: 33, 6: 11, 7: 3, 8: 125}
LongSet = dict1 if len(dict1)>len(dict2) else dict2
ShortSet = dict1 if len(dict1)<len(dict2) else dict2
for k, v in LongSet.items():
    if k in ShortSet:
        newVal = int(dict1[k])+int(dict2[k])
        dict1.update({k: newVal})
    else:
        dict1.update({k: v})
print("#6 ", dict1)

#7. Գրել ծրագիր, որը տրված տողի համար կկառուցի բառարան, այնպես, որ բառարանի բանալիները կլինեն տրված տողի սիմվոլները,
# իսկ համապատասխան արժեքները կլինեն տողում այդ սիմվոլի քանակը։
str1 = "aaabbcdeeee"
set1 = set(str1)
newDict = {}
for x in set1:
    newDict[x] = str1.count(x)
print("#7 ", newDict)



