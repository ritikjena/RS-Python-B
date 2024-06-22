def count_frequencies(lst):
    frequency_dict = {}
    for elem in lst:
        if elem in frequency_dict:
            frequency_dict[elem] += 1
        else:
            frequency_dict[elem] = 1
    return frequency_dict

string1 = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6]
result = count_frequencies(string1)
print(result)
