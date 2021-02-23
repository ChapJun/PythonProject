# 링크드리스트 (Linked List) - 연결 리스트
# 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
# 파이썬은 리스트 타입이 링크드리스트의 기능을 모두 지원

# 별도의 주소 공간이 필요
# 데이터 검색 속도가 느림 (인덱스 미존재)
# 중간 데이터 삭제시, 연결 재구성 작업 필요

# 노드(Node) - 데이터 저장 단위
# 포인터(Pointer) - 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

class Node:
    def __init__(self, data, next=None):  # 생성자
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):  # 생성자
        self.head = Node(data)

    def add(self, data):  # 맨 끝 추가
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):  # 출력
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        print(node.data)

    def insert(self, data, idx):  # 중간삽입
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            cnt = 0
            while cnt < idx - 1:
                node = node.next
                cnt += 1
            node.next = Node(data, node.next)

    def delete(self, data):
        if self.head == '':
            return
        node = self.head
        if node.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

    def select(self, data):
        if self.head == '':
            return None
        node = self.head
        if node.data == data:
            return node.data
        else:
            while node.next:
                if node.data == data:
                    return node.data
                else:
                    node = node.next


linkedlist1 = NodeMgmt(0)

for i in range(1, 10):
    linkedlist1.add(i)

print(linkedlist1.select(4))

linkedlist1.insert(200, 2)
linkedlist1.insert(500, 5)
# linkedlist1.desc()

# print("=====================")

linkedlist1.delete(200)
# linkedlist1.desc()

# print("=====================")

linkedlist1.delete(0)
# linkedlist1.desc()
