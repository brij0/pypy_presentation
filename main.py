import time

"""
This function performs matrix multiplication on two square matrices A and B.
It assumes that both matrices are of the same size.
The result is a new matrix where each element is the dot product of the corresponding row of A and column of B.
"""
def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

"""
This function generates a fixed n x n matrix where each element is a sequential integer starting from 1.
For example, for n=3, the matrix would be:
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
"""
def generate_fixed_matrix(n):
    matrix = []
    for i in range(n):
        row = [j + 1 + i * n for j in range(n)]
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    n = 300

    A = generate_fixed_matrix(n)
    B = generate_fixed_matrix(n)

    start_time = time.time()

    result = matrix_multiply(A, B)

    end_time = time.time()

    print("\nResulting Matrix after multiplication (first 3 elements of first 3 rows):")
    for row in result[:3]:
        print("[", end="")
        for i in row[:3]:
            print(f"{i}, ", end="")
        print(".....],")

    print(f"\nTime taken for matrix multiplication: {end_time - start_time:.5f} seconds")
