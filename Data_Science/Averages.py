import numpy as np
import pandas as pd


data = {
    'salary_p_year': [50000, 60000, 55000],
    'employees_number': [100, 120, 110]
}
df = pd.DataFrame(data)

weighted_avg_m3 = round(np.average(df['salary_p_year'], weights=df['employees_number']), 2)

print("Weighted Average Salary per Year:", weighted_avg_m3)
