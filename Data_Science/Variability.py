from statistics import variance  
from fractions import Fraction as fr 

sample1 = (1, 2, 5, 4, 8, 9, 12) 

sample2 = (-2, -4, -3, -1, -5, -6) 

sample3 = (-9, -1, -0, 2, 1, 3, 4, 19) 

sample4 = (fr(1, 2), fr(2, 3), fr(3, 4), fr(5, 6), fr(7, 8)) 

sample5 = (1.23, 1.45, 2.1, 2.2, 1.9) 
 
 
print("Variance of Sample1 is % s " %(variance(sample1))) 
print("Variance of Sample2 is % s " %(variance(sample2))) 
print("Variance of Sample3 is % s " %(variance(sample3))) 
print("Variance of Sample4 is % s " %(variance(sample4))) 
print("Variance of Sample5 is % s " %(variance(sample5))) 
 
 
 
 
 
 
 