import asyncio
import copy
import datetime
import random
import time
from collections import OrderedDict
from random import  shuffle


def dijkstra(dict_map, dict_parent, dict_cost):
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


def test():
    dict_map = {
        "start": {"a": 6, "b": 2},
        "a": {"end": 1},
        "b": {"a": 3, "end": 5}
    }
    dict_parent = {"a": "start", "b": "start", "end": None}
    dict_cost = {"a": 6, "b": 2, "end": float("inf")}


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


if __name__ == '__main__':
    province = {"北京市", "河北省", "山西省", "平原省", "绥远省", "察哈尔省", "辽东省", "辽西省", "吉林省", "黑龙江省", "松江省", "热河省", "陕西省", "甘肃省",
                "宁夏省", "青海省", "新疆省", "山东省", "福建省", "浙江省", "台湾省", "河南省", "湖北省", "湖南省", "江西省", "广东省", "广西省", "贵州省", "云南省"}
    copy_province = province.copy()
    channel = {}
    list_province = list(province)
    # 应该生成全覆盖的电台。由两部分组成：一部分不重复的取1-4集合province，一部分增加0-3个任意省份
    while copy_province:
        result = set()
        count = min(len(copy_province), random.randint(1,4))
        for i in range(0, count):
            result.add(copy_province.pop())

        for i in range(0,random.randint(0,3)):
            shuffle(list_province)
            result.add(list_province[0])

        channel[len(channel)] = result






