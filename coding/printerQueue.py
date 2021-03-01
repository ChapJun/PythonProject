# 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고,
# 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때,
# 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
# 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

def solution(n, m, data):
    cnt = 0
    mx = max(data)
    data_list = list()
    for i in range(0, len(data)):
        data_list.append((i, data[i]))
    isFind = True
    # 1 2 3 4
    while isFind:
        mx = max(data)
        for tu in data_list:
            if tu[1] == mx:
                #print('Max : ', mx, ' tu : ', tu)
                cnt += 1
                if m == tu[0]:
                    isFind = False
                    break
                else:
                    data.remove(tu[1])
                    #print(data)
                    data_list.remove(tu)
                    break
            else:
                #print('before : ', data_list)
                tmp = tu;
                #print(tmp)
                data_list.remove(tu)
                #print(tmp)
                data_list.append(tmp)
                #print('after : ' , data_list)
                break
    print(cnt)

def main():
    case = int(input())
    for i in range(0, case):
        n, m = list(map(int, input().split(' ')))
        data = list(map(int, input().split(' ')))
        solution(n, m, data)
        #print('\n')


if __name__ == "__main__":
    main()