import heapq

def dijkstra(graph,start,end):
    pq = [(0,start)]
    distances = {node: float('inf') for node in graph }
    distances[start] = 0

    previos = {node: None for node in graph}

    while pq:
        currentDistance,currentNode = heapq.heappop(pq)
        if(currentNode == end):
            break
        if currentDistance > distances[currentNode]:
            continue

        for neighbour,weight in graph[currentNode]:
            distance = currentDistance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previos[neighbour] = currentNode
                heapq.heappush(pq,(distance,neighbour))
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previos[current]

    path.reverse()
    if distances[end] == float('inf'):
        return float('inf'),[]
    return distances[end],path
graph ={
    'a':[('b',4),('c',2)],
    'b':[('a',4),('c',1),('d',5)],
    'c':[('a',2),('b',1),('d',8)],
    'd':[('b',5),('c',8)]
}
distance,path = dijkstra(graph,'a','d')
print("Distance: ",distance)
print("path: ",(" -> ").join(path))
