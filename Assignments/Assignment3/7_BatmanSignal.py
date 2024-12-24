def batmanSignal(length: int):
    result_list = []  # Initialize a list to store the results

    def backtrack(current_signal):
        # Check if the current signal length equals the desired length
        if len(current_signal) == length:
            result_list.append(current_signal)  # Add the current signal to results
            return
        
        # If the current signal is empty or ends with 'x', we can add 'y'
        if not current_signal or current_signal[-1] == 'x':
            backtrack(current_signal + 'y')  # Add 'y' to the current signal
        
        # If the current signal is empty or ends with 'y' or 'x', we can add 'x'
        if not current_signal or current_signal[-1] == 'y' or current_signal[-1] == 'x':
            backtrack(current_signal + 'x')  # Add 'x' to the current signal

    backtrack("")  # Start backtracking with an empty signal
    
    return result_list  # Return the list of results

# Test Cases
# print(batmanSignal(3))  # Output: ['yxy', 'yxx', 'xyx', 'xxy', 'xxx']
# print(batmanSignal(1))  # Output: ['x', 'y']
