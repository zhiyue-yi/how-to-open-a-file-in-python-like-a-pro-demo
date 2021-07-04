f = open('./i-am-a-very-large-file', 'rb')
for line in f.readlines():
  print(line)
f.close()