def rgb_hex():
  invalid_msg = "The value entered is invalid!"
  red = int(raw_input("Enter red (R) value: "))
  if (red < 0 or red > 225):
    print ivalid_msg
    return
  green = int(raw_input("Enter green (G) value: "))
  if (green < 0 or green > 225):
    print ivalid_msg
    return
  blue = int(raw_input("Enter blue (B) value: "))
  if (blue < 0 or blue > 225):
    print ivalid_msg
    return
  val = (red << 16) + (green << 8 ) + blue
  print "%s" % (hex(val)[2:]).upper()


def hex_rgb():
  hex_val = raw_input("Enter the color (six hexadeximal deigits): ")
  if len(hex_val) !=6:
    print "Invalid hexidecimal value. Try again"
    return
  else :
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
  

def convert():
  while True:
   option = raw_input(" Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
   if option == '1' :
    print "RGB to HEX..."
    rgb_hex()
  
   elif option == '2':
    print "HEX to RGB..."
    hex_rgb()

   elif option == 'X' or option =='x':
    break

  else :
    print "Error..."
  

convert()
