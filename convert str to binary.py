s = "ABC"
 
result = ' '.join(format(ord(c), 'b') for c in s)
print(result)       # 1000001 1000010 1000011
