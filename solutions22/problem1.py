processes = list()
time_by_process = dict()

with open('./data/22data/22-1.csv', encoding='utf-8') as f:
    for line in f.readlines()[1:]:
        process, time, dependent = line.split(',')
        process = int(process)
        time = int(time)
        dependent = [int(item) for item in dependent.split(';')]

        if dependent == [0]:
            dependent = 0
            processes.append((process, time, dependent))
        else:
            processes.append((process, time, dependent))

processes.sort(key = lambda item: (item[0], item[1], item[2]))
for item in processes:
    if item[2] == 0:
        time_by_process[item[0]] = item[1]
    else:
        time_by_process[item[0]] = item[1] + max([time_by_process[x] for x in item[2]])

print(max(time_by_process.values()))