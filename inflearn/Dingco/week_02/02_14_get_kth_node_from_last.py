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

    # 전체 길이 구하고 뒤에서 접근하는 방식
    # def get_kth_node_from_last(self, k):
    #     length = 1
    #     cur = self.head
    # 
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    # 
    #     target_index = (length - k)
    #     cur = self.head
    # 
    #     for _ in range(target_index):
    #         cur = cur.next
    #
    #     return cur

    # 포인터 두 개 두고 하는 방법
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for _ in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)