Question 1: Car Matrix Generation
Under the function named generate_car_matrix write a logic that takes the dataset-1.csv as a DataFrame. Return a new DataFrame that follows the following rules:

values from id_2 as columns
values from id_1 as index
dataframe should have values from car column
diagonal values should be 0.


                                  ...                                 
![TASK1](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/c34afa2b-72cb-4067-803e-ad6112cc77d6)
![task1answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/ba1757e6-b9de-4709-84fb-9535a6c4755c)

Question 2: Car Type Count Calculation
Create a Python function named get_type_count that takes the dataset-1.csv as a DataFrame. Add a new categorical column car_type based on values of the column car:

low for values less than or equal to 15,
medium for values greater than 15 and less than or equal to 25,
high for values greater than 25.
Calculate the count of occurrences for each car_type category and return the result as a dictionary. Sort the dictionary alphabetically based on keys.






![TASK2](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/a588f630-4c4f-4d55-95f2-406cd5f6d33c)
![task2answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/853b5f88-ea04-40b0-be53-55160f89a86d)

Question 3: Bus Count Index Retrieval
Create a Python function named get_bus_indexes that takes the dataset-1.csv as a DataFrame. The function should identify and return the indices as a list (sorted in ascending order) where the bus values are greater than twice the mean value of the bus column in the DataFrame.




![TASK3](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/19346ddb-8ce4-4a0d-8a9b-a0dc21872870)![task3answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/4d688ce9-9965-4bd5-8048-29ba7a047e95)

Question 4: Route Filtering
Create a python function filter_routes that takes the dataset-1.csv as a DataFrame. The function should return the sorted list of values of column route for which the average of values of truck column is greater than 7.





![TASK4](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2c56e611-8023-4161-98ba-c9c4b6ca6c6f)

![task4answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/b1374d0d-2f0c-40d3-ad11-876e23b93b6b)

Question 5: Matrix Value Modification
Create a Python function named multiply_matrix that takes the resulting DataFrame from Question 1, as input and modifies each value according to the following logic:

If a value in the DataFrame is greater than 20, multiply those values by 0.75,
If a value is 20 or less, multiply those values by 1.25.
The function should return the modified DataFrame which has values rounded to 1 decimal place.








![TASK5](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/3378a7d0-0e9b-466b-ba5c-70b756a4a8e0)


![task5answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/f614de67-1144-4d27-976b-a0f624214b6c)


Question 6: Time Check
You are given a dataset, dataset-2.csv, containing columns id, id_2, and timestamp (startDay, startTime, endDay, endTime). The goal is to verify the completeness of the time data by checking whether the timestamps for each unique (id, id_2) pair cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).

Create a function that accepts dataset-2.csv as a DataFrame and returns a boolean series that indicates if each (id, id_2) pair has incorrect timestamps. The boolean series must have multi-index (id, id






![TASK6](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/47385083-5f14-40f1-9370-9da53157d8d6)


![task6answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/68d7b1ee-eb38-4e8d-bc86-968fbc86689c)

Question 1: Distance Matrix Calculation
Create a function named calculate_distance_matrix that takes the dataset-3.csv as input and generates a DataFrame representing distances between IDs.

The resulting DataFrame should have cumulative distances along known routes, with diagonal values set to 0. If distances between toll locations A to B and B to C are known, then the distance from A to C should be the sum of these distances. Ensure the matrix is symmetric, accounting for bidirectional distances between toll locations (i.e. A to B is equal to B to A).



 

![TASK7](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2085bf24-8279-47cb-a563-5366c9dc2ab2)


![task7answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/d883cdbc-3d04-41b0-bf95-edfaff8baa58)


Question 2: Unroll Distance Matrix
Create a function unroll_distance_matrix that takes the DataFrame created in Question 1. The resulting DataFrame should have three columns: columns id_start, id_end, and distance.




![TASK8](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/8791c17f-9be8-419a-9d96-95be7c400933)


![TASK88](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/7506fef2-0758-4800-a094-6c608442cc88)




![task8answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/573450ba-769d-4b0f-b2cf-a1202602e469)


Question 3: Finding IDs within Percentage Threshold
Create a function find_ids_within_ten_percentage_threshold that takes the DataFrame created in Question 2 and a reference value from the id_start column as an integer.

Calculate average distance for the reference value given as an input and return a sorted list of values from id_start column which lie within 10% (including ceiling and floor) of the reference value's average.







 



![TASK9](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/3a91886d-2ca1-44e8-8148-e32216059a2f)


![TASK99](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/93adb789-0f62-495f-a3b7-b3264ae9756d)

![TASK999](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/e6065a66-8be9-4b01-80a2-60a0b91c59f1)

![task9answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/67f37d52-e2f1-49e3-bc27-a770d3519779)

Question 4: Calculate Toll Rate
Create a function calculate_toll_rate that takes the DataFrame created in Question 2 as input and calculates toll rates based on vehicle types.

The resulting DataFrame should add 5 columns to the input DataFrame: moto, car, rv, bus, and truck with their respective rate coefficients. The toll rates should be calculated by multiplying the distance with the given rate coefficients for each vehicle type:

0.8 for moto
1.2 for car
1.5 for rv
2.2 for bus
3.6 for truck


    







![TASK10](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/2febf532-827f-4a4c-827f-383151780c76)




![TASK100](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/7d53f65c-45b9-4ff8-a893-1adb9eee6108)




![task10answer](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/a8dfdcdf-b17f-4533-83bc-04fc475e1232)

Question 5: Calculate Time-Based Toll Rates
Create a function named calculate_time_based_toll_rates that takes the DataFrame created in Question 3 as input and calculates toll rates for different time intervals within a day.

The resulting DataFrame should have these five columns added to the input: start_day, start_time, end_day, and end_time.

start_day, end_day must be strings with day values (from Monday to Sunday in proper case)
start_time and end_time must be of type datetime.time() with the values from time range given below.
Modify the values of vehicle columns according to the following time ranges:

Weekdays (Monday - Friday):

From 00:00:00 to 10:00:00: Apply a discount factor of 0.8
From 10:00:00 to 18:00:00: Apply a discount factor of 1.2
From 18:00:00 to 23:59:59: Apply a discount factor of 0.8
Weekends (Saturday and Sunday):

Apply a constant discount factor of 0.7 for all times.
For each unique (id_start, id_end) pair, cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).


 




![TASK11](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/aee67faa-114f-4249-a976-08ca8200eca0)

    
![TASK111](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/e82c2bd1-e0d5-478f-8fe5-4711702c0aab)


EXCEL 

![Screenshot (36)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/f14760c2-7a62-469b-899f-ba383092ae58)

![Screenshot (37)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/797bd70b-0a95-4231-8995-e4d04468217b)

![Screenshot (38)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/78f132df-86ba-4a45-b796-8ee4910ad3ea)


![Screenshot (39)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/32475f6b-96eb-49d1-afd7-a2dfa3b0eed5)
![Screenshot (40)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/3c9382ad-bf39-4f4e-9ce4-01e3e6aa0144)

![Screenshot (46)](https://github.com/deepaksundaran/mapup-.ai/assets/123062995/07c23617-ab57-4d5e-b0df-3cfed5c2c906)

