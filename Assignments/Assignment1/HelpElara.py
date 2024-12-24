def justifyLine(line: list[str], width: int, is_last: bool) -> str:
        # If it is the last line, left-align
        if is_last or len(line) == 1:
            return ' '.join(line).ljust(width)

        # Calculate the total spaces needed and how many between words
        total_spaces = width - sum(len(word) for word in line)
        num_gaps = len(line) - 1

        even_spaces = total_spaces // num_gaps
        extra_spaces = total_spaces % num_gaps

        justified_line = ""

        for i in range(len(line) - 1):
            justified_line += line[i] + " " * (even_spaces + (1 if i < extra_spaces else 0))

        justified_line += line[-1]  # Last word without extra spaces after it

        return justified_line

def helpElara(words: list[str], width: int) -> list[str]:

    result = []
    current_line = []
    current_length = 0

    for word in words:
        # Check if the current word can fit in the current line
        if current_length + len(word) + len(current_line) > width:
            result.append(justifyLine(current_line, width, False))
            current_line = []
            current_length = 0

        # Add the word to the current line
        current_line.append(word)
        current_length += len(word)

    # Handle the last line (left-aligned)
    if current_line:
        result.append(justifyLine(current_line, width, True))

    return result

# Test cases
# print(helpElara(["To","be","or","no","question","answer","is","question"], 13))
# print(helpElara(["Hello", "world", "this", "is", "a", "test", "of", "help", "Elara"], 15))
