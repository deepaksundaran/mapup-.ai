import pandas as pd

def generate_car_matrix():
    # Read the dataset into a DataFrame
    df = pd.read_csv(r'C:\Users\DEEPAK\OneDrive\Desktop\python\datasets-1.csv')
    
    # Select the required columns
    filtered_df = df[['id_1', 'id_2', 'car']]
    
    # Create a pivot table to get car values in the desired matrix format
    car_matrix = filtered_df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    return car_matrix

# Call the function to get the desired DataFrame
result_matrix = generate_car_matrix()
print(result_matrix)