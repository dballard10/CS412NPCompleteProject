"""
Min Graph Coloring Exact Solution

NP-Complete Final Project

Hunter Bowles and Dylan Ballard

Exact Solution Code written by Hunter Bowles
"""
import itertools

def verify(permutation, vertices, edges):

  """
  Takes list of vertices with colors and list of edges/vertices
  returns validity of color graph
  """

  def isValidPairing(p1, p2):

    """
    Conditions to be invalid color set:
    1) 2 color assignments for same vertex
    2) 2 vertices with same color are neighbors
      a) IF the two are neighbors, then they MUST have different colors
      b) if they are not neighbors, they can have the same
      c) if they are not neighbors, they can still be different, too

    I mean, that's really all there is to it

    If the tuples in question pass both tests, return true
    If it fails any of these tests, then return false
    """

    if p1[0] == p2[0]: ## if the two tuples represent the same vertex, no need to do more.

      return False
    if p2[0] in edges[vertices.index(p1[0])]: ## if they're neighbors, confirm the color difference
      if p1[1] == p2[1]:
        return False
      else:
        return True

  """
  Check to ensure fully unique vertices
  check that neighbors have different colors
  """

  for pair in permutation:
    for other in permutation:
      if pair != other:
        if isValidPairing(pair, other) == False:
          return None
  return permutation

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

    graph_options = list(itertools.permutations(potential_colors, len(vertices)))

    for option in graph_options:
      if verify(option, vertices, graph) != None:
        print(colorNum)
        return option
  


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
  solution = minColorExact(edges, vertices)

  for pair in solution:
    print("{0} {1}".format(pair[0],pair[1]))

if __name__ == "__main__":
  main()
