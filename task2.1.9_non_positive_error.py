class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, p_object):
        if p_object > 0:
            super(PositiveList, self).append(p_object)
        else:
            raise NonPositiveError

list = PositiveList()

try:
    list.append(2)
    list.append(1)
    list.append(-1)
    list.append(12)
except NonPositiveError:
    print('Non positive number')

print(list)
