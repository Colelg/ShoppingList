
sum = 0
items_dictionary = {}
input = open('Grocery List.txt', 'rt')
output = open('Total_Grocery_List.txt', 'wt')
print('Processing list')
print('Your grocery list: \n', file = output)

for line in input:
  (key,val) = line.split(': ')
  items_dictionary[(key)] = val
for i, (key, val) in enumerate(items_dictionary.items()):
  print(key, val, file = output)
  sum += float(val)

print('\nTotal: ' + str(sum), file = output)
print('Output complete')
output.close
