"""
# File       : dijkstra.py
# Time       ：2021/7/23 15:02
# Author     ：Rohan
# version    ：python 3.7
# Description：狄克斯特拉算法
"""
from collections import OrderedDict

def rank_dict():
    list_node = []

    def rank(dict_cost):
        min_wight = None
        min_node = None
        for node, wight in dict_cost.items():
            if node not in list_node:
                if min_wight is None:
                    min_wight = wight
                    min_node = node
                if wight <= min_wight:
                    min_node = node
        list_node.append(min_node)
        print(min_node, "已经被处理了")
        return min_node

    return rank



def dijkstra(dict_map, dict_parent, dict_cost):
    """
    狄克斯特拉算法
    :param dict_map:存放所有节点，及其子节点的字典
    :param dict_parent:维护记录所有节点的父节，只存放初始状态的即可，算法会不断更新此字典
    :param dict_cost:记录到达某个节点所需要的分数，算法会不断更新此字典
    :return:无返回值，但是传进去的dict_parent和dict_cost会被更新
    """
    set_slave = set()

    # 遍历所有节点
    for slave in dict_map.keys():
        if isinstance(dict_map[slave], dict):
            # 将当前节点，按照权重排序子节点
            order_slave_map = OrderedDict(sorted(dict_map[slave].items(), key=lambda obj: obj[1]))

            # 权重最低的子节点，及对应的权重
            min_slave, min_wight = order_slave_map.popitem(False)

            # 遍历子节点的邻居
            if min_slave in dict_map.keys() and min_slave not in set_slave:
                set_slave.add(min_slave)
                for neighbor, neighbor_wight in dict_map[min_slave].items():
                    # 获取权重字典中，邻居当前的权重
                    neighbor_cost = dict_cost.get(neighbor, float("inf"))
                    # 如果从这个权重最低子节点到邻居节点，权重会降低，那么更新邻居节点的权重和父节点
                    if min_wight + neighbor_wight < neighbor_cost:
                        dict_cost[neighbor] = min_wight + neighbor_wight
                        dict_parent[neighbor] = min_slave


def map_algorithm():
    """
    狄克斯特拉算法 入口
    :return:
    """
    dict_map = {
        "start": {"a": 6, "b": 2},
        "a": {"end": 1},
        "b": {"a": 3, "end": 5}
    }
    dict_parent = {"a": "start", "b": "start", "end": None}
    dict_cost = {"a": 6, "b": 2, "end": float("inf")}
    dijkstra(dict_map, dict_parent, dict_cost)