# bitwise_operations.py
import sys

# Input Validation: Retrieves the values from user input (either from the form or URL) and validates them.
def validate_input(input_str):
    try:
        string_values = input_str.split(',')
        string_values = [value.strip() for value in string_values]
        numbers = []
        for value in string_values:
            if value:
                number = int(value)
                numbers.append(number)
            else:
                print("Error: Input must contain integers separated by commas.")
                sys.exit(1)
        return numbers
    except ValueError:
        print("Error: Input must contain integers separated by commas and threshold.")
        sys.exit(1)

# Calculate the AND, OR, and XOR of all integers in the list.Output the results of each operation.
def perform_bitwise_operations(numbers):
    and_result = numbers[0]
    or_result = numbers[0]
    xor_result = numbers[0]
    
    for num in numbers[1:]:
        and_result &= num
        or_result |= num
        xor_result ^= num
    
    return and_result, or_result, xor_result

# Use a loop to filter and display all numbers greater than a user-specified threshold.
def filter_numbers(numbers, threshold):
    filtered_results = []
    for num in numbers:
        if num > threshold:
            filtered_results.append(num)
    return filtered_results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 bitwise_operations.py <comma-separated-integers> <threshold>")
        sys.exit(1)
    
    input_str = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 0  # Default threshold is 0
    
    numbers = validate_input(input_str)
    
    and_result, or_result, xor_result = perform_bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)
    
    print(f"<p>Input numbers: {numbers}</p>")
    print(f"<p>Threshold: {threshold}</p>")
    print(f"<p>Bitwise AND: {and_result}</p>")
    print(f"<p>Bitwise OR: {or_result}</p>")
    print(f"<p>Bitwise XOR: {xor_result}</p>")
    print(f"<p>Numbers greater than threshold: {filtered_numbers}</p>")

if __name__ == "__main__":
    main()
