import matplotlib.pyplot as plt 
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(0,0,c='green',s=100)
plt.scatter(x_values,y_values,c=(0.5,0.5,0.6),s=15)
plt.title("Squarre Number",  fontsize=24)
plt.xlabel("value",fontsize=12)
plt.ylabel("square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.savefig('scaquartPlot.png',bbox_inches='tight')
plt.show()