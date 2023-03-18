processes = dict()
total_duration = dict()

with open('./data/22data/22-26.csv', encoding='utf-8') as f:
    for line in f.readlines()[1:]:
        process_id, time, dependent = line.split(',')
        process_id = int(process_id)
        time = int(time)
        dependent = [int(item) for item in dependent.split(';')]

        if dependent == [0]:
            total_duration[process_id] = time
        else:
            processes[process_id] = (time, dependent)

while processes:
    ids = list(processes.keys())
    for pid in ids:
        time, dependent = processes[pid]
        if all(item in total_duration for item in dependent):
            total_duration[pid] = max(total_duration[item] for item in dependent) + time
            del processes[pid]

print(max(total_duration.values()))