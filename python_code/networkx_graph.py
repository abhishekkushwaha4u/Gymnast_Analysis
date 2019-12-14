import networkx as nx

def draw_graph(nPoints, points):
    G = nx.Graph()
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ] 
    
    points = [(120, 184), (160, 184), (144, 184), (144, 232), (144, 280), (184, 192),
    (184, 256), (152, 288), (184, 264), (144, 288), None, (192, 264), (152, 296), None, (176, 224)]

    for pair in POSE_PAIRS:
         part_a = pair[0]
         part_b = pair[1]
         if(points[part_a] and points[part_b]):
             G.add_edge(part_a, part_b)

    # print(G)
    # print(G.nodes)
    k = set()
    for node in G.nodes:
        print(node)
        neig = G.neighbors(node)
        
        print(neig)
        print(dict(neig))

        # k.add([node])
        # for iter in neig:
            # print(iter, end = '', sep=' ')
            # neig_neig = G.neighbors(iter)
            # for iter2 in neig_neig:
            #     print(iter2, end = '')

    # print(G.edges)
    
draw_graph(nPoints=15, points= [(120, 184), (160, 184), (144, 184), (144, 232), (144, 280), (184, 192),
    (184, 256), (152, 288), (184, 264), (144, 288), None, (192, 264), (152, 296), None, (176, 224)])

# Points
