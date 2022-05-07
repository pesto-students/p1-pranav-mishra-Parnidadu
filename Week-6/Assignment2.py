#  problem spiral Order matrix II
# Problem Description Given a matrix of m * n elements (m rows, n columns), return allelements of the matrix in spiral order.

# Example: Given the following matrix: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] You should return[1, 2, 3, 6, 9, 8, 7, 4, 5]


def spiralMatrix(mat):
    left = 0
    right = len(mat[0])-1 
    top=0 
    bottom= len(mat)-1

    spiral_list = []
    while(1):
        # Moving toward right
        if left>right:
            break
        for i in range(left, right+1):
            spiral_list.append(mat[top][i])
        top+=1
        # Moving down
        if top>bottom:
            break
        for i in range(top, bottom+1):
            spiral_list.append(mat[i][right])
        right-=1

        # Moving left

        if right<left:
            break
        for i in range(right,left-1,-1):
            spiral_list.append(mat[bottom][i])
        bottom-=1

        # Moving up

        if bottom<top:
            break

        for i in range(bottom,top-1,-1):
            spiral_list.append(mat[i][left])
        left+=1

    return spiral_list


mat = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]

print(spiralMatrix(mat))