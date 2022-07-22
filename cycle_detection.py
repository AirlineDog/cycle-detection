import math
import argparse


def f(y):
    return seq[y]


def purge(table, b):
    i = 0
    while i < len(table):
        if table[i][1] % b != 0:
            table.pop(i)
        else:
            i += 1


def search_table_y(table, y):
    for value in table:
        if value[0] == y:
            return value[1]
    return -1


def search_table_j(table, j):
    for value in table:
        if value[1] == j:
            return value[0]


def detect_cycle(x, f, b, g, max_size):
    y = x
    i = 0
    m = 0
    while True:
        if i % b == 0 and m == max_size:
            b *= 2
            purge(table, b)
            m = math.floor(m / 2)
        if i % b == 0:
            table.append((y, i))
            m += 1
        y = f(y)
        i += 1
        if (i % (b*g)) < b:
            j = search_table_y(table, y)
            if j != -1:
                return y, i, j, b


def recover_cycle(f, y, i, j):
    c = 1
    found_c = False
    y_c = y
    while c <= (g + 1) * b and not found_c:
        y_c = f(y_c)
        if y == y_c:
            found_c = True
        else:
            c += 1
    if not found_c:
        c = i - j
    block_length = g * b
    final_block = block_length * math.floor(i / block_length)
    previous_block = final_block - block_length
    ii = max(c, previous_block)
    jj = ii - c
    leader = jj + 1
    while find_f_to_the_nth(leader) != find_f_to_the_nth(leader + c):
        leader += 1
    return leader, c


def find_f_to_the_nth(n):
    kb = search_table_j(table, b * math.floor(n / b))
    more = n % b
    for i in range(more):
        kb = f(kb)
    return kb


def make_sequence_dict(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        d = {}
        first = int(lines[0].strip())
        for i in range(len(lines) - 1):
            if int(lines[i].strip()) in d:
                break
            d[int(lines[i].strip())] = int(lines[i + 1].strip())
    return d, first


# Handle arguments
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-t', action='store_const', const=True, help="Print table contents")
my_parser.add_argument('b')
my_parser.add_argument('g')
my_parser.add_argument('table_size')
my_parser.add_argument('sequence_file')
args = my_parser.parse_args()

b = int(args.b)
g = int(args.g)
max_size = int(args.table_size)
table = []
seq, start_number = make_sequence_dict(args.sequence_file)
y, i, j, b = detect_cycle(start_number, f, b, g, max_size)
l, c = recover_cycle(f, y, i, j)
print("cycle", c, "leader", l)
if args.t:
    table.sort()
    for value in table:
        print(*value)
