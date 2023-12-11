import pandas as pd

def get_type_count(df):
    # Add a new column 'car_type' based on conditions
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)
    
    # Count occurrences for each car_type category
    type_count = df['car_type'].value_counts().to_dict()
    
    # Sort the dictionary alphabetically based on keys
    sorted_type_count = dict(sorted(type_count.items()))
    
    return sorted_type_count

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')

# Call the function to get the count of occurrences for each car_type category
result = get_type_count(dataset_df)
print(result)