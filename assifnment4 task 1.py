try:
    with open('sample.txt', 'r') as f:
        for i, line in enumerate(f, start=1):
            print(f"Line {i}: {line.rstrip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")