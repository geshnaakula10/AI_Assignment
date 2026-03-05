# main.py

from bfs import bfs
from dfs import dfs


def print_result(name, result):
    print(f"\n===== {name} =====")
    if result:
        print("Solution Path:", result["solution"])
        print("Number of Steps:", len(result["solution"]) - 1)
        print("Nodes Expanded:", result["nodes_expanded"])
        print("Time Taken:", result["time"], "seconds")
    else:
        print("No Solution Found")


if __name__ == "__main__":
    initial_state = (0, 0)

    # BFS
    bfs_result = bfs(initial_state)
    print_result("BFS", bfs_result)

    # DFS
    dfs_result = dfs(initial_state)
    print_result("DFS", dfs_result)