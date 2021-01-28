# 배열 (Array)
# 같은 종류의 데이터를 순차적으로 저장 (빠른접근가능 -- index // But, 추가/삭제가 쉽지않음)

# Ctrl + Alt + L (코드정렬)
# Ctrl + Shift + F10 (실행)

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9) # Data cannot be changed!
numDictionary = {'one': 1, 'two': 2, 'three': 3}

numDicKeys = [data for data in numDictionary.keys()] # using list comprehension

print(numList)
for num in numList:
    print(type(num), " : ", num)

print(numTuple)
for num in numTuple:
    print(type(num), " : ", num)

print(numDictionary['one'])
print(numDicKeys)