# -*- coding: utf-8 -*-


def read_csv(filename):
    # read csv
    csv = open(filename, 'r')
    samples = []
    # filter 编号
    categories = csv.readline().replace('\n', '').split(',')[1:]
    for v in csv.readlines():
        # filter 编号
        samples.append(v.replace('\n', '').split(',')[1:])
    return categories, samples


def divide_two_parts(set, parameter, value):
    pass
