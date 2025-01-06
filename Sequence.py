#this code counts the items in a sequence 
def count(sequence, item):
  sum_item = 0
  for i in sequence:
    if i == item:
      sum_item = sum_item + 1
  return sum_item
