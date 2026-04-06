import math
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

simulator = AerSimulator()

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)
qc.rx(math.pi/4, qr)
qc.measure(qr, cr)
counts = simulator.run(qc).result().get_counts()
# print(int(list(counts.keys())[0],2))
print(counts)
name = input("Enter the name of the file: ")
print(qc.draw('mpl', filename=name))

