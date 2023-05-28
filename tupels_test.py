file_name = 'tf.txt'

counts = dict()

with open(file_name) as fh:
    for line in fh:
        if not line.startswith('From '):
            continue

        words = line.split()
        time = words[5]
        hour = time[:2]

        counts[hour] = counts.get(hour,0) + 1

sorted_list = sorted([(k,v) for k,v in counts.items()])

for key,val in sorted_list:
    print(key,val)