def dijkstras(graph, S):
    distance = [float("inf") for g in graph]
    distance[S] = 0
    
    parents = [None for g in graph]
    
    path = set()
    sptSet = [False for g in graph]
    
    notVisited = [i for i in range(len(graph))]
    while len(notVisited) > 0:
        minIndx = getMinDist(distance, notVisited)
        for v in range(len(graph)):
            if (v in notVisited
            and distance[minIndx] != float("inf")
            and graph[minIndx][v] != 0
            and distance[v] > graph[minIndx][v] + distance[minIndx]):
                distance[v] = graph[minIndx][v] + distance[minIndx]
                parents[v] = minIndx
            
        del notVisited[notVisited.index(minIndx)]
    return path
    
def getMinDist(distance, notVisited):
    mind = float("inf")
    mIdx = 0
    for idx, vDist in enumerate(distance):
        if idx in notVisited and vDist != float("inf") and vDist < mind:
            mind = vDist
            mIdx =  idx
        
    return mIdx
    
#           S  T   Y  X  Z
dijkstras([[0, 10, 5, 0, 0],
           [0, 0,  2, 1, 0], 
           [0, 3,  0, 9, 2], 
           [0, 0,  0, 0, 4], 
           [0, 0,  0, 0, 0]], 0)
