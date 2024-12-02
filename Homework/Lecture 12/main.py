# Create a file that will contain 100 lines, each line will contain  20 random  numbers. 
# Read all the file lines and using map function convert the line into integer array.
# Using filter function filter the numbers which are > 40 
# Write the data back to file
# Read the same file as a generetor(use yield to achieve that)
# Create decorator that will measure the function execution time 


import time

def create_numbers_file(filename):
    with open(filename, 'w') as f:
        for i in range(100):  
            line = " ".join(str((num * (i + 3)) % 101 + 1) for num in range(1, 21)) 
            f.write(line + "\n")

def read_and_process_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        processed_lines = []
        for line in lines:
            numbers = list(map(int, line.split()))
            filtered_numbers = list(filter(lambda x: x > 40, numbers))
            processed_lines.append(filtered_numbers)
        return processed_lines

def write_filtered_data_to_file(filename, processed_lines):
    with open(filename, 'w') as f:
        for line in processed_lines:
            f.write(" ".join(str(num) for num in line) + "\n")

def read_file_as_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield list(map(int, line.split())) 

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time
def process_file(filename):
    create_numbers_file(filename)
    processed_lines = read_and_process_file(filename)
    write_filtered_data_to_file(filename, processed_lines)

filename = "numbers.txt"

process_file(filename)

for line in read_file_as_generator(filename):
    print(line)
