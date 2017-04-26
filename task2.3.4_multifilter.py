class MultiFilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.lst = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        i = 0
        while i < len(self.lst):
            neg = 0
            pos = 0
            for func in self.funcs:
                if func(self.lst[i]) is False:
                    neg += 1
                else:
                    pos += 1
            if self.judge(pos, neg) is True:
                yield self.lst[i]
            i += 1

        return self


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(MultiFilter(a, mul2, mul3, mul5)))
