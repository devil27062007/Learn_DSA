def find(parent,x):
    if parent[x]!= x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,rank,x,y):
    root_x = find(parent,x)
    root_y = find(parent,y)

    if root_x!=root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def krushkals(vertices,edges):
    edges.sort(key = lambda x: x[2])
    parent = {}
    rank = {}

    for v in vertices:
        parent[v] = v
        rank[v] = 0
    
    mst = []
    tc = 0
    for u,v,cost in edges:
        if find(parent,u) != find(parent,v):
            union(parent, rank, u, v)
            mst.append((u, v, cost))
            tc += cost
    return mst, tc

vertices = ['a','b','c','d','e']
edges = [
    ('a','b',1),
    ('a','c',5),
    ('b','c',4),
    ('b','d',2),
    ('c','d',3),
    ('c','e',6),
    ('d','e',7)
]

mst , tc = krushkals(vertices,edges)
print("Total cost: ",tc)
for u,v,c in mst:
    print(u +" -> " + v + " = " + str(c))
