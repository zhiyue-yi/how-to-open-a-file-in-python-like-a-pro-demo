import os

file_path = './i-am-a-very-large-file'

if(os.path.isfile(file_path)):
  f = open(file_path, 'rb')
  for line in f.readlines():
    print(line)
  f.close()