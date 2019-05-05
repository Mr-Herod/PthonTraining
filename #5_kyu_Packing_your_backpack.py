Description:

"""
You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. The bad news is that the airline has informed you, that your luggage cannot exceed a certain amount of weight.
To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items that you decide to bring.
Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of equal length, so you don't have to worry about verifying your input.
You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.
For instance, given these inputs:
scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8The maximum score will be 29. This number comes from bringing items 1, 3 and 4.
Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.

"""

My codes:

def pack_bagpack(scores, weights, capacity):
    pack= [0 for _ in range(1000)]
    for i in range(len(scores)):
        for j in range(capacity,weights[i]-1,-1):
            pack[j] = max(pack[j-weights[i]]+scores[i],pack[j])
    return pack[capacity]

Others codes:

def pack_bagpack(S,W,C) :
    M = [0] * (1 + C)
    for F,V in enumerate(S) :
        M = [max(U,M[T - W[F]] + V if W[F] <= T else 0) for T,U in enumerate(M)]
    return M[-1]

import time
def pack_bagpack(scores, weights, capacity):
    """
    求最大分数
    :param scores:   行李评分列表
    :param weights:  行李重量列表
    :param capacity: 限制重量
    :return: 最大分数

    1）按照均分倒序排列
    2) 递归组合
        max_value = max(包含自己的最大值, 跳过自己的最大值)
    3) 得出最优
    """
    start_time = time.time()
    # 组合
    lst = list(zip(scores, weights))

    # 1) 倒序排列 >> 均分 = 分数/重量
    lst_sorted = sorted(lst, key=lambda x: x[0], reverse=True)

    cache_dict = {}

    def calc_item(index, weight_last):
        if index >= len(lst_sorted) or weight_last <= 0:
            return 0
        current = lst_sorted[index]

        cache_key = "{}-{}".format(index, weight_last)

        if cache_key not in cache_dict:
            # 算上当前的最大结果
            score_with_current = 0
            if weight_last >= current[1]:
                score_with_current = current[0] + calc_item(index + 1, weight_last - current[1])
            # 跳过当前的最大结果
            score_no_current = calc_item(index + 1, weight_last)

            # 缓存当前的位置和剩余重量的值, 让以后的递归不再重复计算类似结果
            cache_dict[cache_key] = max(score_with_current, score_no_current)
            
        return cache_dict[cache_key]

    final_score = calc_item(0, capacity)

    print("score: {}  duration---> {}".format(final_score,time.time() - start_time))
    # 3) 得出最优
    return final_score
