
import heapq

GOAL = (1,2,3,8,0,4,7,6,5)


def misplaced_tiles(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != GOAL[i]
    )


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors


def astar(start):
    pq = [(misplaced_tiles(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if new_g < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_g
                parent[neighbor] = current
                h = misplaced_tiles(neighbor)
                heapq.heappush(pq, (new_g + h, new_g, neighbor))

    return None


def display(path):
    if path is None:
        print("No solution exists")
        return

    print("Number of moves:", len(path) - 1)

    for step, state in enumerate(path):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i + 3])


start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

print("A* using Misplaced Tiles Heuristic")
display(astar(start))
