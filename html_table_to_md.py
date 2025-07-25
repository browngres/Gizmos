from bs4 import BeautifulSoup

def html_table_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    # 获取表头
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    # 获取表格行
    rows = []
    for row in table.find_all('tr')[1:]:  # 从第二行开始，因为第一行是表头
        cells = row.find_all('td')
        if cells:
            rows.append([cell.get_text(strip=True) for cell in cells])

    # 转换为 Markdown 格式
    md = []

    # 表头部分
    md.append('| ' + ' | '.join(headers) + ' |')
    md.append('|' + '---|' * len(headers))  # 分隔符

    # 表格数据部分
    for row in rows:
        md.append('| ' + ' | '.join(row) + ' |')

    return '\n'.join(md)


# 示例
html_content = """
 <table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
    <th>Header 3</th>
  </tr>
  <tr>
    <td>Row 1 Col 1</td>
    <td>Row 1 Col 2</td>
    <td>Row 1 Col 3</td>
  </tr>
  <tr>
    <td>Row 2 Col 1</td>
    <td>Row 2 Col 2</td>
    <td>Row 2 Col 3</td>
  </tr>
</table>
"""

markdown = html_table_to_markdown(html_content)
with open('table.md', 'w') as f:
    f.write(markdown)