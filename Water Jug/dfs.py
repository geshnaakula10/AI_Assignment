import time
from water_jug import is_goal, get_successors


def dfs(initial_state):
    """
    Depth First Search (Iterative using Stack)
    Returns solution path, nodes expanded, and time taken.
    """

    start_time = time.time()

    stack = [(initial_state, [])]
    visited = set()
    nodes_expanded = 0

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)
        nodes_expanded += 1

        if is_goal(state):
            end_time = time.time()
            return {
                "solution": path + [state],
                "nodes_expanded": nodes_expanded,
                "time": end_time - start_time
            }

        for successor in get_successors(state):
            if successor not in visited:
                stack.append((successor, path + [state]))

    return None