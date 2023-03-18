processes = dict()
total_duration = dict()

mode2 = 0
with open('./data/22data/22-6.csv', encoding='utf-8') as f:
    for line in f.readlines()[1:]:
        process_id, time, dependent = line.split(',')
        process_id = int(process_id)
        time = int(time)
        dependent = [int(item) for item in dependent.split(';')]

        if dependent == [0]:
            total_duration[process_id] = time
        else:
            processes[process_id] = (time, dependent)
        mode2 = max(mode2, time)

while processes:
    ids = list(processes.keys())
    for pid in ids:
        time, dependent = processes[pid]
        if all(item in total_duration for item in dependent):
            total_duration[pid] = max(total_duration[item] for item in dependent) + time
            del processes[pid]

mode1 = max(total_duration.values())

print(mode1 - mode2)