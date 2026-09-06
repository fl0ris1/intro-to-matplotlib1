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

#polynomial functions
x=np.arange(0,10,0.2)
y_sqr=x**2
y_cubed=x**3
plt.plot(x,y_sqr,color='red',label="Y = X ^ 2")
plt.plot(x,y_cubed,color='green',label="Y = X ^ 3")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.title("Polynomial Functions")
plt.show()


#bar graphs
categories=["A","B","C","D"]
numbers=[4,6,8,3]
plt.bar(categories,numbers,color='blue')
plt.title("Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Numbers")
plt.show()

#multi bar graphs
numbers2=[3,5,6,9]
bar_width=0.35
plt.bar(categories,numbers,color='blue',label="Values 1",width=bar_width)

plt.bar(categories,numbers2,color='green',label="Values 2",width=bar_width,bottom=numbers)

plt.xticks(rotation=45)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple bar graphs")
plt.legend()
plt.show()

#2 graphs

plt.bar(["Male","Female"],[90,95],color='blue')
plt.show()
