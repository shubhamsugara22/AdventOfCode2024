def count_possible_designs_from_file(filename):
    # Read the input file
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Split towel patterns and designs
    towel_patterns = lines[0].split(", ")
    designs = lines[2:]  # Designs start after the blank line
    
    # Convert towel patterns into a set for quick lookup
    patterns = set(towel_patterns)

    def can_form_design(design, memo={}):
        # If already checked this design, return cached result
        if design in memo:
            return memo[design]
        
        # If the design is empty, it can be formed
        if not design:
            return True
        
        # Try to match the design with available patterns
        for pattern in patterns:
            if design.startswith(pattern):
                remaining_design = design[len(pattern):]
                if can_form_design(remaining_design, memo):
                    memo[design] = True
                    return True
        
        # If no pattern matches, it's not possible
        memo[design] = False
        return False
    
    # Count designs that can be formed
    possible_count = sum(can_form_design(design) for design in designs)
    return possible_count

# Example usage
filename = "tshirt.txt"
possible_designs = count_possible_designs_from_file(filename)
print(f"Number of possible designs: {possible_designs}")
