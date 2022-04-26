# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def convert_string_upper(my_string):
  my_string = ""
  converted_string = my_string.upper()
  return converted_string

def test():
  my_string = input(str("Full name: "))
  converted_string = my_string.upper()
  print(converted_string)

# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
  test()
