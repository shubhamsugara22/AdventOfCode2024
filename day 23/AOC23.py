# from collections import defaultdict

# # Step 1: Read connections from file
# with open('Lan.txt', 'r') as file:
#     connections = [line.strip() for line in file if line.strip()]

# # Step 2: Build the graph as an adjacency list
# graph = defaultdict(set)
# for connection in connections:
#     a, b = connection.split("-")
#     graph[a].add(b)
#     graph[b].add(a)

# # Step 3: Find all triangles
# triangles = set()
# for node in graph:
#     neighbors = graph[node]
#     for neighbor in neighbors:
#         # Find common neighbors between `node` and `neighbor`
#         common_neighbors = neighbors & graph[neighbor]
#         for common in common_neighbors:
#             # A triangle is formed by (node, neighbor, common)
#             triangle = tuple(sorted([node, neighbor, common]))
#             triangles.add(triangle)

# # Step 4: Filter triangles where at least one name starts with 't'
# filtered_triangles = [triangle for triangle in triangles if any(comp[0] == 't' for comp in triangle)]

# # Step 5: Output the result
# print("Total triangles with at least one computer starting with 't':", len(filtered_triangles))
# print("Triangles:", filtered_triangles)


#############################################################

from collections import defaultdict

# Step 1: Read connections from file
with open('Lan.txt', 'r') as file:
    connections = [line.strip() for line in file if line.strip()]

# Step 2: Build the graph as an adjacency list
graph = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

# Step 3: Find the largest clique (fully connected set)
def find_largest_clique(graph):
    def is_clique(nodes):
        return all(b in graph[a] for a in nodes for b in nodes if a != b)

    largest_clique = set()
    nodes = list(graph.keys())

    # Check all subsets of nodes for being a clique
    from itertools import combinations
    for size in range(len(nodes), 0, -1):
        for subset in combinations(nodes, size):
            if is_clique(subset):
                return set(subset)
    return largest_clique

largest_clique = find_largest_clique(graph)

# Step 4: Generate the password
password = ",".join(sorted(largest_clique))

# Step 5: Output the result
print("Largest clique size:", len(largest_clique))
print("Password to the LAN party:", password)

