#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Alan-11510 
# Date: 2018/11/21
# version: 1.0
# python_version: 3.62

import sys
import copy
import re

class Dis(object):
    def __init__(self,graph):
        self.graph = graph

        # in distance_initial -1 instead of infinite
        # 初始化所有节点的到所有节点的距离 无法直接到达的用 sys.maxsize 表示
        self.distance_matrix = copy.deepcopy(self.graph)

        for node in self.distance_matrix:
            route = self.distance_matrix[node]
            for node_2 in self.distance_matrix:
                if node_2 is not node:
                    if node_2 not in route:
                        route[node_2] = {"path":[node,node_2],"distance":sys.maxsize}
                    else:
                        route[node_2] = {"path": [node, node_2], "distance": route[node_2]}

    def single_all_dij(self,start_node_name):
        if (start_node_name in self.graph):
            # 根据graph算出来的各节点到其他节点的距离，不能直接到达的用的是整数的最大值
            matrix = self.distance_matrix

            # 初始节点到其他节点的距离，不能直接到达的用的是整数的最大值
            nodes_route = copy.deepcopy(matrix[start_node_name])

            # 储存初始节点到各个节点的已探测的最小路程路线
            explored_paths = {}
            while len(nodes_route) != 0:
                min_node_key = self.__find_min_key_in_route(nodes_route)
                min_node_distance = nodes_route[min_node_key]["distance"]
                min_node_path = nodes_route[min_node_key]["path"]

                explored_paths[min_node_key] = {"path": min_node_path,"distance":min_node_distance}
                del nodes_route[min_node_key]

                for node in nodes_route:
                    may_distance = explored_paths[min_node_key]["distance"] + matrix[min_node_key][node]["distance"]
                    if may_distance < nodes_route[node]["distance"]:
                        may_path = copy.copy(explored_paths[min_node_key]["path"])
                        may_path.append(node)
                        nodes_route[node]["path"] = may_path
                        nodes_route[node]["distance"] = may_distance
            return explored_paths
        return None

    def __find_min_key_in_route(self,start_node_route):
        min_key = -1
        min_value = sys.maxsize + 1

        for key in start_node_route:
            if (start_node_route[key]["distance"] < min_value):
                min_value = start_node_route[key]["distance"]
                min_key = key
        return min_key

class InputParser(object):
    def __init__(self,info):
        num_pattern = re.compile("(\d+)")
        str_pattern = re.compile(": (\w+)")

        # 描述信息
        self.name = str_pattern.search(info[0]).group(1)
        self.vertices  = int(num_pattern.search(info[1]).group(1))
        self.depot = int(num_pattern.search(info[2]).group(1))
        self.required_edges = int(num_pattern.search(info[3]).group(1))
        self.non_required_edges = int(num_pattern.search(info[4]).group(1))
        self.vehicles = int(num_pattern.search(info[5]).group(1))
        self.capacity = int(num_pattern.search(info[6]).group(1))
        self.total_cost_of_required_edges = int(num_pattern.search(info[7]).group(1))

        # 原始节点信息
        self.graph = {}
        # 所有需求信息
        self.demands = {}
        for path in info[9:]:
            temp_arr = str(path).split()
            if int(temp_arr[0]) not in self.graph:
                # start, end, cost, demand
                self.graph[int(temp_arr[0])] = {int(temp_arr[1]):(int(temp_arr[2]),int(temp_arr[3]))}
                if int(temp_arr[3]) != 0:
                    self.demands[int(temp_arr[0])] = {int(temp_arr[1]):(int(temp_arr[2]),int(temp_arr[3]))}
            else:
                self.graph[int(temp_arr[0])][int(temp_arr[1])] = (int(temp_arr[2]),int(temp_arr[3]))
                if int(temp_arr[3]) != 0:
                    self.demands[int(temp_arr[0])][int(temp_arr[1])] = (int(temp_arr[2]),int(temp_arr[3]))

        # 用来计算路由算法的处理后节点信息
        self.dis_graph = {}
        for key in self.graph:
            self.dis_graph[key] = {}

            item = self.graph[key]
            for key2 in item:
                self.dis_graph[key][key2] = item[key2][0]
        temp_dict = copy.deepcopy(self.dis_graph)
        for start in temp_dict:
            ends_info = temp_dict[start]
            for end in ends_info:
                if end not in self.dis_graph:
                    self.dis_graph[end] = {}
                    self.dis_graph[end][start] = temp_dict[start][end]
                else:
                    self.dis_graph[end][start] = temp_dict[start][end]

        # 所有节点名称
        self.nodes = list(self.dis_graph)

        # 每个节点到其他
        self.shortest_paths = {}
        dis = Dis(self.dis_graph)
        for node in self.nodes:
            self.shortest_paths[node] = dis.single_all_dij(node)

    def get_node_names(self):
        return self.nodes

    def get_depot(self):
        return self.depot

    def get_capacity(self):
        return self.capacity

    def get_vehicles (self):
        return self.vehicles

    def get_demands(self):
        return self.demands

    def get_shortest_paths(self):
        return self.shortest_paths

    # def get_str_capacity(self):
    #     return str(self.capacity)
    #
    # def get_str_demands(self):
    #     result = ""
    #     for path in self.demands:
    #         result += (str(path) + " : " + str(self.demands[path]) + "\n")
    #     return result
    #
    # def get_str_shortest_paths(self):
    #     result = ""
    #     for path in self.shortest_paths:
    #         result += (str(path) + " : " + str(self.shortest_paths[path]) + "\n")
    #     return result
    #
    # def get_str_dis_graph(self):
    #     result = ""
    #     for node in self.dis_graph:
    #         result += str(node) + " : " + str(self.dis_graph[node]) + "\n"
    #     return result
    #
    # def get_str_node_names(self):
    #     return str(list(self.nodes))

    def __str__(self):
        graph = "\n"
        for key in self.graph:
            graph += str(key) + " : " + str(self.graph[key]) + "\n"

        return ("name : %s\n" +
                "vertices : %d\n" +
                "depot : %d\n" +
                "required_edges : %d\n" +
                "non_required_edges : %d\n" +
                "vehicles : %d\n" +
                "capacity : %d\n" +
                "total_cost_of_required_edges : %d\n" +
                "graph : %s\n" ) % \
               (self.name, self.vertices, self.depot, self.required_edges,
                self.non_required_edges, self.vehicles, self.capacity, self.total_cost_of_required_edges,
                graph)

class CARP(object):
    def __init__(self,info):
        parser = InputParser(info)

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

            while temp_capacity < capacity:
                founded = False
                for demand in free:
                    if demand[3] + temp_capacity <= capacity:
                        temp_capacity += demand[3]
                        new_route.append(demand)
                        founded = True
                        break
                if founded:
                    free.remove(demand)
                else:
                    break
            routes.append(new_route)

        print("s",end=" ")
        # find path cost along route
        cost = 0
        for route in routes:
            print(0,end=",")
            for demand in route:
                body = "("+ str(demand[0]) + "," + str(demand[1]) + "),"
                print(body,end="")
            if route == routes[len(routes)-1]:
                print(end="0")
            else:
                print(end="0,")

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
            cost += paths[next_demand[1]][self.depot]["distance"]
        print()
        print("q",cost)

    def __str__(self):
        demands = "\n"
        for key in self.demands:
            demands += str(key) + " : " + str(self.demands[key]) + "\n"

        shortest_paths = "\n"
        for key in self.shortest_paths:
            shortest_paths += str(key) + " : " + str(self.shortest_paths[key]) + "\n"

if __name__ == '__main__':
    info = []
    temp = input()

    while temp != "END":
        info.append(temp)
        temp = input()

    carp = CARP(info)
    carp.carp()