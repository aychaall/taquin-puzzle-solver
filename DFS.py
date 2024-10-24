class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return f"{self.state}"

def dfs_real_time(initial_state, goal_state):
    frontier = [Node(initial_state, None, None)]  # Stack for DFS
    explored = set()
    actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    frontier_set = {initial_state}  # Set to keep track of nodes in the frontier
    solution = set()

    while frontier:
        node = frontier.pop()  # DFS uses last-in, first-out (LIFO)
        frontier_set.remove(node.state)
        explored.add(node.state)

        if node.state == goal_state:
            # If the goal is found, reconstruct the path by following parent links
            path = []
            while node.parent is not None:
                path.append(node.action)
                node = node.parent
                solution.add(node.state)
            path.reverse()  # Reverse to get the correct order of actions
            return path, solution

        # Expand the node
        for action in actions:
            child_state = get_child(node.state, action)

            if child_state is not None and child_state not in explored and child_state not in frontier_set:
                child_node = Node(child_state, node, action)
                frontier.append(child_node)
                frontier_set.add(child_state)

    return None, solution

def get_child(state, action):
    index = state.index(0)  # Find the position of the empty tile (0)

    if action == 'UP' and index >= 3:
        new_state = list(state)
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        return tuple(new_state)

    if action == 'DOWN' and index <= 5:
        new_state = list(state)
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        return tuple(new_state)

    if action == 'LEFT' and index % 3 != 0:
        new_state = list(state)
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        return tuple(new_state)

    if action == 'RIGHT' and index % 3 != 2:
        new_state = list(state)
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        return tuple(new_state)

    return None
def print_puzzle(state):
    print("{")
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print("}")
# Example usage:
#initial_state = (1, 3, 2, 6, 7, 4, 0, 8, 5)
#goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
#path, solution = dfs_real_time(initial_state, goal_state)

# Output only the solution path
#print("Number of explored states:", len(solution))
#print("Length of solution path:", len(path))
