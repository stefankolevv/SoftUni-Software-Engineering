def sum_matrix_columns(matrix):
    transposed_matrix = list(map(list, zip(*matrix)))

    for col_sum in map(sum, transposed_matrix):
        print(col_sum)

def main():
    rows, columns = map(int, input().split(', '))
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    sum_matrix_columns(matrix)

if __name__ == "__main__":
    main()