def get_parents(child, classes):
    parents = set()

    def find_parents(child):
        if child not in classes:
            return
        for cls in classes[child]:
            parents.add(cls)
            find_parents(cls)
        return

    find_parents(child)
    return parents

classes = {}
exceptions = []

for i in range(int(input())):
    inp = input()
    if ':' in inp:
        exception, parents = [e.strip() for e in inp.split(':')]
        if exception not in classes:
            classes[exception] = set()
        for parent in parents.split():
            classes[exception].add(parent)
    else:
        exception = inp.strip()
        if exception not in classes:
            classes[exception] = set()

for j in range(int(input())):
    exception = input().strip()
    parents = get_parents(exception, classes)
    for parent in parents:
        if parent in exceptions:
            print(exception)
            break
    exceptions.append(exception)
