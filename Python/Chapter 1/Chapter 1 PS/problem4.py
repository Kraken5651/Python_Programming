import os

# Print contents of current directory
files = os.listdir('/Games')  # or os.listdir('.')


for file in files:
    print(file)
