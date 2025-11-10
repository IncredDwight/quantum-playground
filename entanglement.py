from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# 1. Build the circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])


simulator = Aer.get_backend('aer_simulator')

compiled_circuit = transpile(qc, simulator)

result = simulator.run(compiled_circuit, shots=1024).result()

counts = result.get_counts()
print(counts)
plot_histogram(counts)
