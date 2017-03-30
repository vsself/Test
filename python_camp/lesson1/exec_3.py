"""
draw diamond graph with given row number
example:
1. input row number 3 the graph should be as follow
 *
* *
 *
2. if can not draw the graph completely, return False
"""
from string import strip


def draw_diamond_graph(row):
    if row % 2 == 0:
        return False
    else:
        med = (row-1)/2
        str1 = ''
        for i in range(row):
            str1 = str1 + abs(med - i)*' ' + ((abs(med - abs(med - i)) + 1)*'* ').strip() + '\n'
        str1 = str1[0:-1]
        return str1



