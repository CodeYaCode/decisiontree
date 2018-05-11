# -*- coding: utf-8 -*-
import CsvUtil

if __name__ == '__main__':
    categories, samples = CsvUtil.read_csv("../resources/watermelon.csv")
    for s in samples:
        if s[-1] == '是':
            print('nice')
        else:
            print(s[1])
