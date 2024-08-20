import json
import time

import pandas as pd
import requests
from collections import Counter

# 读取 player 数据
df = pd.read_csv('players_reward.csv', index_col=0)
top_100_player = df.head(100).index

MAINNET_API = "https://mainnet-api.tig.foundation/"


def get_block_id():
    data1 = requests.get(MAINNET_API + "get-block").json()
    return data1["block"]["id"]


def count_once(player_id, block_id):
    # 统计一个人的
    arg_dict = {'player_id': player_id, 'block_id': block_id}
    benchmarks = requests.get(MAINNET_API + "get-benchmarks", params=arg_dict).json()
    benchmarks = benchmarks["benchmarks"]
    # 统计这个人有解的算法
    algo_list = []
    for b in benchmarks:
        if b["details"]["num_solutions"] > 0:
            algo_list.append(b['settings']['algorithm_id'])
    # 计数器
    c1 = Counter(algo_list)
    return c1


block_id = get_block_id()
result = Counter()  # 总数据
for i in range(100):
    # 逐个统计，叠加结果
    if i % 10 == 0:
        block_id = get_block_id()
    one_result = count_once(top_100_player[i], block_id )
    print(f"第{i + 1}名：", one_result)
    result = result + one_result
    print("总结果：", result)
    time.sleep(5)

# with open('123.json', 'w') as f:
#     json.dump(player_benchmarks, f)
