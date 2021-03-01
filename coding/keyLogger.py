# 5398 키로거

def solution(data):
    left = []
    right = []
    for i in range(len(data)):
        if data[i] == '<':
            if left:
                right.append(left.pop())
        elif data[i] == '>':
            if right:
                left.append(right.pop())
        elif data[i] == '-':
            if left:
                left.pop()
        else:
            left.append(data[i])
    print(left)
    print(right)
    left.extend(reversed(right))
    print(''.join(left))


def main():
    testcase = int(input())
    for i in range(testcase):
        data = list(input())
        solution(data)


if __name__ == "__main__":
    main()
