from collections import deque

# DFS 풀이 (재귀)
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS 풀이 (큐)
# class Solution(object):
#     def maxDepth(self, root):
#         max_depth = 0
#         if not root:
#             return 0
#         q = deque([root, 1])
#
#         while q:
#             cur_node, cur_depth = q.popleft()
#             max_depth = max(max_depth, cur_depth)
#
#             if cur_node.left:
#                 q.append([cur_node.left, cur_depth+1])
#             if cur_node.right:
#                 q.append([cur_node.right, cur_depth+1])
#
#         return max_depth