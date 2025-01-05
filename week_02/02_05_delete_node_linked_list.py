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
    
    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            index_minus_1_node = self.get_node(index - 1)
            next_node = index_minus_1_node.next

            index_minus_1_node.next = new_node
            new_node.next = next_node

    # Q. 링크드 리스트에서 index번째 원소를 제거하시오.
    def delete_node(self, index):
        # 인덱스가 0일 때
        if index == 0:
            self.head = self.head.next
        # 인덱스가 0이 아닐 때
        else:
            prev_node = self.get_node(index - 1)
            index_node = self.get_node(index)

            prev_node.next = index_node.next



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.print_all()
print()

print("노드 추가 후")
linked_list.add_node(1, 6)
linked_list.add_node(3, 11)
linked_list.add_node(0, 99)
linked_list.print_all()
print()

print("노드 제거 후")
linked_list.delete_node(2)
linked_list.delete_node(0)
linked_list.print_all()