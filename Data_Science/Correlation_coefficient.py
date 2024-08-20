import math 
 
def correlationCoefficient(X, Y, n) : 
    sum_X = 0 
    sum_Y = 0 
    sum_XY = 0 
    squareSum_X = 0 
    squareSum_Y = 0 
             
    i = 0 
    while i < n :
        sum_X = sum_X + X[i] 
        sum_Y = sum_Y + Y[i] 
        sum_XY = sum_XY + X[i] * Y[i]  
        squareSum_X = squareSum_X + X[i] * X[i] 
        squareSum_Y = squareSum_Y + Y[i] * Y[i]
        i = i + 1
    corr = (float)(n * sum_XY - sum_X * sum_Y)/ (float)(math.sqrt((n * squareSum_X - sum_X * sum_X)* (n * squareSum_Y -  sum_Y * sum_Y))) 
    return corr 

X = [15, 18, 21, 24, 27] 
Y = [25, 25, 27, 31, 32] 
n = len(X) 
print ('{0:.6f}'.format(correlationCoefficient(X, Y, n)))