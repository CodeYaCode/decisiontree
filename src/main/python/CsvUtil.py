# -*- coding: utf-8 -*-


def read_csv(filename):
    # read csv
    csv = open(filename, 'r')
    result = {}
    values = []
    titles = csv.readline().replace('\n', '').split(',')[1:]
    for v in csv.readlines():
        values.append(v.replace('\n', '').split(','))
    for i, t in enumerate(titles):
        result[t] = []
        for v in values:
            result[t].append(v[i+1])
    return result
