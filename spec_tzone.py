import matplotlib.pyplot as plt
import sys
import math

average_time_start = int(sys.argv[1])
print(f'average_time_start = {average_time_start}\r\n')

average_time = average_time_start + 1
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
    if (line.find('[realtime]') == -1):
        continue
    
    parts = line.strip().split()
    # 00000878	0.03263780	[21404] [realtime] average[0] p[-24629] index[877] 	
    # 00000879	0.03265740	[21404] [realtime] average[0] p[-24626] index[878] 	
    # 00000880	0.03267760	[21404] [realtime] average[0] p[-24622] index[879]

    average = int(parts[4].split('[')[-1].strip(']'))
    index = int(parts[6].split('[')[-1].strip('],'))
    amp = int(parts[5].split('[')[-1].strip('],'))
    #if index > 840:
    #    continue
    
    for i in range(average_time_start, average_time):
        if average == i:
            data[i].append((average, index, amp))

colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'red', 'purple', 'orange']
markers = ['o', 's', '^', 'o', 's', '^', 'o', 's', '^']
# 创建图表并绘制数据
plt.figure(figsize=(10, 6))
for i in range(average_time_start, average_time):
    # 提取数据
    average, index, amp = zip(*(data[i]))
    # plt.plot(index, amp, label = f'Real (Data {i + 1})', color = colors[i], marker = markers[i])
    plt.plot(index, amp)


# 设置图表标签和标题
plt.xlabel('Index')
plt.ylabel('Value')
plt.title(f'Real and Image Data [{average_time_start + 1}]')

# 显示图例
plt.legend()

# 显示图表
plt.grid(True)
plt.show()
