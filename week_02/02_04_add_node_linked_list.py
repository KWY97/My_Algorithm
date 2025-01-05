class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur
    
    # Q. 링크드 리스트에서 index번 위치에 value 값을 가지는 원소를 추가하시오.
    def add_node(self, index, value):
        new_node = Node(value)

        # 인덱스가 0일 때
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        # 인덱스가 0이 아닐 때
        else:
            index_minus_1_node = self.get_node(index - 1)
            next_node = index_minus_1_node.next

            index_minus_1_node.next = new_node
            new_node.next = next_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.print_all()

print("노드 추가 후")
linked_list.add_node(1, 6)
linked_list.add_node(3, 11)
linked_list.add_node(0, 99)
linked_list.print_all()

