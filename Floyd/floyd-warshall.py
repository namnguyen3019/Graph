'''
    n = size of the adjacency matrix
    dp = the memo table that will contain APSP(All-paired shortest path) SOLV
    next = MATRIX used to reconstruct shortest paths

    function floydWarshall(m):
        setup(m)

        # Execute FWa all pairs shortest path algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        next[i][j] = next[i][k]
        
        # Detect and propagate negative cycles:
        propagateNegativeCycles(dp, n):

        return dp

'''
def createGraph(n):
    m = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0
    
    return m



def floydWarshall(m):
    # Setup function

    n = len(m)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    # This next matrix is for path reconstruciton
    # Path from i to j: at first is j (which mean go directly from i to j) if m[i][j] not infinite

    next = [[None for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            dp[r][c] = m[r][c]
            if m[r][c] is not float('inf'):
                next[r][c] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[i][k]

    # Detect negative cycle: run the above for loop once again
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = float('inf')
                    next[i][j] = -1
    # TODO: 

    def reconstruciton(matrixPath, start, end):
        at = start
        path = [start]
        while at != end:
            node = matrixPath[at][end]
            path.append(node)
            at = node
        
        return path
    
    print(reconstruciton(next, 0, 1))

    return dp

if __name__ == "__main__":
    n = 5
    m = createGraph(n)
    m[0][1] = 10
    m[1][0] = 5
    m[0][2] = 3
    m[2][3] = 2
    m[3][1] = 2

    print(floydWarshall(m))