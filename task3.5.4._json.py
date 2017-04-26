import json

str_json = input()
data_json = json.loads(str_json)
classes = {}

for data in data_json:
    if data['name'] not in classes:
        classes[data['name']] = set()

for data in data_json:
    for parent in data['parents']:
        if parent in classes:
            classes[parent].add(data['name'])


def count_children(graph, name):
    buffer = set()

    def recursive_search(key):
        nonlocal graph
        nonlocal buffer
        for cld in graph[key]:
            if cld not in buffer:
                buffer.add(cld)
            if cld in graph:
                recursive_search(cld)
    recursive_search(name)

    return len(buffer)

for key, children in sorted(classes.items()):
    print('{0} : {1}'.format(key, (count_children(classes.copy(), key) + 1)))
