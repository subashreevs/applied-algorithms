def combine_signals(signals):
    combined_signal_strength = []
    for i in range(len(signals)-1):
        combined_signal_strength.append(signals[i]|signals[i+1])
    return combined_signal_strength

#combine_signals([5,4,9,11])