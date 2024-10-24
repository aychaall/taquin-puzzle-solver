from collections import deque

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def __repr__(self):
        return f"{self.state}"

def bfs_real_time(initial_state, goal_state):
    frontier = deque([Node(initial_state, None, None)])  # Use deque for faster popping
    explored = set()
    actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    seen_states = {initial_state}  # Use this to avoid re-adding states to both explored and frontier
    solution=set()
    while frontier:
        node = frontier.popleft()  # Pop from the left (FIFO)
        explored.add(node.state)

        if node.state == goal_state:
            path = []
            while node.parent is not None:
                path.append(node.action)
                solution.add(node.state)
                node = node.parent
            path.reverse()
            return path, solution

        for action in actions:
            child_state = get_child(node.state, action)
            if child_state is not None and child_state not in seen_states:
                child_node = Node(child_state, node, action)
                frontier.append(child_node)
                seen_states.add(child_state)

    return None, solution

def get_child(state, action):
    index = state.index(0)  # No need to convert to list repeatedly

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
#path, explored = bfs_real_time(initial_state, goal_state)


#for state in explored:
#    print_puzzle(state)
# Output the results
#print("Number of explored states:", len(explored))
#print("Length of solution path:", len(path))



