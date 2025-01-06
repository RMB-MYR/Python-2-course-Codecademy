def median(number_list):
  number_list = sorted(number_list)
  n = len(number_list)
  if n % 2 == 1:
    return number_list[n//2]
  else:
    mid1 = number_list[n//2]
    mid2 = number_list[n//2-1]
    return ((mid1+mid2)/2.0)


  

