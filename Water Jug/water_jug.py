# Jug capacities
JUG1_CAPACITY = 4
JUG2_CAPACITY = 3
GOAL_AMOUNT = 2


def is_goal(state):
    """
    Goal is achieved if either jug contains GOAL_AMOUNT.
    """
    x, y = state
    return x == GOAL_AMOUNT or y == GOAL_AMOUNT


def get_successors(state):
    """
    Returns all possible successor states from the current state.
    """
    x, y = state
    successors = []

    # Fill Jug1
    successors.append((JUG1_CAPACITY, y))

    # Fill Jug2
    successors.append((x, JUG2_CAPACITY))

    # Empty Jug1
    successors.append((0, y))

    # Empty Jug2
    successors.append((x, 0))

    # Pour Jug1 -> Jug2
    transfer = min(x, JUG2_CAPACITY - y)
    successors.append((x - transfer, y + transfer))

    # Pour Jug2 -> Jug1
    transfer = min(y, JUG1_CAPACITY - x)
    successors.append((x + transfer, y - transfer))

    return successors