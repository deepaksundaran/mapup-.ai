import pandas as pd

# Generate initial DataFrame
def generate_car_matrix():
    df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\datasets-1.csv")
    pivot_table = df.pivot(index='id_1', columns='id_2', values='car')
    pivot_table.values[[range(len(pivot_table))]*2] = 0
    return pivot_table

# Modify values in the DataFrame
def multiply_matrix(dataframe):
    modified_df = dataframe.copy()
    modified_df[dataframe > 20] *= 0.75
    modified_df[dataframe <= 20] *= 1.25
    modified_df = modified_df.round(1)
    return modified_df

# Use both functions together
car_matrix = generate_car_matrix()
modified_car_matrix = multiply_matrix(car_matrix)

# Display the modified DataFrame
print(modified_car_matrix)

