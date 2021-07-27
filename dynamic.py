"""
# File       : dynamic.py
# Time       ：2021/7/27 15:47
# Author     ：Rohan
# version    ：python 3.7
# Description：动态规划
"""
import collections

Items = collections.namedtuple("Items", ["name", "price", "wight"])


def dynamic_programming(items: list, max_wight) -> list:
    nobody = Items(None, 0, 0)
    # 初始化一个二维list，第一行代表可偷的物品为空，所以背包都是空
    list_result = [[nobody for i in range(max_wight + 1)]]
    # 将二维list的第一列初始化为空，代表背包容量为0；添加这两列对后面写逻辑判断有帮助
    for i in range(len(items)):
        list_result.append([nobody])

    for row, item in enumerate(items):
        row_result = []
        for current_wight in range(1, max_wight + 1):
            # 相同容积下，历史的最佳纪录
            history_choice = list_result[row][current_wight]

            # 新的可偷的东西目前能放进袋子里
            if item.wight <= current_wight:
                # 如果把新的可偷的作为必偷物，然后根据剩余空间，可以轻松的选出最佳组合即 history_second_choice变量
                history_second_choice = list_result[row][current_wight - item.wight]
                if history_second_choice.name is not None:
                    might_choice_name = item.name + ", " + history_second_choice.name
                    might_choice_wight = item.wight + history_second_choice.wight
                    might_choice_price = item.price + history_second_choice.price

                    might_choice = Items(might_choice_name, might_choice_price, might_choice_wight)
                else:
                    might_choice = item
            # 新的可偷的东西目前不能放进袋子里
            else:
                might_choice = history_choice
            # 两种方案选择最棒的方案
            if history_choice.price >= might_choice.price:
                row_result.append(history_choice)
            else:
                row_result.append(might_choice)

        list_result[row + 1].extend(row_result)
    return list_result


def main():
    # 可偷物品
    list_items = [Items("PS5", 3000, 4), Items("Switch", 2200, 2),
                  Items("Airpods", 1800, 1), Items("Ipad", 2899, 2),
                  Items("Kindle", 899, 1)]
    # 背包最大重量
    max_wight = 6

    result = dynamic_programming(list_items, max_wight)
    pass
