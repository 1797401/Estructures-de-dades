def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    matriu = [[0] * n for _ in range(n)]
    graus=[]
    for i in edges:
        matriu[i[0]-1][i[1]-1]=1
        matriu[i[1]-1][i[0]-1]=1
    deg = [sum(fila) for fila in matriu]
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if matriu[i][j] == 1:
                for k in range(j + 1, n):
                    if matriu[i][k] == 1 and matriu[j][k] == 1:
                        graus.append( deg[i] + deg[j] + deg[k] -6)

    if graus:
        return min(graus)
    return -1