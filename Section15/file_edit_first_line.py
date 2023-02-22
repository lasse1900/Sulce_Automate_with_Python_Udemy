with open('merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open('merged.csv', 'w') as file:
  file.writelines(content)   # works with lists
  # file.write('ID,AMOUNT,COST\n') # works with strings
  # wipes rest