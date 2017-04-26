cls_count = int(input())
classes = {}


def has_parent(cld, prnt):
    is_found = False

    def inspect_parents(cld, prnt):
        nonlocal is_found
        if cld == prnt:
            is_found = True
            return
        elif cld in classes:
            for cls in classes[cld]:
                inspect_parents(cls, prnt)
    inspect_parents(cld, prnt)
    return is_found


for i in range(cls_count):
    inp = input()
    if ':' in inp:
        name, parents = [i.strip() for i in inp.split(':')]
        if name not in classes:
            classes[name] = set()
        for parent in parents.split():
            classes[name].add(parent.strip())
    elif inp not in classes:
        classes[inp] = set()

qs_count = int(input())

for i in range(qs_count):
    prnt, cld = input().split()
    if has_parent(cld, prnt):
        print('Yes')
    else:
        print('No')
