_array = [72, 97, 112, 112, 121, 32, 66, 105, 114, 116, 104, 100, 97, 121]

import time

# Function to print each character from the ASCII array every second
def print_chars_every_second(ascii_array):
    for ascii_value in ascii_array:
        print(chr(ascii_value), end="", flush=True)
        time.sleep(1)

# Call the function with the ASCII array
print_chars_every_second(_array)
