import pandas as pd

def get_bus_indexes(df):
    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()
    
    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()
    
    # Sort the indices in ascending order
    bus_indexes.sort()
    
    return bus_indexes

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')

# Call the function to get the indices where 'bus' values are greater than twice the mean
result = get_bus_indexes(dataset_df)
print(result)