import numpy as np

# Basis states
zero = np.array([[1], [0]], dtype=complex)
one = np.array([[0], [1]], dtype=complex)

# Superposition
plus = (zero + one) / np.sqrt(2)

# Print
print("zero =", zero.T)
print("one  =", one.T)
print("plus =", plus.T)

X = np.array([[0, 1], [1, 0]], dtype=complex)
psi = X @ zero
print("After X gate: ", psi.T)