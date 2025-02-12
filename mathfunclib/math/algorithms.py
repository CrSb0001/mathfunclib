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

def convex_hull_DC(pts):
    '''
    Implementation of the Convex Hull Divide and conquer Algorithm
    '''
    if type(pts)!=list:
        return "Paramter [list] must be a list."
    for i in range(len(pts)):
        if type(pts[i])!=tuple:
            return "[pts] may only contains 2D tuples as the input."
    
    x_sort = sorted(pts)
    def divideCH(alist):
        l = len(alist)
        if l <= 5:
            return convex_hull_gift_wrapping(alist)
        mid = l//2
        left = divideCH(alist[:mid])
        right = divideCH(alist[mid:])
        return mergeCH(left, right)

    def mergeCH(left, right):
        top_r = max(left) 
        top_l = min(right) 
        bot_r = top_r
        bot_l = top_l
            
        curr_right_index = right.index(top_l)
        curr_left_index = left.index(top_r)
        
        hull_copy = left[:curr_left_index + 1] + right[curr_right_index:] + right[curr_right_index:curr_right_index + 1] + left[curr_left_index:]
        len_h = len(hull_copy)
        
        top_r_index = curr_left_index
        top_l_index = top_r_index + 1
        bot_l_index = top_l_index + len(right)
        bot_r_index = bot_l_index + 1
        
        prev_r = None
        prev_l = None
        while True:
            prev_r = top_r
            prev_l = top_l
            while is_clockwise(top_r, top_l, hull_copy[top_l_index + 1]) == False:
                top_l_index += 1
                top_l = hull_copy[top_l_index]

            while is_clockwise(top_l, top_r, hull_copy[top_r_index - 1]):
                top_r_index -= 1            
                top_r = hull_copy[top_r_index]
            
            if top_r == prev_r and top_l == prev_l:
                break
        
        prev_r = None
        prev_l = None
        while True:
            prev_r = bot_r
            prev_l = bot_l
            
            while is_clockwise(bot_r, bot_l, hull_copy[bot_l_index - 1]):
                bot_l_index -= 1
                bot_l = hull_copy[bot_l_index]
                
            while True:
                if bot_r_index + 1 < len_h:
                    if is_clockwise(bot_l, bot_r, hull_copy[bot_r_index + 1]) == False:
                        bot_r_index += 1
                        bot_r = hull_copy[bot_r_index]
                    else:
                        break
                else:
                    bot_r_index = -1     
            if bot_r == prev_r and bot_l == prev_l:
                break
        
        if bot_r_index == 0:
            convex_hull = hull_copy[0:top_r_index + 1] + hull_copy[top_l_index:bot_l_index + 1]
        else:
            convex_hull = hull_copy[0:top_r_index + 1] + hull_copy[top_l_index:bot_l_index + 1] + hull_copy[bot_r_index:]
        return convex_hull 
    
    return divideCH(x_sort)
