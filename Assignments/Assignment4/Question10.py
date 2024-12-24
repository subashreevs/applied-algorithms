import heapq  # Import heapq for priority queue functionality
from collections import Counter  # Import Counter to count character frequencies

class Huffman:
    def __init__(self):
        # Initialize dictionary to store Huffman codes and a variable to store the source string
        self.huffman_codes = {}  # Dictionary to store generated Huffman codes for each character
        self.source_string_to_encode = ""  # Variable to store the input string

    def set_source_string(self, src_str: str):
        # Method to set the source string for encoding
        self.source_string_to_encode = src_str

    def generate_codes(self):
        # Ensure that the huffman_codes_dict is reset each time we generate codes
        self.huffman_codes = {}

        # Count the frequency of each character in the source string
        character_frequency_counter = Counter(self.source_string_to_encode)
        
        # Create a heap with elements as [frequency, character] for each unique character
        frequency_heap = [[character_frequency_counter[character], character] for character in character_frequency_counter]
        heapq.heapify(frequency_heap)  # Convert list to a heap

        # Build the Huffman tree
        while len(frequency_heap) > 1:
            # Pop two nodes with the lowest frequency
            lowest_frequency_node = heapq.heappop(frequency_heap)
            second_lowest_frequency_node = heapq.heappop(frequency_heap)
            
            # Assign '0' and '1' to the left and right branches respectively
            for character in lowest_frequency_node[1:]:
                self.huffman_codes[character] = '0' + self.huffman_codes.get(character, '')
            for character in second_lowest_frequency_node[1:]:
                self.huffman_codes[character] = '1' + self.huffman_codes.get(character, '')
            
            # Push the combined node back into the heap with summed frequency
            combined_frequency_node = [lowest_frequency_node[0] + second_lowest_frequency_node[0]] + \
                                      lowest_frequency_node[1:] + second_lowest_frequency_node[1:]
            heapq.heappush(frequency_heap, combined_frequency_node)

    def encode_message(self, message_to_encode: str) -> str:
        # Check if codes have been generated, raise an error if not
        if not self.huffman_codes:
            raise ValueError("Huffman codes have not been generated. Call generate_codes() first.")

        # Encode a message using the generated Huffman codes
        return ''.join(self.huffman_codes[char] for char in message_to_encode)

    def decode_message(self, encoded_msg: str) -> str:
        # Check if codes have been generated, raise an error if not
        if not self.huffman_codes:
            raise ValueError("Huffman codes have not been generated. Call generate_codes() first.")

        # Reverse the Huffman codes to map encoded strings back to characters
        reverse_huffman_codes = {code: char for char, code in self.huffman_codes.items()}
        
        decoded_message = ""  # Variable to store the decoded message
        current_code = ""  # Temporary variable to accumulate bits

        # Process each bit in the encoded message
        for bit in encoded_msg:
            current_code += bit  # Append the bit to the current code
            # If the accumulated bits form a valid code, decode it
            if current_code in reverse_huffman_codes:
                decoded_message += reverse_huffman_codes[current_code]  # Append the decoded character
                current_code = ""  # Reset current code for the next character

        return decoded_message  # Return the fully decoded message

# # Example usage
# huffman = Huffman()
# huffman.set_source_string("cbadeeee")
# huffman.generate_codes()
# print(huffman.huffman_codes)  # Expected Output: {'a': '000', 'b': '001', 'c': '010', 'd': '011', 'e': '1'}
# print(huffman.encode_message("ae"))  # Expected Output: "0001"
# print(huffman.decode_message("0100011011"))  # Expected Output: "cbed"