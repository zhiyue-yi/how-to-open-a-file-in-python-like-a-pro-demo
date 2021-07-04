import os

file_path = './i-am-a-very-large-file'

if(os.path.isfile(file_path)):
  with open(file_path, 'rb') as f:
    for line in f.readlines():
      print(line)