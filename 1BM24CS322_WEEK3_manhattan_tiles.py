
import heapq

GOAL = (1,2,3,8,0,4,7,6,5)
def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            row, col = divmod(i, 3)
            goal_row, goal_col = divmod(tile - 1, 3)

            distance += abs(row - goal_row)
            distance += abs(col - goal_col)

    return distance
def neighbors(state):
    result = []
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
            result.append(tuple(new_state))

    return result
def astar(start):
    pq = [(heuristic(start), 0, start)]
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

        for nxt in neighbors(current):
            new_g = g + 1

            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = current
                h = heuristic(nxt)
                heapq.heappush(pq, (new_g + h, new_g, nxt))

    return None


def display(path):
    if path is None:
        print("No solution exists")
        return

    print("Step | g(n) | h(n) | f(n)")
    print("-" * 30)

    for step, state in enumerate(path):
        g = step
        h = heuristic(state)
        f = g + h

        print(f"{step:4} | {g:4} | {h:4} | {f:4}")
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()
start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)
path = astar(start)
display(path)
