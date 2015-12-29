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
for i in range(0,len(good_coords)-1):
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

	invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
	u = (dot11 * dot02 - dot01 * dot12) * invDenom
	v = (dot00 * dot12 - dot01 * dot02) * invDenom
	if ((u >= 0) and (v >= 0) and (u + v < 1)):
		total += 1


print total , counter
total = 0
counter = 0
for i in range(0,len(good_coords)-1):
	counter +=1
	A = good_coords[i][0]
	B = good_coords[i][1]
	C = good_coords[i][2]
	P = [0,0]

	denom = ((B[1]-C[1]) * (A[0]-C[0]) + (C[0]-B[0]) * (A[1]-C[1]))

	alpha = float(((B[1] - C[1])*(P[0] - C[0]) + (C[0] - B[0]) * (P[1]-C[1]))/denom)
	beta  = float(((C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1]-C[1]))/denom)
	gamma = 1-alpha-beta

	print alpha,beta,gamma
	if (alpha > 0 and alpha < 1 and beta < 1 and beta > 0):
		total += 1

print total, counter
# try #2


# print good_coords[0]
# print good_coords[0][1][1]
# a = np.array(good_coords[0][0])
# b = np.array(good_coords[0][1])
# print np.cross(a,b)