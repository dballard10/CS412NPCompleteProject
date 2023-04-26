"""
Min Graph Coloring Exact Solution

NP-Complete Final Project

Hunter Bowles and Dylan Ballard

Exact Solution Code written by Hunter Bowles
"""
import itertools

def verify(permutations, vertices, edges):
  """
  Takes list of vertices with colors and list of edges/vertices
  returns validity of color graph
  """

  ##permutations = list(itertools.permutations(colored_graph, 3))

  for perm in permutations:
    """
    Check to ensure fully unique vertices
    check that neighbors have different colors
    """


  return None

def minColorExact(graph, vertices):
  """
  Input: undirected graph

  Output: Number c where c = the fewest number of colors to Color the graph
  Output will be formatted as a dictionary where the key is the vertex label which points to the color value assiciated with it
  """

  complete = False
  colorNum = 0
  while complete == False:
    colorNum += 1 ## increase the number of colors until a valid graph is found
    colors = [] ## sets starting condition where no colors are used
    for i in range(colorNum):
      colors.append(i)

    potential_colors = list(itertools.product(vertices,colors)) ## display all possible color assignments for reference

    ## print(potential_colors)

    """
    Process for finding min color graph:
    
    1) generate a single set of colored vertices
    2) see if any neighbors have the same color
    3) if so, repeat with a new combination of colors
    4) if not, then you have a graph
    5) if all combinations fail to produce, add another color
    6) repeat until success

    The process is given a list of all vertices with all color assignments. How can this work??

    Consider: rework list to be a list for each vertex?
    Also Consider: Iterate through each unique vertex and combine with others
    """

    final_graph = verify(list(itertools.permutations(potential_colors, len(vertices))), vertices, graph)

    complete = True

  return final_graph


def main():
  numEdges = int(input())

  vertices = []
  edges = []
  
  for _ in range(numEdges):
    x,y = input().split()
    if x not in vertices:
      vertices.append(x)
      edges.append([])
    if y not in vertices:
      vertices.append(y)
      edges.append([])
    edges[vertices.index(x)].append(y)
    edges[vertices.index(y)].append(x)
  print("The minimum color graph for the provided graph is {}".format(minColorExact(edges, vertices)))

  ##print(vertices)
  ##print(edges)

if __name__ == "__main__":
  main()
