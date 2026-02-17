import numpy as np
import pandas as pd

df = pd.read_csv("Iris.csv")   

# Convert to NumPy array (drop Id column)
iris = df.iloc[:, 1:5].values


sepal_length = iris[:, 0]

sorted_sepal = np.sort(sepal_length)

print(sorted_sepal)
