import random
from random import shuffle


if __name__ == '__main__':
    province = {"北京市", "河北省", "山西省", "平原省", "绥远省", "察哈尔省", "辽东省", "辽西省", "吉林省", "黑龙江省", "松江省", "热河省", "陕西省", "甘肃省",
                "宁夏省", "青海省", "新疆省", "山东省", "福建省", "浙江省", "台湾省", "河南省", "湖北省", "湖南省", "江西省", "广东省", "广西省", "贵州省", "云南省"}
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
