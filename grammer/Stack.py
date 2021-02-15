# 스택 (Lifo - List in, First Out)
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조

stack = list()

stack.append(3)
stack.append(5)
stack.append(7)

print(stack.pop())
print(stack.pop())
print(stack.pop())


# 연습1 : 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기

def push_stack(data):
    stack.insert(len(stack) + 1, data)


def pop_stack():
    if len(stack) > 0:
        print(stack[-1])  # 맨 끝에 있는 데이터
        del stack[-1]
    else:
        print("Empty Stack!!")


for index in range(1, 3):
    push_stack(index)

print(stack)

pop_stack()
pop_stack()
pop_stack()
