import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

data = np.arange(1, 10, 0.01)
pdf = norm.pdf(data, loc=5.3, scale=1)

sb.set_style('whitegrid')
plt.plot(data, pdf, color='black')
plt.xlabel('Heights')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.show() 
 