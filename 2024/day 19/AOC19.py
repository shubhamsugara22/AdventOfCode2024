# def count_possible_designs_from_file(filename):
#     # Read the input file
#     with open(filename, 'r') as file:
#         lines = file.read().strip().split("\n")
    
#     # Split towel patterns and designs
#     towel_patterns = lines[0].split(", ")
#     designs = lines[2:]  # Designs start after the blank line
    
#     # Convert towel patterns into a set for quick lookup
#     patterns = set(towel_patterns)

#     def can_form_design(design, memo={}):
#         # If already checked this design, return cached result
#         if design in memo:
#             return memo[design]
        
#         # If the design is empty, it can be formed
#         if not design:
#             return True
        
#         # Try to match the design with available patterns
#         for pattern in patterns:
#             if design.startswith(pattern):
#                 remaining_design = design[len(pattern):]
#                 if can_form_design(remaining_design, memo):
#                     memo[design] = True
#                     return True
        
#         # If no pattern matches, it's not possible
#         memo[design] = False
#         return False
    
#     # Count designs that can be formed
#     possible_count = sum(can_form_design(design) for design in designs)
#     return possible_count

# # Example usage
# filename = "tshirt.txt"
# possible_designs = count_possible_designs_from_file(filename)
# print(f"Number of possible designs: {possible_designs}")


def count_combinations_from_file(filename):
    # Read the input file
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Split towel patterns and designs
    towel_patterns = lines[0].split(", ")
    designs = lines[2:]  # Designs start after the blank line
    
    # Convert towel patterns into a set for quick lookup
    patterns = set(towel_patterns)

    def count_ways_to_form(design, memo={}):
        # If already calculated for this design, return the cached result
        if design in memo:
            return memo[design]
        
        # If the design is empty, there is exactly one way to form it (do nothing)
        if not design:
            return 1
        
        # Initialize the count of ways
        ways = 0
        
        # Try matching the design with each pattern
        for pattern in patterns:
            if design.startswith(pattern):
                remaining_design = design[len(pattern):]
                # Recursively count ways for the remaining part
                ways += count_ways_to_form(remaining_design, memo)
        
        # Cache the result
        memo[design] = ways
        return ways
    
    # Calculate the total number of ways for all designs
    total_combinations = sum(count_ways_to_form(design) for design in designs)
    return total_combinations

# Example usage
filename = "tshirt.txt"  
total_combinations = count_combinations_from_file(filename)
print(f"Total number of combinations: {total_combinations}")
