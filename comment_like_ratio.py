import matplotlib.pyplot as plt
from load_data import load_data
import numpy as np
data = [
    {"行数": 89, "Follower 数量": 13000000.0, "like": [2, 10, 26], "comment": [4, 4, 6]},
    {"行数": 516, "Follower 数量": 11900000.0, "like": [9, 16, 9], "comment": [8, 2, 4]},
    {"行数": 416, "Follower 数量": 6600000.0, "like": [87, 105, 26], "comment": [5, 4, 4]},
    {"行数": 137, "Follower 数量": 4100000.0, "like": [194, 5, 24], "comment": [30, 0, 2]},
    {"行数": 461, "Follower 数量": 2200000.0, "like": [2600, 1400, 1200], "comment": [287, 121, 64]},
    {"行数": 197, "Follower 数量": 2000000.0, "like": [32, 23, 59], "comment": [0, 0, 1]},
    {"行数": 419, "Follower 数量": 1900000.0, "like": [36, 34, 43], "comment": [3, 2, 1]},
    {"行数": 570, "Follower 数量": 1900000.0, "like": [14000, 1000, 582], "comment": [2400, 275, 40]},
    {"行数": 317, "Follower 数量": 1800000.0, "like": [30, 100, 48], "comment": [11, 30, 11]},
    {"行数": 522, "Follower 数量": 1300000.0, "like": [10, 22, 16], "comment": [5, 3, 4]},
    {"行数": 195, "Follower 数量": 1000000.0, "like": [3, 2, 1], "comment": [0, 0, 0]},
    {"行数": 420, "Follower 数量": 1000000.0, "like": [6, 2, 3], "comment": [0, 0, 0]}
]

# 计算比值
like_follower_ratios = []
comment_follower_ratios = []
row_numbers = []

# Load your dataset
df = load_data()

for item in data:
    avg_like = sum(item['like']) / len(item['like'])
    avg_comment = sum(item['comment']) / len(item['comment'])
    like_follower_ratios.append(avg_like / item['Follower 数量'])
    comment_follower_ratios.append(avg_comment / item['Follower 数量'])
    row_numbers.append(df.iloc[item['行数']]['Name (English)'])
# 画图
plt.figure(figsize=(12, 6))
bar_width = 0.4  # 稍微增加条形图的宽度，从而增加行间距
index = np.arange(len(row_numbers))  # 使用numpy的arange以支持后续的数值操作

# 绘制第一个柱状图并添加数值标签
bars1 = plt.bar(index, like_follower_ratios, bar_width, label='Like/Follower Ratio')
for bar in bars1:
    yval = bar.get_height()
    plt.text(-0.2+bar.get_x() + bar.get_width()/2.0, yval, '%.4f%%' % (yval * 100), va='bottom', rotation=45)

# 绘制第二个柱状图并添加数值标签
bars2 = plt.bar(index + bar_width, comment_follower_ratios, bar_width, label='Comment/Follower Ratio')
for bar in bars2:
    yval = bar.get_height()
    plt.text(-0.2+bar.get_x() + bar.get_width()/2.0, yval, '%.4f%%' % (yval * 100), va='bottom', rotation=45)

plt.xlabel('Row Number')
plt.ylabel('Ratio')
plt.title('Like/Follower and Comment/Follower Ratios for Twitter Accounts')
plt.xticks(index + bar_width / 2, row_numbers, rotation=45)

# 设置y轴的上限为当前最大值的1.1倍，以留出更多顶部空间
plt.ylim(0, max(max(like_follower_ratios), max(comment_follower_ratios)) * 1.2)

plt.legend()
plt.tight_layout()
plt.show()
