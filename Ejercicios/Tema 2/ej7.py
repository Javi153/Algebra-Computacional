def optimal_mat_mul(tam):
    mat = [[0 for _ in range(i + 1)] for i in range(len(tam))]
    for i in range(len(tam)):
        print(mat[i])


optimal_mat_mul((1,2,3,4,5,6))