def sum_and_print_matrix(matrix):
    total_sum = sum(sum(row) for row in matrix)
    print(total_sum)
    print(matrix)

def main():
    rows, columns = map(int, input().split(', '))
    matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
    sum_and_print_matrix(matrix)

if __name__ == "__main__":
    main()
