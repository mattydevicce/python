
filename = "p102_triangles.txt"

txt = open(filename)

print "Here's your file %r:" % filename
triangle_coordinates = txt.read()

temp = ''
good_coords = []

#Lets store the data in arrays
for x in triangle_coordinates:
	if (x=="\n"):
		hold = temp.split(",")
		good_coords.append([[hold[0],hold[1]],[hold[2],hold[3]],[hold[4],hold[5]]])
		temp = ''
	else:
		temp += x

# I would like to sore the coorinates in a more readable manner.. doing the 
# same thing as above and storing a list of lists
