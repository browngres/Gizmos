import json
import time

import pandas as pd
import requests
from collections import Counter
# 读取 player 数据
df = pd.read_csv('players_reward.csv', index_col=0)

top_100_player = df.head(100).index

MAINNET_API = "https://mainnet-api.tig.foundation/get-block"
data1 = requests.get(MAINNET_API).json()
block_id = data1["block"]["id"]

result = Counter()  # 计算总数据


def count_once(player_id):
    # 统计一个人的
    arg_dict = {'player_id': player_id, 'block_id': block_id}
    url = "https://mainnet-api.tig.foundation/get-benchmarks"
    benchmarks = requests.get(url, params=arg_dict).json()
    benchmarks = benchmarks["benchmarks"]
    # 统计这个人有解的算法
    algo_list = []
    for b in benchmarks :
        if b["details"]["num_solutions"]>0:
            algo_list.append(b['settings']['algorithm_id'])
    # 计数器
    c1 = Counter(algo_list)
    return c1



for i in top_100_player:
    # 逐个统计，叠加结果
    one_result = count_once(i)
    print(one_result)
    time.sleep(1)
    result = result + one_result
    print(f"result: {result}")



# with open('123.json', 'w') as f:
#     json.dump(player_benchmarks, f)
