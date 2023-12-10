import pandas as pd

def demographic_data_analyzer(data):
    # Load data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Calculate basic statistics
    total_rows = len(df)
    num_columns = len(df.columns)
    unique_genders = df['sex'].unique()
    unique_races = df['race'].unique()
    average_age = df['age'].mean()

    # Count the number of people by gender
    gender_counts = df['sex'].value_counts()

    # Calculate the percentage of each race in the dataset
    race_percentages = df['race'].value_counts(normalize=True) * 100

    # Display results
    print(f"Total number of records: {total_rows}")
    print(f"Number of columns: {num_columns}")
    print(f"Unique genders: {', '.join(unique_genders)}")
    print(f"Unique races: {', '.join(unique_races)}")
    print(f"Average age: {average_age:.2f}")
    print("\nGender distribution:")
    print(gender_counts)
    print("\nRace distribution:")
    print(race_percentages)

# Example usage with dummy data
data = {
    'age': [25, 30, 35, 40, 45],
    'sex': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'race': ['White', 'Black', 'White', 'Asian', 'Black']
}

demographic_data_analyzer(data)
