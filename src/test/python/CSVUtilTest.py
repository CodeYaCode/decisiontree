# -*- coding: utf-8 -*-
import CsvUtil

if __name__ == '__main__':
    result_map = CsvUtil.read_csv("../resources/watermelon.csv")
    for key in result_map.keys():
        print(key)
        print(result_map[key])
    print(len(result_map))
