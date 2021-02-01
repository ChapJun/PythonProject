# 배열 (Array)
# 같은 종류의 데이터를 순차적으로 저장 (빠른접근가능 -- index // But, 추가/삭제가 쉽지않음)

# Ctrl + Alt + L (코드정렬)
# Ctrl + Shift + F10 (실행)

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
numSet = set(numList)

print('Set : ', numSet)

# Tuple Data cannot be changed!
numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9)

numDictionary = {'one': 1, 'two': 2, 'three': 3}

# using list comprehension
numDicKeys = [data for data in numDictionary.keys()]

print(numList)
for num in numList:
    print(type(num), " : ", num)

print(numTuple)
for num in numTuple:
    print(type(num), " : ", num)

print(numDictionary['one'])
print(numDicKeys)
