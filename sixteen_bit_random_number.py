import qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

simulator = AerSimulator()

qr = QuantumRegister(16)
cr = ClassicalRegister(16)
qc = QuantumCircuit(qr, cr)
qc.h(qr)
qc.measure(qr, cr)
counts = simulator.run(qc, shots=1).result().get_counts()
print(int(list(counts.keys())[0],2))

name = input("Enter the name of the file: ")
print(qc.draw('mpl', filename=name))

