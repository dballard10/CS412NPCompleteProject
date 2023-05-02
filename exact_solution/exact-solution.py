"""
Min Graph Coloring Exact Solution

NP-Complete Final Project

Hunter Bowles and Dylan Ballard

Exact Solution Code written by Hunter Bowles
"""
import itertools

def minColorExact(edges, vertices):
  """
  Input: undirected graph

  Output: Number c where c = the fewest number of colors to Color the graph

  Output will be formatted as a dictionary where the key is the vertex label which points to the color value assiciated with it
  """

  def containsDupes(item): ## might not get used???
    """
    Helper Method
    Input: list of tuples - potential output
    Output: true or false depending on if the input contains duplicate vertices
    """
    for i in range(len(item)):
      for j in range(len(item)):
        if i != j:
          if item[i][0] == item[j][0]:
            return True
    return False

  def verify(option):
    """
    Helper Method
    Input: selection of potential vertex colors
    Output: either None (invalid) or valid option
    """
    for x in range(len(option)):
      for y in range(x + 1, len(option)): ## iterates through every pair of vertices
        if x != y:
          if option[x][0] == option[y][0]: ## if they're the same vertex, it fails
            return None
          if option[y][0] in edges[vertices.index(option[x][0])]:
            if option[x][1] == option[y][1]: ## if neighbors have the same color, it fails
              return None
    return option
  
  complete = False
  colorNum = 1
  while complete == False and colorNum <= len(vertices): ## set up a while loop to continue until success

    colorNum += 1
    ## make a list of the vertices combined with each color
    combinations = list(itertools.product(vertices,list(range(0,colorNum))))
    ## Split the list into segments by vertex for another round of products
    combinations = [combinations[x:x + colorNum] for x in range(0, len(combinations), colorNum)]
    ## make a list of every combination of each vertex
    combinations = list(itertools.product(*combinations))

    ## for every potential csolution found, verify it. If it passes, you found the Min Color Graph
    for option in combinations:
      if verify(option) != None:
        print(colorNum) ## Don't forget to output the number of colors used
        return option
  print(colorNum)
  worstCase = []
  for z in range(len(vertices)):
    worstCase.append((vertices[z],z))
  return worstCase


def main():
  ## receive inputs from user and assemble the graph
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

  ## Calculate the Minimum Color Graph solution
  solution = list(minColorExact(edges, vertices))

  ## Sort the output, since the list isn't necessarily in numerical order
  solution.sort(key = lambda x: x[0])

  ## print out the colors for each vertex
  for pair in solution:
    print("{0} {1}".format(pair[0],pair[1]))


if __name__ == "__main__":
  main()