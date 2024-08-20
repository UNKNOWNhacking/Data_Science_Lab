import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100)
yl = 5 * x + 9
y2 = -5 * x
y3 = np.random.randn(100)

plt.figure(figsize=(10, 8), dpi=100)
plt.scatter(x, yl, label='yl, Correlation = {:.2f}'.format(np.corrcoef(x, yl)[0, 1]))
plt.scatter(x, y2, label='y2, Correlation = {:.2f}'.format(np.corrcoef(x, y2)[0, 1]))
plt.scatter(x, y3, label='y3, Correlation = {:.2f}'.format(np.corrcoef(x, y3)[0, 1]))

plt.title('Scatterplot and Correlations')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()
