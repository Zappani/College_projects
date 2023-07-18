import numpy as np

r1 = np.random.rand(5) # [0..1[
print(r1)
print(type(r1))
print(type(r1[0]))
print(np.random.rand(3, 5))

r2 = np.random.randint(1, 10, 90) # menor, maior e qtde
r3 = r2.reshape(3, 30)
print(r2)
print(type(r2))
print(type(r2[0]))
print(r3)

r4 = np.random.randint(5, size=(4, 10)) # matriz 4x10, de [0..4[
print(r4)