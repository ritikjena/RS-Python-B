def char_frequency(s):
    
    s = s.replace(" ", "")
    
    
    frequency = {}
    
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    
    sorted_chars = sorted(frequency.keys(), key=lambda x: (x.islower(), x))
    
    
    for char in sorted_chars:
        print(f"{char}-> {frequency[char]}")


input_str = "Robotics Society"

char_frequency(input_str)
