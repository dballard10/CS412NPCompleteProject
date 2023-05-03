import random

def main():
    
    numVerts = int(input())

    numEdges = int(input())

    edges = []

    for i in range(numVerts):
        for j in range(i + 1,numVerts):
            edges.append((i,j))
    
    random.shuffle(edges)

    for a in range(numEdges):
        print("{0} {1}".format(edges[a][0],edges[a][1]))


main()