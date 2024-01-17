import time
import random
import matplotlib.pyplot as plt

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

        for j in range(n):
            if board[i][j] == 1 and abs(i - row) == abs(j - col):
                return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return [list(row) for row in board]

    solutions = []

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            result = solve_n_queens_util(board, row + 1, n)

            if result:
                solutions.extend(result)

            board[row][col] = 0

    return solutions

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0, n)

def calculate_attacks(board, row, col, n):
    attacks = 0

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            attacks += 1

    for i, j in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            attacks += 1

    for i in range(n):
        if i != row and board[i][col] == 1:
            attacks += 1

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            attacks += 1

    for i, j in zip(range(row + 1, n), range(col + 1, n)):
        if board[i][j] == 1:
            attacks += 1

    return attacks

def hill_climbing_n_queens(n, max_iterations=1000):
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        j = random.randint(0, n - 1)
        board[i][j] = 1

    current_attacks = sum(calculate_attacks(board, row, col, n) for row, col in enumerate(range(n)))

    for iteration in range(max_iterations):
        if current_attacks == 0:
            break

        min_attacks = float('inf')
        move = None

        for row in range(n):
            for col in range(n):
                if board[row][col] == 1:
                    continue

                board[row][col] = 1
                new_attacks = sum(calculate_attacks(board, r, c, n) for r, c in enumerate(range(n)))
                board[row][col] = 0

                if new_attacks < min_attacks:
                    min_attacks = new_attacks
                    move = (row, col)
        if move is None:
          return board
        board[move[0]][move[1]] = 1
        current_attacks = min_attacks

def compare_runtimes(max_queens=15):
    backtracking_times = []
    hill_climbing_times = []

    for n in range(1, max_queens + 1):
        # Medición de tiempo para backtracking
        start_time_backtracking = time.time()
        solve_n_queens(n)
        end_time_backtracking = time.time()
        backtracking_times.append(end_time_backtracking - start_time_backtracking)

        # Medición de tiempo para búsqueda local
        start_time_hill_climbing = time.time()
        hill_climbing_n_queens(n)
        end_time_hill_climbing = time.time()
        hill_climbing_times.append(end_time_hill_climbing - start_time_hill_climbing)

    # Graficar los resultados
    plt.plot(range(1, max_queens + 1), backtracking_times, label='Backtracking')
    plt.plot(range(1, max_queens + 1), hill_climbing_times, label='Búsqueda Local (Hill Climbing)')
    plt.xlabel('Número de reinas')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.legend()
    plt.show()

# Llamada a la función para graficar
compare_runtimes(max_queens=10)
