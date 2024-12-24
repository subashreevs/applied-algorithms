from collections import Counter  # Import Counter to count character frequencies

def frequencySort(input_string: str) -> str:
    # Count the frequency of each character in the input string
    character_frequency_counter = Counter(input_string)
    
    # Sort characters by frequency in descending order, and then by ASCII value in ascending order
    sorted_characters_by_frequency = sorted(character_frequency_counter.items(), key=lambda item: (-item[1], item[0]))
    
    # Build the result string by repeating each character according to its frequency
    sorted_frequency_string = ''.join(character * frequency for character, frequency in sorted_characters_by_frequency)
    
    # Return the final sorted string based on frequency
    return sorted_frequency_string

# # Example usage
# example_string_1 = "tree"
# print(frequencySort(example_string_1))  # Expected output: "eert"

# example_string_2 = "cccaaa"
# print(frequencySort(example_string_2))  # Expected output: "aaaccc"

# example_string_3 = "Aabb"
# print(frequencySort(example_string_3))  # Expected output: "bbAa"
