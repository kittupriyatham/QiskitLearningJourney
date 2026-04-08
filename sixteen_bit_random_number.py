from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qbraid import QbraidProvider
import os

def initialize(num_qubits, num_cbits=None):
    simulator = AerSimulator()
    try:
        provider = QbraidProvider()
        device = provider.get_device("qbraid:qbraid:sim:qir-sv")
    except Exception as e:
        print(f"Warning: Failed to initialize Qbraid Provider: {e}")
        device = None
    if num_cbits is None:
        num_cbits = num_qubits
    qr = QuantumRegister(num_qubits)
    cr = ClassicalRegister(num_cbits)
    qc = QuantumCircuit(qr, cr)
    return simulator, device, qc, qr, cr

def core_logic(qc, qr, cr):
    qc.h(qr)
    qc.measure(qr, cr)

def save_circuit_image(qc, script_file):
    filename = os.path.splitext(os.path.basename(script_file))[0] + '.png'
    print(f"\nSaving circuit image to: {filename}")
    try:
        qc.draw('mpl', filename=filename)
    except Exception as e:
        print(f"Warning: Failed to save circuit image drawing. Error: {e}")

def run_qiskit_simulator(simulator, qc, shots=1024):
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Qiskit Aer Simulator counts:", counts)
    return counts

def run_qbraid_device(device, qc, shots=1024):
    if device is None:
        print("Skipping Qbraid execution (device not initialized).")
        return None
    counts = device.run(qc, shots=shots).result().measurement_counts
    print("Qbraid Cloud Provider counts :", counts)
    return counts

def main():
    num_qubits = 16
    num_cbits = 16
    
    simulator, qbraid_device, qc, qr, cr = initialize(num_qubits, num_cbits)
    core_logic(qc, qr, cr)
    
    counts = run_qiskit_simulator(simulator, qc, shots=1)
    if counts:
        print("Generated 16-bit Int:", int(list(counts.keys())[0], 2))
    
    # run_qbraid_device(qbraid_device, qc, shots=1)
    
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
