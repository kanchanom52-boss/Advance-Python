import numpy as np
import pandas as pd

# Set the seed for reproducibility
np.random.seed(42)

# Generate 10 random integers between 1 and 100
data = np.random.randint(1, 101, 10)

# Create the pandas Series
s = pd.Series(data)

# Print the Series
print(s)
