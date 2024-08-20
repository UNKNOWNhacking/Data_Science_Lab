import matplotlib.pyplot as plt 

a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
plt.plot(a) 

plt.plot(b, "or") 
 
plt.plot(list(range(0, 22, 3))) 
 
plt.xlabel('Day ->') 
 
plt.ylabel('Temp ->') 
 
c = [4, 2, 6, 8, 3, 20, 13, 15] 
plt.plot(c, label = '4th Rep') 
 
ax = plt.gca() 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 
ax.spines['left'].set_bounds(-3, 40) 
plt.xticks(list(range(-3, 10))) 
plt.yticks(list(range(-3, 20, 3))) 
ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep']) 
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15)) 
plt.title('All Features Discussed') 
plt.show()
 
 
