def swap_case(s):
  swap = "" 
  for char in s: 
      if char.isupper():
         swap = swap + char.lower() 
      else:
         char.islower() 
         swap = swap + char.upper() 
  return swap
