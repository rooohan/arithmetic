"""
# File       : greedy_algorithm.py
# Time       ：2021/7/27 10:34
# Author     ：Rohan
# version    ：python 3.7
# Description：用贪婪算法解决集合覆盖的问题
"""
import random
from random import shuffle


def create_channel(province: set) -> dict:
    """
    根据传进来的省份集合，随机生成几个频道，且频道包含的省份有重复
    :param province:集合类型，包含所有省份
    :return:返回一个包含频道号和覆盖省份的字典，eg：{0:"山东省"}
    """
    copy_province = province.copy()
    channel = {}
    list_province = list(province)
    # 应该生成全覆盖的电台。由两部分组成：一部分不重复的取1-4集合province，一部分增加0-3个任意省份
    while copy_province:
        result = set()
        count = min(len(copy_province), random.randint(1, 4))
        for i in range(0, count):
            result.add(copy_province.pop())

        for i in range(0, random.randint(0, 3)):
            shuffle(list_province)
            result.add(list_province[0])

        channel[len(channel)] = result

    return channel


def greedy():
    province = {"北京市", "河北省", "山西省", "平原省", "绥远省", "察哈尔省", "辽东省", "辽西省", "吉林省", "黑龙江省", "松江省", "热河省", "陕西省", "甘肃省",
                "宁夏省", "青海省", "新疆省", "山东省", "福建省", "浙江省", "台湾省", "河南省", "湖北省", "湖南省", "江西省", "广东省", "广西省", "贵州省", "云南省"}
    dict_channel = create_channel(province)
    # 贪心算法，每次都找一个能够最大限度覆盖我 还没覆盖的省份的一个电台，直至全部覆盖
    my_target = set()
    while len(province) != len(my_target):
        new_province_count = 0
        pick_num = None
        for ch_num, ch in dict_channel.items():
            # 如果这个频道能够给我们额外增加很多省份，就先增加这个频道
            if len(ch - my_target) > new_province_count:
                new_province_count = len(ch - my_target)
                pick_num = ch_num
        if pick_num is not None:
            print("新增频道", pick_num)
            my_target = my_target | dict_channel[pick_num]
