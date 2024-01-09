import matplotlib.pyplot as plt
import sys
import math

data = []
with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.lstrip('\t')
        if line.startswith('['):
            items = line.split('\t')
            data.append(float(items[1]))


plt.plot(range(len(data)), data)
plt.show()