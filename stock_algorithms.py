import heapq

# ------------------------------
# 1️⃣ Divide and Conquer - Max Profit Finder
# ------------------------------
def max_profit_divide_and_conquer(prices):
    def helper(low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        left_profit = helper(low, mid)
        right_profit = helper(mid + 1, high)
        cross_profit = max(prices[mid+1:high+1]) - min(prices[low:mid+1])
        return max(left_profit, right_profit, cross_profit)
    return helper(0, len(prices) - 1) if prices else 0

# ------------------------------
# 2️⃣ Heap Algorithm - Top K Stocks
# ------------------------------
def top_k_profitable_stocks(stocks, k):
    if not stocks:
        return []
    return heapq.nlargest(k, stocks.items(), key=lambda x: x[1])

# ------------------------------
# 3️⃣ Graph Algorithm - Dijkstra (Simulated for stock days)
# ------------------------------
def dijkstra_shortest_path(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        (dist, current) = heapq.heappop(pq)
        if dist > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
