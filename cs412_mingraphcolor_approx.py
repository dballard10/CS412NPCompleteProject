"""
Dylan Ballard
Min Graph Coloring approximate solution
Greedy approach
"""

def main():
    num_edges = int(input())

    graph = {}
    colored_graph = {}

    for _ in range(num_edges):
        v1, v2 = input().split()
        if v1 not in graph:
            graph[v1] = []
        graph[v1].append(v2)

        if v2 not in graph:
            graph[v2] = []
        graph[v2].append(v1)

        if v1 not in colored_graph:
            colored_graph[v1] = -1
        
        if v2 not in colored_graph:
            colored_graph[v2] = -1
        
    print(min_graph_coloring(graph, colored_graph))
    for v in colored_graph:
        print(v, colored_graph[v])

def min_graph_coloring(graph, colored_graph):
    colors = []

    for _ in range(len(graph)):   
        vertex_map = {}
        for v in graph:
            degree = len(graph[v])
            sat = 0
            for u in graph[v]:
                if colored_graph[u] > -1:
                    sat += 1
            #set degrees for each vertex
            #set saturation for each vertex
            vertex_map[v] = (degree, sat)

        #find vertices with high saturation
        sat_vertices = get_saturated(vertex_map, colored_graph)
        #find vertex with highest degree
        highest_degree_vertex = get_highest_degree(sat_vertices, colored_graph)

        #color vertex with minimum color possible
        if len(colors) == 0:
            colors.append(0)
            colored_graph[highest_degree_vertex] = colors[0]
        else:
            color = get_best_color(highest_degree_vertex, graph, colored_graph, colors)
            if color == -1:
                colors.append(len(colors))
                colored_graph[highest_degree_vertex] = len(colors) - 1
            else:
                colored_graph[highest_degree_vertex] = color

    return len(colors)

def get_saturated(vertex_map, colored_graph):
    sat_vertices = {}
    greatest_sat = -1

    for v in vertex_map:
        if colored_graph[v] == -1:
            curr_sat = vertex_map[v][1]
            if curr_sat > greatest_sat:
                sat_vertices = {}
                greatest_sat = curr_sat
                sat_vertices[v] = vertex_map[v]
            if curr_sat == greatest_sat:
                sat_vertices[v] = vertex_map[v]
    return sat_vertices

def get_highest_degree(sat_map, colored_graph):
    highest_degree = -1
    highest_vertex = -1
    for v in sat_map:
        if colored_graph[v] == -1:
            curr_degree = sat_map[v][0]
            if curr_degree > highest_degree:
                highest_degree = curr_degree
                highest_vertex = v
    return highest_vertex

def get_best_color(v, graph, colored_graph, colors):
    remaining_colors = colors.copy()
    for u in graph[v]:
        color = colored_graph[u]
        if color > -1:
            if color in remaining_colors:
                remaining_colors.remove(color)
        
    if len(remaining_colors) > 0:
        return remaining_colors[0]
    return -1

if __name__ == "__main__":
    main()