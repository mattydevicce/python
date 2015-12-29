import numpy as np

filename = "p102_triangles.txt"

txt = open(filename)

triangle_coordinates = txt.read()

temp = ''
good_coords = []

#Lets store the data in arrays
for x in triangle_coordinates:
	if (x=="\n"):
		hold = temp.split(",")
		good_coords.append([[int(hold[0]),int(hold[1])],[int(hold[2]),int(hold[3])],[int(hold[4]),int(hold[5])]])
		temp = ''
	else:
		temp += x


# Barycentric Technique
total = 0
counter = 0
for i in range(0,len(good_coords)):
	counter +=1
	A = np.array(good_coords[i][0])
	B = np.array(good_coords[i][1])
	C = np.array(good_coords[i][2])
	P = np.array([0,0])

	v0 = [C[0]-A[0], C[1]-A[1]]
	v1 = [B[0]-A[0], B[1]-A[1]]
	v2 = [P[0]-A[0], P[1]-A[1]]
	dot00 = np.dot(v0, v0)
	dot01 = np.dot(v0, v1)
	dot02 = np.dot(v0, v2)
	dot11 = np.dot(v1, v1)
	dot12 = np.dot(v1, v2)
	u = (dot11 * dot02 - dot01 * dot12) / (dot00 * dot11 - dot01 * dot01)
	v = (dot00 * dot12 - dot01 * dot02) / (dot00 * dot11 - dot01 * dot01)
	if ((u >= 0) and (v >= 0) and (u + v < 1)):
		total += 1

print total , counter


total = 0
counter = 0

def SameSide(p1, p2, a, b):
	
	cp1 = np.cross([b[0]-a[0],b[1],a[1]],[p1[0]-a[0],p1[1]-a[1]])
	cp2 = np.cross([b[0]-a[0],b[1],a[1]],[p2[0]-a[0],p2[1]-a[1]])

	if np.dot(cp1, cp2) >= 0:
		return True

for i in range(0,len(good_coords)):
	counter +=1
	points = good_coords[i]
	a = points[0]
	b = points[1]
	c = points[2]
	p = [0,0]
	if (SameSide(p,a, b,c) and SameSide(p,b, a,c) and SameSide(p,c, a,b)):
		total += 1
	

print total, counter
# try #2


# print good_coords[0]
# print good_coords[0][1][1]
# a = np.array(good_coords[0][0])
# b = np.array(good_coords[0][1])
# print np.cross(a,b)