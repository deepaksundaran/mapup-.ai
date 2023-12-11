import pandas as pd

def calculate_distance_matrix(df):
    unique_ids = sorted(set(df['id_start']).union(set(df['id_end'])))
    distance_matrix = pd.DataFrame(0, columns=unique_ids, index=unique_ids)
    
    for _, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.at[start_id, end_id] += distance
        distance_matrix.at[end_id, start_id] += distance
    
    distance_matrix.values[[range(len(distance_matrix))]*2] = 0
    return distance_matrix

def unroll_distance_matrix(distance_matrix):
    ids = distance_matrix.index.tolist()
    unrolled_distances = []
    
    for i in range(len(ids)):
        for j in range(len(ids)):
            id_start = ids[i]
            id_end = ids[j]
            
            if id_start != id_end and distance_matrix.at[id_start, id_end] != 0:
                distance = distance_matrix.at[id_start, id_end]
                unrolled_distances.append([id_start, id_end, distance])
    
    result_df = pd.DataFrame(unrolled_distances, columns=['id_start', 'id_end', 'distance'])
    return result_df

def find_ids_within_percentage_threshold(df, reference_id):
    # Calculate average distance for the reference value
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()
    
    # Calculate lower and upper threshold values (10% above and below average distance)
    lower_threshold = reference_avg_distance - (reference_avg_distance * 0.1)
    upper_threshold = reference_avg_distance + (reference_avg_distance * 0.1)
    
    # Filter IDs within the 10% threshold
    filtered_ids = df[(df['distance'] >= lower_threshold) & (df['distance'] <= upper_threshold)]['id_start'].unique()
    sorted_filtered_ids = sorted(filtered_ids)
    
    return sorted_filtered_ids

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)

# Unroll the distance matrix
result_unrolled_distances = unroll_distance_matrix(result_distance_matrix)

# Find IDs within 10% threshold for a reference ID (e.g., reference_id = 100 as an example)
reference_id = 100  # Change this value as needed
ids_within_threshold = find_ids_within_percentage_threshold(result_unrolled_distances, reference_id)
print(f"IDs within 10% threshold of average distance for ID {reference_id}:")
print(ids_within_threshold)