import os

size = 1024*1024*1024*4 # 4GB 

with open('i-am-a-very-large-file', "wb") as f:
  f.write(os.urandom(size))
