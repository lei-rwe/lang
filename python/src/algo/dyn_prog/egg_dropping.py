import sys

matrix = [[0] * 6] * 2

def print2d(matrix):
    s = ""
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            s += "{0:<3d}".format( matrix[i][j] )
        s += "\n"
    print s

print2d(matrix)

def drops(n,h):
    if (n == 1 or h == 0 or h == 1):
        return h

    minimum = sys.maxint

    for x in range(1, h+1):
        minimum = min(minimum, 1 + max(drops(n - 1, x - 1), drops(n, h - x)))

    return minimum

def solvepuzzle(E, F):
    numdrops = [[0]*(F+1) for _ in range(E+1)]

    for e in range(0, F+1):
        numdrops[1][e] = e
    print2d(numdrops)

    # This loop fills up the matrix
    for e in range(2, E+1):
        for f in range(1, F+1):
            # Defines the minimum as the highest possible value
            minimum = sys.maxint

            # Evaluates 1+min{max(numeggs[e][f-x],numeggs[e-1][x-1])), for x:1,2,3...f-1,f}
            for x in range(1, f+1):
                # print F, E, e, f, x, numdrops[e][f-x], numdrops[e-1][x-1]
                minimum=min(minimum,(1+max(numdrops[e][f-x],numdrops[e-1][x-1])))
                
            # Defines the minimum value for numeggs[e][f]
            numdrops[e][f]=minimum;

    print2d(numdrops)

if __name__ == "__main__":
    solvepuzzle(4, 8)