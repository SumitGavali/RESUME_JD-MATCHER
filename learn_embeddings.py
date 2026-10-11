import numpy as np


# A 3D vector — a point in space
v1 = np.array([1.0, 2.0, 3.0])
v2 = np.array([2.0, 4.0, 6.0])   # same direction as v1, 2x length

print("v1:", v1, "|v1|:", np.linalg.norm(v1))
print("v2:", v2, "|v2|:", np.linalg.norm(v2))

def cosine_sim(a,b):
    dot=np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot/(norm_a*norm_b)

print(cosine_sim(v1,v2))
print(cosine_sim(np.array([1,0,0]), np.array([0,1,0]))) #this is perpendicular
print(cosine_sim(np.array([1,0,0]), np.array([-1,0,0])))