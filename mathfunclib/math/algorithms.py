from .simple import is_clockwise

def prims_algorithm(matrix):
    '''
    Implementation of "Prim's Algorithm".
    
    This finds a Minimal Spanning Tree for a
    weighted undirected graph.

    :param matrix: Takes an adjacency matrix as the input.

    :returns Weight: The sum of the min. spanning tree.
    :returns mask: The corresponding adjacency matrix
                   for the minimal spanning tree.
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be of type list[list[int]]."
    
    dim=len(matrix)
    mask=[[0 for x in range(len(matrix[0]))]for x in range(dim)]
    Tree=set([0])
    Weight=0
    for x in range(dim-1):
        min_edge,a,b=min([(matrix[x][y],x,y)for x in Tree for y in range(dim) if y not in Tree and matrix[x][y]!=0)
        Tree.add(b)
        mask[a][b]=matrix[a][b]
        mask[b][a]=matrix[a][b]
        Weight+=min_edge
        if len(Tree)==dim:
            break
    return Weight,mask

def dijkstras_algorithm(graph,start_node=0,INFINITY=float('inf')):
    '''
    Implementation of Dijkstra's Algorithm.
    It finds the shortest paths between nodes in a grid.

    :param graph: Takes an adjacency matrix as input.
    :param start_node: Optional tuple, default is 0.
    :param INFINITY: Optional integer, default is `float('inf')`.
                     Is used to set the "INFINITY" value.

    :returns: Shortest path between start_node and all other nodes.
    '''
    if type(graph)!=list:
        return "Parameter [graph] should be a list."
    if INFINITY!=float('inf') and type(INFINITY)!=int:
        return "Parameter [INFINITY] should be an integer if not float('inf')."
    
    n=len(graph)
    D = [INFINITY]*n
    D[start_node]=0
    cloud=[False for i in range(n)]
    for i in range(n):
        _, v = min((D[i],i) for i in range(n) if cloud[i] == False)
        cloud[v] = True
        for b,w in graph[v]:
            if cloud[b] == False:
                t = D[v] + w
                if t < D[b]:
                    D[b] = t
        flag=True
        for i in range(n):
            if cloud[i]==False:
                if D[i]!=INFINITY:
                    flag=False
                    break
        if flag:
            break
    return D

def floyd_warshall_algo(graph,INFINITY=float('inf')):
    '''
    Implementation of the Floyd-Warshall algorithm.
    This finds the shortest path between every node
    in the graph to every node in the graph.
    
    It's like applying Djikstra's Algorithm to every
    node in the graph.
    '''
    if type(graph)!=list:
        return "Parameter [graph] must be a list."
    if INFINITY!=float('inf') and type(INFINITY)!=int:
        return "Parameter [INFINITY] must be an integer if not float('inf')."
    
    n = len(graph)
    D = [[[INFINITY for i in range(n)] for j in range(n)] for k in range(n+1)]
    for v in range(n):
        D[0][v][v] = 0
        for e,w in graph[v]:
            D[0][v][e] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[k+1][i][j] = min(D[k][i][j],D[k][i][k]+D[k][k][j])
    return D[n][:][:]

def convex_hull_gift_wrapping(pts):
    '''
    Implementation of the Convex Hull Gift Wrapping Algorithm
    '''
    if type(pts)!=list:
        return "Parameter [pts] must be a list."
    for i in range(len(pts)):
        if type(pts[i])!=tuple:
            return "[pts] must contain only 2D tuples as the input."
    
    lp = min(pts)
    convex_hull=[lp]
    hull_not_finished = True
    while hull_not_finished:
        p = convex_hull[-1]
        for q in pts:
            if q!=p:
                flag = True
                for r in pts:
                    if r!=p and r!=q:
                        if is_clockwise(p,q,r) == False:
                            flag = False
                            break
                if flag:
                    if q==lp:
                        hull_not_finished = False
                    else:
                        convex_hull.append(q)
    return convex_hull
