from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import os
import matplotlib.pyplot as plt

simulator = AerSimulator()

qr1 = QuantumRegister(1)
cr1 = ClassicalRegister(1)
qc = QuantumCircuit(qr1,cr1)

qc.h(qr1[0])
qc.measure(qr1[0], cr1[0])

name = os.path.splitext(os.path.basename(__file__))[0] + '.png'
print(qc.draw('mpl', filename=name))
# plt.show()

counts = simulator.run(qc, shots=1).result().get_counts()
print(int(list(counts.keys())[0],2))
