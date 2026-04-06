from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import os

def initialize(num_qubits, num_cbits=None):
    simulator = AerSimulator()
    if num_cbits is None:
        num_cbits = num_qubits
    qr = QuantumRegister(num_qubits)
    cr = ClassicalRegister(num_cbits)
    qc = QuantumCircuit(qr, cr)
    return simulator, qc, qr, cr

def core_logic(qc, qr, cr):
    """
    STUDENT TASK: The Entangled Swap
    
    GIVEN:
    - 2 independent qubits starting at '0'.
    
    REQUIRED:
    - Step 1: Create a standard Bell State (entanglement) using 2 gates.
    - Step 2: Swap the two qubits using your 3-gate Swap Trick.
    
    Write your 5 quantum gates below, and see what happens when you run it!
    """
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])

    qc.cx(qr[0], qr[1])
    qc.cx(qr[1], qr[0])
    qc.cx(qr[0], qr[1])
    pass

def save_circuit_image(qc, script_file):
    filename = os.path.splitext(os.path.basename(script_file))[0] + '.png'
    print(f"Saving circuit image to: {filename}")
    try:
        qc.draw('mpl', filename=filename)
    except Exception as e:
        print(f"Warning: Failed to save circuit image drawing. Error: {e}")

def run_simulation(simulator, qc, shots=1):
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Measurement counts:", counts)
    return counts

def main():
    num_qubits = 2
    num_cbits = 2
    
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    core_logic(qc, qr, cr)
    
    qc.measure(qr, cr)
    
    # Using 1000 shots so we can clearly see the probability distribution
    run_simulation(simulator, qc, shots=1000)
    
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
