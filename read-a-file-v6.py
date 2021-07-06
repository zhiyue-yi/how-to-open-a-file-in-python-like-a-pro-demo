import sys
import io

file_path = './i-am-a-file'

with open(file_path, 'rb') as f:
    fi = io.FileIO(f.fileno())
    fb = io.BufferedReader(fi)

    while True:
        block = fb.read(20)
        if block:
            print(block)
        else:
            break
