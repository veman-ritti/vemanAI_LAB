
def calculate_h(state):
    n = len(state)
    h = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Rows are i+1 and j+1; values give columns
            if abs(state[i] - state[j]) == abs(i - j):
                h += 1

    return h


def print_board(state):
    n = len(state)

    for row in range(n):
        for col in range(n):
            if state[row] == col + 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def hill_climbing(state):
    n = len(state)
    step = 0

    print("Initial state:", state)
    print("Initial h =", calculate_h(state))

    while calculate_h(state) > 0:
        current_h = calculate_h(state)
        best_state = None
        best_h = current_h
        best_swap = None

        # Swap the column positions of queens in two rows
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = state.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

                h = calculate_h(neighbor)

                print(
                    f"Swap rows {i+1} and {j+1}: "
                    f"{neighbor}, h = {h}"
                )

                if h < best_h:
                    best_h = h
                    best_state = neighbor
                    best_swap = (i + 1, j + 1)

        if best_state is None:
            print("Local optimum reached; no improving swap.")
            return

        state = best_state
        step += 1

        print(f"Step {step}: Selected swap rows {best_swap}")
        print("New state:", state)
        print("New h =", best_h)
        print()

    print("Solution found!")
    print("Final state:", state)
    print("Final h =", calculate_h(state))
    print("Final board:")
    print_board(state)


n = int(input("Enter N: "))

if n < 1:
    print("N must be positive.")
elif n == 2 or n == 3:
    print("No solution exists for N =", n)
else:
    if n == 4:
        initial_state = [1, 3, 2, 4]
    else:
        initial_state = list(range(1, n + 1))

    hill_climbing(initial_state)
