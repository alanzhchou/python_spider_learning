# /usr/bin/env python3
# -*- coding: utf-8 -*-
from data_struct import Stack,Queue,GraphNode,MinPriorityQueue
import sys,time,copy

class Graph(object):
    '''
    类似表示
    graph_test={0:{1:7, 3:3, 4:3, 5:2},
       1:{0:7,2:5, 4:1, 5:2},
       2:{1:5,3:6, 5:3},
       3:{0:3,2:6,5:1},
       4:{0:3,1:1},
       5:{0:2,1:2,2:3,3:1}}
    '''
    def __init__(self,graph = {}):
        self.graph = graph

    def insert_node(self,node_name,route):
        for graph_node in route:
            if graph_node in self.graph:
                self.graph[graph_node][node_name] = route[graph_node]
        self.graph[node_name] = route

    def delete_node(self,node_name):
        if node_name in self.graph:
            for node in self.graph:
                route = self.graph[node]
                if node_name in route:
                    del route[node_name]
            del self.graph[node_name]

    def set_node(self,origin_name,new_name,new_route={}):
        if origin_name in self.graph:
            for node in self.graph:
                route = self.graph[node]
                if origin_name in route:
                    route[new_name] = route.pop(origin_name)
            self.graph[new_name] = self.graph.pop(origin_name)

            if len(new_name) is not 0:
                self.graph[new_name] = new_route

    def dfs_search_any_path(self,start_node_name,end_node_name):
        if (start_node_name not in self.graph) or (end_node_name not in self.graph) :
            return None
        else:
            path = []

            stack = Stack()
            visited = {}
            stack.push(start_node_name)

            while stack.top() is not None:

                # 类似 info = {0:{1:7, 3:3, 4:3, 5:2}}
                start = stack.pop()

                visited[start] = True
                path.append(start)
                if end_node_name in self.graph[start]:
                    path.append(end_node_name)
                    return path
                else:
                    route = self.graph[start]
                    for end in route:
                        if end not in visited:
                            visited[end] = True
                            stack.push(end)
            return None

    def dfs_search_all_from_one_node(self,start_node_name):
        if (start_node_name not in self.graph):
            return None
        else:
            path = []

            stack = Stack()
            visited = {}
            stack.push(start_node_name)

            while stack.top() is not None:

                # 类似 info = {0:{1:7, 3:3, 4:3, 5:2}}
                start = stack.pop()

                visited[start] = True
                path.append(start)

                if len(visited) == len(self.graph):
                    while stack.top() is not None:
                        path.append(stack.pop())
                    return path
                else:
                    route = self.graph[start]
                    for end in route:
                        if end not in visited:
                            visited[end] = True
                            stack.push(end)
            return None

    def bfs_search_any_path(self,start_node_name,end_node_name):
        if (start_node_name not in self.graph) or (end_node_name not in self.graph) :
            return None
        else:
            path = []

            queue = Queue()
            visited = {}
            queue.enQueue(start_node_name)

            while queue.front() is not None:
                # 类似 info = {0:{1:7, 3:3, 4:3, 5:2}}
                start = queue.deQueue()

                if start not in visited:
                    visited[start] = True
                path.append(start)

                if end_node_name in self.graph[start]:
                    path.append(end_node_name)
                    return path
                else:
                    route = self.graph[start]
                    for end in route:
                        if end not in visited:
                            visited[end] = True
                            queue.enQueue(end)

            return None

    def bfs_search_all_from_one_node(self,start_node_name):
        if (start_node_name not in self.graph):
            return None
        else:
            path = []

            queue = Queue()
            visited = {}
            queue.enQueue(start_node_name)

            while queue.front() is not None:

                # 类似 info = {0:{1:7, 3:3, 4:3, 5:2}}
                start = queue.deQueue()

                visited[start] = True
                path.append(start)

                if len(visited) == len(self.graph):
                    while queue.front() is not None:
                        path.append(queue.deQueue())
                    return path
                else:
                    route = self.graph[start]
                    for end in route:
                        if end not in visited:
                            visited[end] = True
                            queue.enQueue(end)
            return None

    # uniform_cost_search
    def dijkstra(self,start_node_name,end_node_name):
        if (start_node_name in self.graph) and (end_node_name in self.graph):
            if start_node_name is end_node_name:
                return {"path":[start_node_name],"min_distance":0}
            else:
                # 根据graph算出来的各节点到其他节点的距离，不能直接到达的用的是整数的最大值
                distance = self.__get_dijkstra_distance()
                # 初始节点到其他节点的距离，不能直接到达的用的是整数的最大值
                start_node_route = distance[start_node_name].copy()

                # 储存初始节点到各个节点的已探测的最小路程路线
                explored_paths = {}
                while len(start_node_route) is not 0:
                    # 初始节点 到 各个未被探测最短距离的节点 中距离最短的节点
                    min_key = self.__find_positive_min_in_dict(start_node_route)

                    path = [start_node_name,min_key]

                    # 初始节点 到 该未被探测节点 的距离
                    min_distance = start_node_route[min_key]
                    for node in explored_paths:
                        last_node_in_path = explored_paths[node]["path"][-1]
                        explored_distance = explored_paths[node]["min_distance"] + distance[last_node_in_path][min_key]

                        if explored_distance < min_distance:
                            path = explored_paths[node]["path"].copy()
                            path.append(min_key)
                            min_distance = explored_distance
                    explored_paths[min_key] = {"path": path, "min_distance": min_distance}
                    del start_node_route[min_key]

                for node in explored_paths:
                    explored_paths[node]["path"].insert(0,start_node_name)
                return explored_paths[end_node_name]
        return None

    def greedy_search_shortest_path(self,start_node_name,end_node_name,info):
        if (start_node_name not in self.graph) or (end_node_name not in self.graph) :
            return None
        else:
            path = []
            queue = MinPriorityQueue()
            visited = {}

            if start_node_name in info:
                queue.en_queue_with_priority(info[start_node_name],start_node_name)

                while queue.front() is not None:
                    start = queue.deQueue()
                    if start not in visited:
                        visited[start] = True
                    path.append(start)

                    if start is not end_node_name:
                        route = self.graph[start]
                        for end in route:
                            if end not in visited:
                                visited[end] = True
                                queue.en_queue_with_priority(info[end], end)
                    else:
                        return path
            return None

    def a_star_search_shortest_path(self,start_node_name,end_node_name,info):
        if (start_node_name in self.graph) and (end_node_name in self.graph):
            if start_node_name == end_node_name:
                return {"path":[start_node_name],"min_distance":0}
            else:
                # 根据graph算出来的各节点到其他节点的距离，不能直接到达的用的是整数的最大值
                distance = self.__get_dijkstra_distance()

                start_node_route = distance[start_node_name].copy()

                queue = MinPriorityQueue()
                priority = 0 + info[start_node_name]
                queue.en_queue_with_priority(priority,start_node_name)

                visited = {}
                # 储存初始节点到各个节点的已探测的最小路程路线
                explored_paths = {start_node_name: {"path": [start_node_name], "min_distance": 0}}
                while queue.front() is not None:
                    # 初始节点 到 各个未被探测最短距离的节点 中距离最短的节点
                    new_node_name = queue.deQueue()
                    # print("***********************")
                    # print(new_node_name)
                    visited[new_node_name] = True
                    linked_nodes = self.graph[new_node_name]

                    # for explored_node_name in explored_paths:

                    for linked_node_name in linked_nodes:
                        if linked_node_name == start_node_name:
                            continue
                        path = [start_node_name,linked_node_name]
                        min_distance = 0
                        # print("\tlinked_node_name: ",linked_node_name)
                        if linked_node_name != start_node_name:
                            min_distance = start_node_route[linked_node_name]

                        # 寻找出发节点到 该 linked_node 的最小距离
                        for explored_node_name in explored_paths:
                            if linked_node_name == explored_node_name:
                                break
                            explored_node_info = explored_paths[explored_node_name]


                            # print("\t\texplored_node_name: ",explored_node_name,explored_node_info)


                            explored_to_distance = explored_node_info["min_distance"] + distance[explored_node_name][linked_node_name]
                            if explored_to_distance < min_distance:
                                path = explored_paths[explored_node_name]["path"].copy()
                                path.append(linked_node_name)
                                min_distance = explored_to_distance
                        # 储存出发节点到 该 linked_node 的最小距离
                        explored_paths[linked_node_name] = {"path": path, "min_distance": min_distance}

                        priority = min_distance + info[linked_node_name]

                        if (linked_node_name == end_node_name) and (queue.front() is None or priority < queue.front()[0]):
                            return explored_paths[end_node_name]
                        else:
                            if linked_node_name not in visited:
                                queue.en_queue_with_priority(priority, linked_node_name)
                return explored_paths[end_node_name]
        else:
            return None

    def __find_positive_min_in_dict(self,dict):
        min_key = -1
        min_value = sys.maxsize + 1

        for key in dict:
            if (dict[key] < min_value):
                min_value = dict[key]
                min_key = key
        if min_key is not -1:
            return min_key
        else:
            return key

    def __get_dijkstra_distance(self):
        # in distance_initial -1 instead of infinite
        # 初始化所有节点的到所有节点的距离 无法直接到达的用 sys.maxsize 表示
        distance = copy.deepcopy(self.graph)
        for node in distance:
            route = distance[node]
            for node_2 in distance:
                if node_2 is not node and (node_2 not in route):
                    route[node_2] = sys.maxsize
        return distance

# for test
if __name__ == "__main__":
    graph_test=\
        {
            "Arad":{"Zerind":75,"sibiu":140,"Timisoara":118},
            "Zerind":{"Arad":75,"Oradea":71},
            "Oradea":{"Zerind":71,"sibiu":151},
            "sibiu":{"Arad":140,"Oradea":151,"Rimnicu Vilcea":80,"Fagaras":99},
            "Fagaras":{"sibiu":99,"Bucharest":211},
            "Timisoara":{"Arad":118,"Lugoj":111},
            "Lugoj":{"Timisoara":111,"Mehadia":70},
            "Mehadia":{"Lugoj":70,"Dobreta":75},
            "Dobreta":{"Mehadia":75,"Craiova":120},
            "Craiova":{"Dobreta":120,"Rimnicu Vilcea":146,"Pitesti":138},
            "Rimnicu Vilcea":{"sibiu":80,"Pitesti":97,"Craiova":146},
            "Pitesti":{"Rimnicu Vilcea":97,"Craiova":138,"Bucharest":101},
            "Bucharest": {"Pitesti": 101, "Fagaras": 211}
        }
    
    graph = Graph(graph_test)

    # print(graph.dfs_search_any_path("Arad","Bucharest"))
    #
    # print(graph.dfs_search_all_from_one_node("Arad"))

    # print(graph.bfs_search_any_path("Arad","Bucharest"))

    # print(graph.bfs_search_all_from_one_node("Arad"))

    nodes_to_end_info = \
        {
            "Arad":366,
            "Bucharest":0,
            "Craiova":160,
            "Dobreta":242,
            "Eforie":161,
            "Fagaras":178,
            "Giurgiu":77,
            "Hirsova":151,
            "Iasi":226,
            "Lugoj":244,
            "Mehadia":241,
            "Neamt":234,
            "Oradea":380,
            "Pitesti":98,
            "Rimnicu Vilcea":193,
            "sibiu":253,
            "Timisoara":329,
            "Urziceni":80,
            "Vaslui":199,
            "Zerind":374
        }

    start1 = time.clock()
    # print(graph.dijkstra("Arad","Bucharest"))
    graph.dijkstra("Arad", "Bucharest")
    stop1 = time.clock()
    print("time: %f"%(stop1-start1))

    # start2 = time.clock()
    # print(graph.greedy_search_shortest_path("Arad","Bucharest",nodes_to_end_info))
    # stop2 = time.clock()
    # print("time: %f"%(stop2-start2))


    # # # print(graph.a_star_search_shortest_path("Arad","Bucharest",nodes_to_end_info))

    start3 = time.clock()
    # print(graph.a_star_search_shortest_path("Arad","Bucharest",nodes_to_end_info))
    graph.a_star_search_shortest_path("Arad", "Bucharest", nodes_to_end_info)
    stop3 = time.clock()
    print("time: %f"%(stop3-start3))