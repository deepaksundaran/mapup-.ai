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

def calculate_toll_rate(df):
    df['moto'] = df['distance'] * 0.8
    df['car'] = df['distance'] * 1.2
    df['rv'] = df['distance'] * 1.5
    df['bus'] = df['distance'] * 2.2
    df['truck'] = df['distance'] * 3.6
    
    return df

# Read the dataset into a DataFrame
dataset_df = pd.read_csv(r"C:\Users\DEEPAK\OneDrive\Desktop\dataset\dataset-3.csv")

# Calculate the distance matrix
result_distance_matrix = calculate_distance_matrix(dataset_df)

# Unroll the distance matrix
result_unrolled_distances = unroll_distance_matrix(result_distance_matrix)

# Calculate toll rates based on vehicle types
result_with_toll_rates = calculate_toll_rate(result_unrolled_distances)
print(result_with_toll_rates)