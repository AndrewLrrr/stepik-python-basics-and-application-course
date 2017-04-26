with open('task2.4.4/dataset.txt') as f, open('task2.4.4/out.txt', 'w') as o:
    res = []
    for line in f:
        res.append(line.strip())
    o.write("\n".join(res[::-1]))
