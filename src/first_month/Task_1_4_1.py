#1. Գրել ծրագիր, որը կվերադարձնի տրված լիստը առանց կրկնվող էլեմենտների
lst1 = [1,2,2,2,5,7,8,1,11]
lst2 = [0,2,2,3,5,7,8,0,10]

def getListWithoutDuplicates(lst):
    st = set(lst1)
    return list(st)

print("#1 ", getListWithoutDuplicates(lst1))

#2. Գրել ծրագիր, որը տրված 2 ցուցակների համար կվերադարձնի նրանց ընդհանուր էլեմենտների բազմությունը
def getIntersection(lst1, lst2):
    return set(lst1) & set(lst2)

print("#2 ", getIntersection(lst1, lst2))

#3. Գրել ծրագիր, որը տրված երկու ցուցակների համար կվերադարձնի այն էլեմենտները, որոնք կան առաջինում, բայց չկան երկրորդում
def getDifference(lst1, lst2):
    return set(lst1) - set(lst2)

print("#3 ", getDifference(lst1, lst2))

#4. Գրել ծրագիր, որը տրված երկու ցուցակների համար կվերադարձնի այն էլեմենտները, որոնք կան կամ առաջինում, կամ երկրորդում,
# բայց ոչ միաժամանակ երկուսում էլ։
def getSymmetricDifference(lst1, lst2):
    return set(lst1) ^ set(lst2)

print("#4 ", getSymmetricDifference(lst1, lst2))

#5. Գրել ծրագիր, որը տրված երկու ցուցակների համար կվերադարձնի այն էլեմենտները, որոնք կան կամ առաջին ցուցակում,
# կամ երկրորդ, կամ երկուսում միաժամանակ
def getUnion(lst1, lst2):
    return set(lst1) | set(lst2)

print("#5 ", getUnion(lst1, lst2))

#6. Գրել ծրագիրը, որը կստանա բազմություն և էլեմենտի արժեք, ու բազմությունից կհեռացնի տվյալ արժեքով էլեմենտը։
def removeElemntFromSet(el, st):
    st.remove(el)
    return st

st = {'b','c','a','d'}
el = 'a'
print("#6 ", removeElemntFromSet(el, st))

#7. Գրել ծրագիր, որը կստանա թվերի բազմություն և կվերադարձնի ցուցակ,
# որի էլեմենտները կլինեն բազմության էլեմենտների խորանարդները։
def getListFromSetElCabs(numSet):
    newList = []
    for x in numSet:
        newList.append(x ** 3)
    return newList

numSet = {1,2,3,4,5}
print("#7 ", getListFromSetElCabs(numSet))
