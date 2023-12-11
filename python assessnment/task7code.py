import pandas as pd

def calculate_distance_matrix(df):
    # Create an empty DataFrame with unique IDs to store distances
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    # Calculate cumulative distances between IDs
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance  # Ensure symmetry
    
    # Set diagonal values to 0
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    
    return distance_matrix

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)
print(result_distance_matrix)