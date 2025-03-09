
import pandas as pd
matches = pd.read_csv("/Users/tshreek/Downloads/ipldata/matches.csv")  # Corrected filename

# Display the first few rows
print(matches.head())

# Check dataset information
print(matches.info())

# Check for missing values
print(matches.isnull().sum())
