
file_path = './i-am-a-very-large-file'

with open(file_path, 'rb') as file:
  for line in file: print(line)