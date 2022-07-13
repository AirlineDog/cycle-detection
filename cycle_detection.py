b = 3
g = 2
max_size = 3
table = []

file = open("seq_1.txt", "r")


def f(y):
    line = file.readline()
    if line == "":
        return
    return int(line)


def purge(table, b):
    i = 0
    while i < len(table):
        if table[i][1] % b != 0:
            table.pop(i)
        else:
            i += 1


def search_table(table, y):
    for value in table:
        if value[0] == y:
            return value[1]
    return -1


def detect_cycle(x, f, b, g, max_size):
    y = x
    i = 0
    m = 0
    while True:
        if i % b == 0 and m == max_size:
            b *= 2
            purge(table, b)
            m = int(m / 2)
        if i % b == 0:
            table.append((y, i))
            m += 1
        y = f(y)
        i += 1
        if (i % (b*g)) < b:
            j = search_table(table, y)
            if j != -1:
                return y, i, j


print(detect_cycle(f(0), f, b, g, max_size))
