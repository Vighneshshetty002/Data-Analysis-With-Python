import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    return math.sqrt(variance)

def main():
    # Input: list of numbers
    data = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

    # Calculate mean
    mean = calculate_mean(data)

    # Calculate variance
    variance = calculate_variance(data, mean)

    # Calculate standard deviation
    std_deviation = calculate_standard_deviation(variance)

    # Display results
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")

if __name__ == "__main__":
    main()
