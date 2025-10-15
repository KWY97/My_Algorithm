import heapq
from collections import defaultdict
# 기본 템플릿 방식
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node not in costs:
                costs[cur_node] = cur_cost

                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_node))

        if len(costs) < n:
            return -1
        return max(costs.values())

# Dist 기반 방식
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        dist = [10**15] * (n + 1)
        dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_w, cur_v = heapq.heappop(pq)
            if cur_w > dist[cur_v]:
                continue
            for w, next_v in graph[cur_v]:
                next_w = cur_w + w
                if next_w < dist[next_v]:
                    dist[next_v] = next_w
                    heapq.heappush(pq, (next_w, next_v))

        ans = max(dist[1:])
        return -1 if ans == 10**15 else ans
