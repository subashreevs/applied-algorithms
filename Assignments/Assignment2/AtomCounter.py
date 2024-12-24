from collections import defaultdict

def atom_counter(formula: str) -> str:
    stack = []  # Stack to handle nested parentheses
    counts = defaultdict(int)  # Dictionary to count atoms
    i = 0  # Index to traverse the formula

    while i < len(formula):
        char = formula[i]

        if char == '(':  # Start of a new group
            stack.append(counts.copy())  # Save current counts on stack
            counts.clear()  # Clear current counts for the new group
            i += 1  # Move to the next character

        elif char == ')':  # End of a group
            i += 1  # Move past ')'
            multiplier = 0  # Initialize multiplier
            
            # Read any digits following ')'
            while i < len(formula) and formula[i].isdigit():
                multiplier = multiplier * 10 + int(formula[i])
                i += 1
            
            # Default multiplier is 1 if none specified
            if multiplier == 0:
                multiplier = 1
            
            # Multiply the current counts by the multiplier
            for atom in counts:
                counts[atom] *= multiplier
            
            # Add previous counts from the stack
            if stack:
                previous_counts = stack.pop()
                for atom in previous_counts:
                    counts[atom] += previous_counts[atom]

        else:  # An atom is found
            # Read the atom name
            j = i
            while j < len(formula) and formula[j].isalpha():
                j += 1
            
            # Atom name logic: if the current char is uppercase
            # and the next one is lowercase, it's part of the same atom.
            atom = char  # Start with the current character
            i += 1  # Move to the next character
            
            # If the next character is lowercase, include it in the atom name
            if i < len(formula) and formula[i].islower():
                atom += formula[i]
                i += 1  # Move past the lowercase letter
            
            # Read any digits following the atom to get its count
            count = 0
            while i < len(formula) and formula[i].isdigit():
                count = count * 10 + int(formula[i])
                i += 1
            
            # Default count is 1 if no digits found
            if count == 0:
                count = 1
            
            # Update the count of the atom
            counts[atom] += count

    # Construct the result string from counts
    result = []
    for atom in sorted(counts):  # Sort atom names alphabetically
        result.append(atom)  # Add atom name
        if counts[atom] > 1:  # Add count if greater than 1
            result.append(str(counts[atom]))

    return ''.join(result)  # Join and return the final result string

# Example usage:
print(atom_counter("H2O"))             # Output: "H2O"
print(atom_counter("Mg(OH)2"))         # Output: "H2MgO2"
print(atom_counter("K4(ON(SO3)2)2"))   # Output: "K4N2O14S4"
print(atom_counter("C6H12O6"))         # Output: "C6H12O6"
print(atom_counter("Fe2O3"))           # Output: "Fe2O3"
