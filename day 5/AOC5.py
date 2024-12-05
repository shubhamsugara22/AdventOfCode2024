from collections import defaultdict, deque

def parse_input_file(file_path):
    """Parse input from a file containing rules and updates."""
    with open(file_path, "r") as file:
        input_data = file.read()

    rules_section, updates_section = input_data.strip().split("\n\n")

    # Parse ordering rules
    rules = []
    for line in rules_section.strip().split("\n"):
        X, Y = map(int, line.split("|"))
        rules.append((X, Y))

    # Parse updates
    updates = []
    for line in updates_section.strip().split("\n"):
        updates.append(list(map(int, line.split(","))))

    return rules, updates

def build_graph(rules, pages):
    """Build a directed graph from the rules relevant to the given pages."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Add edges only for the relevant pages
    for X, Y in rules:
        if X in pages and Y in pages:
            graph[X].append(Y)
            in_degree[Y] += 1
            if X not in in_degree:
                in_degree[X] = 0

    return graph, in_degree

def is_valid_order(update, graph, in_degree):
    """Check if the given update is a valid topological order."""
    # Perform topological sort using Kahn's algorithm
    in_degree_copy = in_degree.copy()
    queue = deque([node for node in update if in_degree_copy[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree_copy[neighbor] -= 1
            if in_degree_copy[neighbor] == 0:
                queue.append(neighbor)

    # Check if sorted_order matches the update sequence
    return sorted_order == update

def correct_order(update, graph, in_degree):
    """Generate the correct order of pages based on topological sorting."""
    in_degree_copy = in_degree.copy()
    queue = deque([node for node in update if in_degree_copy[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree_copy[neighbor] -= 1
            if in_degree_copy[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def find_middle(page_list):
    """Find the middle page in a list of pages."""
    return page_list[len(page_list) // 2]

def solve_puzzle_from_file(file_path):
    """Solve the puzzle using input from a file."""
    rules, updates = parse_input_file(file_path)
    total_middle_sum_valid = 0
    total_middle_sum_corrected = 0

    for update in updates:
        # Build a graph for the current update
        graph, in_degree = build_graph(rules, set(update))

        # Check if the update is valid
        if is_valid_order(update, graph, in_degree):
            # Add the middle page to the total sum of valid updates
            total_middle_sum_valid += find_middle(update)
        else:
            # Correct the order and add the middle page to the total sum of corrected updates
            corrected_update = correct_order(update, graph, in_degree)
            total_middle_sum_corrected += find_middle(corrected_update)

    return total_middle_sum_valid, total_middle_sum_corrected

# Example usage
file_path = "rules.txt"
valid_sum, corrected_sum = solve_puzzle_from_file(file_path)
print("Sum of middle pages from correctly ordered updates:", valid_sum)
print("Sum of middle pages after correcting invalid updates:", corrected_sum)
