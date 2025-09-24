# 리스트가 주어질 때 트리로 만들기
tree_list = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(value=3)
root.left = TreeNode(value=9)
root.right = TreeNode(value=20)
root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)


# 트리 만들기 자동화 버전 (BFS 사용) - 문제에 이런 류는 안나옴 (참고용)
# from collections import deque

# def build_tree(tree_list):
#     if not tree_list or tree_list[0] is None:
#         return None
#
#     root = TreeNode(tree_list[0])
#     q = deque([root])
#     i = 1
#
#     while q and i < len(tree_list):
#         node = q.popleft()
#
#         # 왼쪽 자식
#         if i < len(tree_list) and tree_list[i] is not None:
#             node.left = TreeNode(tree_list[i])
#             q.append(node.left)
#         i += 1
#
#         # 오른쪽 자식
#         if i < len(tree_list) and tree_list[i] is not None:
#             node.right = TreeNode(tree_list[i])
#             q.append(node.right)
#         i += 1
#
#     return root
