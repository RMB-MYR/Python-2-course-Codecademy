def purify(number_list):
  
  new_list = []
  for i in number_list:
    if i % 2 == 0:
      new_list.append(i)
  return new_list

    
