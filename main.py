import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from random import randint
from time import perf_counter
from matplotlib.animation import PillowWriter
from matplotlib import animation


#question 1
standardList1 = [randint(0, 9) for i in range(1000000)]
standardList2 = [randint(0, 9) for i in range(1000000)]

start1 = perf_counter()
finalList = [standardList1[i] * standardList2[i] for i in range(len(standardList1))]
end1 =perf_counter()

arr1 = np.random.randint(0,10,1000000)
arr2 = np.random.randint(0,10,1000000)

start2 = perf_counter()
np.multiply(arr1,arr2)
end2 = perf_counter()


print(f'time taken for standard multiplication:  {end1-start1}'
      f'time taken for numpy multiplication:   {end2-start2}')

#question 2
def hist():
    arr = np.genfromtxt('data2.csv' , delimiter =',' )
    arr = arr[2:]
    solids = np.int_(arr[:,2])
    fig = plt.figure(figsize=(6,5))
    ax = fig.add_subplot()
    plt.title("Histogram")
    plt.xlabel("solids")
    plt.ylabel("frequency")
    ax.hist(solids,250,(1000, 60000))
    ax.grid()
    plt.show()

def normHist():
    data = pd.read_csv("data2.csv")
    data = data["Solids"]
    plt.hist(data, bins=16, density=True, rwidth=0.5)
    plt.title('Normalized histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

    #standard deviation
    std_dev = np.std(data)
    print('Standard deviation:', std_dev)



#question 3
def graph3d():
    x = np.linspace(-10, 10)
    y = (1/x)
    z = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, c ='blue')
    plt.show()

#Дополнительное задание
fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)
line, = plt.plot(x, y)

def animated(i):
    line.set_ydata(np.sin(x + i/30))
    return line,
anim = animation.FuncAnimation(fig, animated, interval=10, blit=True, save_count=20)

plt.show()

if  "_main_":
    hist()
    normHist()
    graph3d()








