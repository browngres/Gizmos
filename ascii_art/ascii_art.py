import pandas
# X 朝右递增，Y 朝上递增
TEST_URL = "xxx"
# read the html, find the table and convert it to df.
test_df = pandas.read_html(TEST_URL, encoding="utf-8", header=0)[0]
test_df = test_df.set_index(["y-coordinate", "x-coordinate"])
df2 = test_df.unstack()  # 1-D to 2-D
df2.fillna(" ", inplace=True)  # fill na
df2 = df2.iloc[::-1]    # reverse y-coordinate
print(df2)
print("------")
# print by row
for idx, row in df2.iterrows():
    char = str.join("", row.values)
    print(char)