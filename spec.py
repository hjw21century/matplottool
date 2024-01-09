import matplotlib.pyplot as plt
import sys
import math

average_time = 9
# 读取包含所有数据的文本文件
with open('./10次数据-5-2.LOG', 'r') as file:
    lines = file.readlines()

# 初始化数据列表
data = [[]]
for i in range(0, average_time):
    data.append([])

# 标识当前处理的数据部分（假设每部分以标识行开头）
current_data = None

# 遍历每行数据
for line in lines:
    # 切割每行数据，并选取包含所需信息的部分
    if (line.find('[samping]') == -1):
        continue
    parts = line.strip().split()
    # 00000002	59.59106064	[10236] [samping] average[0] p1[3695.735840] p2[0.000000] index[0], real[3695.735840], image[0.000000] 	
    # 00000003	59.59128189	[10236] [samping] average[0] p1[-123.719116] p2[28.096172] index[1], real[-123.719116], image[28.096172]
    average = int(parts[4].split('[')[-1].strip(']'))
    index = int(parts[7].split('[')[-1].strip('],'))
    real = float(parts[8].split('[')[-1].strip('],'))
    image = float(parts[9].split('[')[-1].strip(']'))
    amp = math.sqrt(real * real + image * image)
    
    for i in range(0, average_time):
        if index >= 200:
            continue
        if average == i:
            data[i].append((index, real, image, amp))

colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'red', 'purple', 'orange']
markers = ['o', 's', '^', 'o', 's', '^', 'o', 's', '^']
# 创建图表并绘制数据
plt.figure(figsize=(10, 6))
for i in range(0, average_time):
    # 提取数据
    indices, real, image, amp = zip(*(data[i]))
    plt.plot(indices, amp, label = f'Real (Data {i + 1})', color = colors[i], marker = markers[i])


# 设置图表标签和标题
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Real and Image Data')

# 显示图例
plt.legend()

# 显示图表
plt.grid(True)
plt.show()