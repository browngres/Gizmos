import pandas

# X increases to the right, Y increases to the top

TEST_URL = "xxx"
MESSAGE_URL = "xxx"


def get_table(url: str):
    # read the html, find the table and convert it to df.
    df = pandas.read_html(url, encoding="utf-8", header=0)[0]
    df = df.set_index(["y-coordinate", "x-coordinate"])
    df2 = df.unstack()  # 1-D to 2-D
    df2.fillna(" ", inplace=True)  # fill na
    df2 = df2.iloc[::-1]  # reverse y-coordinate
    return df2


if __name__ == '__main__':
    # table = get_table(TEST_URL)
    table = get_table(MESSAGE_URL)
    
    # print it by row
    for idx, row in table.iterrows():
        char = str.join("", row.values)
        print(char)
