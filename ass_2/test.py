import math

Q = [1,2,3,4]

print Q

print len(Q)

print Q[0:3-1]

P = [0,2]
Q = [0,4]

print int(math.ceil(math.hypot((abs(P[0] - Q[0])), (abs(P[1] - Q[1])))))
