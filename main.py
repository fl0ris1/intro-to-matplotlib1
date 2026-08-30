import matplotlib.pyplot as plt
import numpy as np

#basic line graph

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

sales=["1000","900","950","850","1100","1050","1000","900","1100","800","900","1050"]

plt.plot(months, sales, color='red')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#scatter plot
plt.scatter(months, sales, color='red')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#limit numbers on each axis
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[10,20,30,40,50,60,70,80,90,100,110,120]
plt.plot(x,y,color='red')
plt.axis([1,10,10,100])
plt.show()

#create a line graph with line width
plt.plot(months, sales, linewidth=5, label="Sales",color='blue')
plt.xlabel("months")
plt.ylabel("sales")
plt.legend()
plt.title("Sales per Month")
plt.show()

#plot multiple line graphs
spendings=[300,100,200,400,100,150,200,350,500,100,200,50]
plt.plot(months,sales, color='red', linewidth=3,label="Sales")
plt.plot(months,spendings, color='blue', linewidth=3, label='Spendings')
plt.xlabel("Months")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("Finances")
plt.show()

