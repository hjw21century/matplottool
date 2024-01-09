import matplotlib.pyplot as plt
import sys
import math

# 初始化数据列表
data1, data2, data3 = [], [], []

def GetSpecData(filename, data):
    # 读取包含所有数据的文本文件
    with open(filename, 'r') as file:
        lines = file.readlines()

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
        
        if index >= 200:
            continue
        if average == 0:
            print(f'average: {average}, index: {index}, real: {real}, image: {image}, amp: {amp}')
            data.append((index, real, image, amp))
        else:
            pass
    

GetSpecData('LAPTOP-Q3NRQ1ER-11.LOG', data1)
GetSpecData('LAPTOP-Q3NRQ1ER-15.LOG', data2)
GetSpecData('LAPTOP-Q3NRQ1ER-13.LOG', data3)

# 提取数据
indices1, real1, image1, amp1 = zip(*data1)
indices2, real2, image2, amp2 = zip(*data2)
indices3, real3, image3, amp3 = zip(*data3)

# 创建图表并绘制数据
plt.figure(figsize=(10, 6))
plt.plot(indices1, amp1, label='Real (Data 1)', color='blue', marker='o')
# plt.plot(indices1, image1, label='Image (Data 1)', color='green', marker='o')
plt.plot(indices2, amp2, label='Real (Data 2)', color='red', marker='s')
# plt.plot(indices2, image2, label='Image (Data 2)', color='purple', marker='s')
plt.plot(indices3, amp3, label='Real (Data 3)', color='orange', marker='^')
# plt.plot(indices3, image3, label='Image (Data 3)', color='brown', marker='^')

# 设置图表标签和标题
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Real and Image Data')

# 显示图例
plt.legend()

# 显示图表
plt.grid(True)
plt.show()