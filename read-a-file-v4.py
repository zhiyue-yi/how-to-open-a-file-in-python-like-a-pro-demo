import os

def read_file(f_path):
  BLOCK_SIZE = 1024

  if(os.path.isfile(f_path)):
    with open(file_path, 'rb') as f:
      while True:
        block = f.read(BLOCK_SIZE)
        if block:
          yield block
        else:
          return

file_path = './i-am-a-very-large-file'

for line in read_file(file_path):
  print(line)