#This program can calculate the areo of diffrent shapes
print "Calculater is starting up..."
option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter the radius of your Circle: [mm]"))
  area = 3.14159*radius*radius
  print "Your Circle has an area of " + str(area)+ "mm2"
elif option == "T":
  base = float(raw_input("Enter the Base of your Triangle: [mm]"))
  height = float(raw_input("Enter the Height of your Triangle: [mm]"))
  area = 0.5*height*base
  print "Your Triangle has an area of " + str(area) + "mm2"
else:
  print "The Information you entered is invalid"

print "The program is now exiting"
