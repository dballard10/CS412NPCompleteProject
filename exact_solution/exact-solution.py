"""
Min Graph Coloring Exact Solution

NP-Complete Final Project

Hunter Bowles and Dylan Ballard

Exact Solution Code written by Hunter Bowles
"""
import itertools

def main():

  def minColorExact():

    """
    Input: undirected graph

    Output: list of color/vertex pairs for minimum color graph

    Output will be formatted as a dictionary where the key is the vertex label which points to the color value assiciated with it
    """

    def verify(option):
        """
        Helper Method
        Input: selection of potential vertex colors
        Output: either None (invalid) or valid option
        """
        for x in range(len(option)):
            for y in range(x + 1, len(option)):
                if x != y:
                    if option[x][0] == option[y][0]:
                        return None
                    if option[y][0] in edges[vertices.index(option[x][0])]:
                        if option[x][1] == option[y][1]:
                            return None
        return option
    
    colorNum = 1
    for i in range(len(vertices)):
        colorNum += 1
        combinations = itertools.product(*([[(v, c) for c in range(colorNum)] for v in vertices]))
        for option in combinations: ## used a generator here to save memory space
            if verify(option) is not None:
                print(colorNum)
                yield option
                return
    print(colorNum) ##print out the number of colors used
    worstCase = [(v, i) for i, v in enumerate(vertices)]
    yield worstCase



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

  # Calculate the Minimum Color Graph solution
  solution = next(minColorExact())

  # print out the colors for each vertex
  for pair in solution:
      print("{0} {1}".format(pair[0], pair[1]))



if __name__ == "__main__":
  main()