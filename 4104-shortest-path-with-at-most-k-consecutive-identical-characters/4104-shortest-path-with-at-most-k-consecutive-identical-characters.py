class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if k == 0:
            return -1 if n > 1 else 0
    
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        start_char = labels[0]
        dist = {(0, start_char, 1): 0}
        pq = [(0, 0, start_char, 1)]

        best = float('inf')

        while pq:
            d, u, last_char, streak = heapq.heappop(pq)
            
            if d > dist.get((u, last_char, streak), float('inf')):
                continue
            
            if u == n - 1:
                best = min(best, d)
                return d
            
            for v, w in graph[u]:
                if labels[v] == last_char:
                    new_streak = streak + 1
                    if new_streak > k:
                        continue
                    new_char = last_char
                else:
                    new_streak = 1
                    new_char = labels[v]
                
                new_d = d + w
                key = (v, new_char, new_streak)
                if new_d < dist.get(key, float('inf')):
                    dist[key] = new_d
                    heapq.heappush(pq, (new_d, v, new_char, new_streak))

        return best if best != float('inf') else -1