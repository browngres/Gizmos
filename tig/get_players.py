import requests
import json
import pandas as pd

# 查询所有 player 的数据
'''
MAINNET_API = "https://mainnet-api.tig.foundation/get-block"
data1 = requests.get(MAINNET_API).json()
block_id = data1["block"]["id"]

arg_dict = {'player_type': "benchmarker", 'block_id': block_id}
response = requests.get("https://mainnet-api.tig.foundation/get-players",
                        params = arg_dict)
# 存为文件
with open('data.json', 'w') as f:
    json.dump(response.json(), f)
'''

###################

# 读取文件
with open('data.json', 'r') as f:
    data = json.load(f)
    f.close()
players = data["players"]

# 取出两列
player_id = []
reward = []
for i in range(len(players)):
    player_id.append(players[i]["id"])
    reward.append(players[i]["block_data"]['reward'])

df = pd.DataFrame(index=player_id, data=reward, columns=["reward"])
df.fillna(value=0, inplace=True)  # 填充空值
df["reward"] = df["reward"].astype(int)  # 转换格式
# print(df.head(10))

# 按 reward 排序
df2 = df.sort_values(by=["reward"], ascending=False)
# print(df2.head(10))
df2.to_csv("players_reward.csv")