def max_closed_substring_length(line):
    result = 0
    nearest_position = dict()

    for i in range(len(line)):
        if line[i] in nearest_position.keys():
            result = max(result, i-nearest_position[line[i]])
            
        nearest_position[line[i]] = i
    
    return result

def count_closed_substrings(line):
    result = 0
    nearest_position = dict()

    for i in range(len(line)):
        if line[i] in nearest_position.keys():
            if nearest_position[line[i]] != i-1:
                result += 1

        nearest_position[line[i]] = i
        # else:
        #     result += 1

    return result

max_distance = 0
closed_substrings = 0

with open('./data/24data/24-174.txt') as f:
    for line in f.readlines():
        if line.count('R') < 30:
            closed_substrings += count_closed_substrings(line)
            max_distance = max(max_distance, max_closed_substring_length(line))

print(max_distance, closed_substrings)