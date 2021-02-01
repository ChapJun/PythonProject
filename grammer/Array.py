# 배열 (Array) - 파이썬 리스트 활용
# 같은 종류의 데이터를 순차적으로 저장 (빠른접근가능 -- index // But, 추가/삭제가 쉽지않음)

# Ctrl + Alt + L (코드정렬)
# Ctrl + Shift + F10 (실행)

# 1차원 배열
data1 = [1, 2, 3, 4, 5]
print(data1)

# 2차원 배열
data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data2)
print(data2[0], "->", data2[0][0], ",", data2[1][2])

# 연습 1 : 2차원배열(data2) 9, 8, 7 순서로 출력해보기
print('data2 : {0}, {1}, {2}'.format(data2[2][2], data2[2][1], data2[2][0]))
print('data2 : %d %d %d' % (data2[2][2], data2[2][1], data2[2][0]))

# 연습 2 : 전체 이름안에 M이 몇번 나왔는지 빈도수 출력
list = ["Braund, Mr. Owen Marris", "Rice, Master. Eugne", 'Mr. Joseph J']
m_cnt = 0
for name in list:
    m_cnt += name.count('M')

print(m_cnt)

m_cnt = 0

for name in list:
    for index in range(len(name)):  # range([시작숫자], 종료숫자, [step])
        if name[index] == 'M':
            m_cnt += 1

print(m_cnt)
