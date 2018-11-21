#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 2018/11/19
# version: 1.0
# python_version: 3.62
import sys

from utils import InputParser as Parser

class CARP(object):
    def __init__(self,info):
        parser = Parser(info)

        self.nodes = parser.get_node_names()#list
        self.depot = parser.get_depot()#int
        self.capacity = parser.get_capacity()#int
        self.vehicles = parser.get_vehicles()#int
        self.demands = parser.get_demands()#dict
        self.shortest_paths = parser.get_shortest_paths()#dict

    def demand(self,ele):
        return ele[3]

    def carp(self):
        capacity = self.capacity
        paths = self.shortest_paths

        # initial free list
        free = []
        for start in self.demands:
            for end in self.demands[start]:
                # start end cost demand
                free.append([start,end,self.demands[start][end][0],self.demands[start][end][1]])
        free.sort(key=self.demand)

        # find routes
        routes = []
        while len(free) !=0:
            new_route = []
            temp_capacity = 0

            # 空时 假设上一个为 首尾都是出发点的 cost,demand 都是0的 demand
            last_demand = [self.depot, self.depot, 0, 0]
            while temp_capacity < capacity:
                # 当前需求为第一个 当前距离为最大值，之后就算遍历第一个也会将距离修改过来
                temp_demand = free[0]
                temp_distance = sys.maxsize

                found = False
                for demand in free:
                    # 所有满足条件的需求
                    if demand[3] + temp_capacity <= capacity:
                        # 如果和上个需求首尾相接，直接加入
                        if demand[0] == last_demand[1]:
                            temp_capacity += demand[3]
                            new_route.append(demand)
                            last_demand = demand
                            found = True
                            break
                        # 否则遍历比较 选择距离上个需求终点最近的需求
                        elif paths[last_demand[1]][demand[0]]["distance"] < temp_distance:
                            temp_demand = demand
                            temp_distance = paths[last_demand[1]][demand[0]]["distance"]

                if not found:
                    temp_capacity += temp_demand[3]
                    new_route.append(temp_demand)
                    last_demand = temp_demand
                    found = True

                free.remove(last_demand)
                if len(free) == 0:
                    break
            routes.append(new_route)
        # find path cost along route
        cost = 0
        i = 0
        for route in routes:
            print(route)

            # deal with the first demand either start with depot or not
            if route[0][0] == self.depot:
                cost += route[0][2]
            else:
                cost += paths[self.depot][route[0][0]]["distance"]
                cost += route[0][2]

            for index in range(len(route)-1):
                this_demand = route[index]
                next_demand = route[index + 1]

                # if this_demand connect with next or not
                if this_demand[1] == next_demand[0]:
                    cost += next_demand[2]
                else:
                    cost += paths[this_demand[1]][next_demand[0]]["distance"]
                    cost += next_demand[2]

            #deal with the last one to depot
            if next_demand[1] != self.depot:
                cost += paths[next_demand[1]][self.depot]["distance"]
        print(cost)

    def __str__(self):
        demands = "\n"
        for key in self.demands:
            demands += str(key) + " : " + str(self.demands[key]) + "\n"

        shortest_paths = "\n"
        for key in self.shortest_paths:
            shortest_paths += str(key) + " : " + str(self.shortest_paths[key]) + "\n"

        return ("nodes : %s\n" +
                "depot : %d\n" +
                "capacity : %d\n" +
                "vehicles : %d\n" +
                "demands : %s\n" +
                "paths : %s\n" ) % \
               (str(self.nodes), self.depot, self.capacity, self.vehicles,
                demands, shortest_paths)


if __name__ == '__main__':
    # info = []
    # temp = input()
    #
    # while temp != "END":
    #     info.append(temp)
    #     temp = input()
    sample = \
'''NAME : sample
VERTICES : 8
DEPOT : 1
REQUIRED EDGES : 5
NON-REQUIRED EDGES : 5
VEHICLES : 2
CAPACITY : 6
TOTAL COST OF REQUIRED EDGES : 13
NODES       COST         DEMAND
1   2        4              0
2   3        2              3
3   4        3              3
1   4        4              0
4   5        7              0
5   6        2              2
6   7        3              2
7   8        3              2
1   8        1              0
1   5        3              0'''

    test = \
'''NAME : egl-e1-A
VERTICES : 77
DEPOT : 1
REQUIRED EDGES : 51
NON-REQUIRED EDGES : 47
VEHICLES : 5
CAPACITY : 305
TOTAL COST OF REQUIRED EDGES : 1468
NODES       COST         DEMAND
1   2   32       32
2   3   14       14
2   4   17       17
4   5   56       56
9   10   20       20
11   12   32       32
12   16   29       29
13   16   13       13
13   14   7       7
15   17   26       26
15   18   38       38
18   19   41       41
19   20   32       32
19   21   38       38
21   22   17       17
22   75   24       24
23   31   40       40
31   32   58       58
32   33   30       30
32   34   43       43
32   35   86       86
35   41   15       15
43   44   78       78
44   45   12       12
44   46   13       13
46   47   33       33
47   48   10       10
47   49   9       9
49   50   8       8
49   51   10       10
50   52   2       2
52   54   4       4
55   56   6       6
42   57   14       14
57   58   78       78
58   59   25       25
11   59   78       78
58   60   33       33
60   61   39       39
60   62   23       23
62   63   30       30
63   65   21       21
62   66   16       16
66   68   45       45
58   69   32       32
59   69   11       11
4   69   75       75
23   75   17       17
20   76   8       8
21   51   2       2
44   59   28       28
5   6   8       0
5   7   6       0
7   8   18       0
8   9   26       0
10   11   12       0
14   15   7       0
13   77   12       0
18   20   21       0
22   24   4       0
24   25   27       0
25   75   16       0
25   26   17       0
23   26   12       0
26   27   15       0
26   28   18       0
28   29   16       0
25   29   27       0
30   31   14       0
33   36   27       0
33   37   75       0
37   38   8       0
37   39   21       0
39   40   5       0
35   39   7       0
40   41   9       0
41   42   18       0
42   43   11       0
45   46   12       0
11   48   79       0
51   53   4       0
52   53   4       0
24   53   24       0
19   50   30       0
42   56   26       0
63   64   9       0
70   71   56       0
71   72   6       0
71   73   5       0
72   73   5       0
73   74   25       0
18   72   92       0
56   67   36       0
12   76   7       0
15   77   13       0
76   77   35       0
60   67   29       0
62   67   31       0'''

    test2 = \
'''NAME : gdb1
VERTICES : 12
DEPOT : 1
REQUIRED EDGES : 22
NON-REQUIRED EDGES : 0
VEHICLES : 5
CAPACITY : 5
TOTAL COST OF REQUIRED EDGES : 252
NODES       COST         DEMAND
1   2   13       1
1   4   17       1
1   7   19       1
1   10   19       1
1   12   4       1
2   3   18       1
2   4   9       1
2   9   2       1
3   4   20       1
3   5   5       1
5   6   7       1
5   11   20       1
5   12   11       1
6   7   4       1
6   12   3       1
7   8   8       1
7   12   18       1
8   10   3       1
8   11   10       1
9   10   16       1
9   11   14       1
10   11   12       1'''

    test3 = \
'''NAME : gdb10
VERTICES : 12
DEPOT : 1
REQUIRED EDGES : 25
NON-REQUIRED EDGES : 0
VEHICLES : 4
CAPACITY : 10
TOTAL COST OF REQUIRED EDGES : 252
NODES       COST         DEMAND
1   8   9       1
1   9   4       2
1   10   13       1
1   11   12       2
2   1   11       1
2   3   15       1
2   4   18       2
2   5   8       2
3   4   8       2
3   8   18       2
3   9   6       1
4   1   7       1
4   6   10       2
4   11   17       1
5   1   9       2
5   6   15       1
6   11   3       2
7   2   6       1
7   4   11       2
7   5   5       1
8   9   14       2
8   12   5       1
9   10   19       1
10   12   2       2
11   12   7       1'''

    carp = CARP(test3.split("\n"))
    carp.carp()

