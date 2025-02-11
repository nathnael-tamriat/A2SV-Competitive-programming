class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        move = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

        row_length = len(img)
        col_length = len(img[0])

        res = [[0]*col_length for _ in range(row_length)]

        def check(i,j):
            return ( i < row_length and i >= 0) and ( j < col_length and j >= 0)

        #finding all sum_values and number of valid elements
        def evaluate(i,j):
            total_sum = 0
            total_length = 0
            for row,col in move:
                new_i = row+i
                new_j = col + j
                if check(new_i,new_j):
                    total_sum += img[new_i][new_j]
                    total_length += 1
            total_sum += img[i][j]
            total_length += 1
            return total_sum,total_length

        #construct the matrix
        for i in range(row_length):
            for j in range(col_length):
                total_sum,total_length = evaluate(i,j)
                res[i][j] = total_sum//total_length
        
        return res