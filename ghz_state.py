from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import os

def initialize(num_qubits, num_cbits=None):
    """
    Initializes the simulator, quantum register, classical register, and quantum circuit.
    """
    simulator = AerSimulator()
    if num_cbits is None:
        num_cbits = num_qubits
        
    qr = QuantumRegister(num_qubits)
    cr = ClassicalRegister(num_cbits)
    qc = QuantumCircuit(qr, cr)
    
    return simulator, qc, qr, cr

def core_logic(qc, qr, cr):
    """
    STUDENT TASK: The GHZ State (3-Qubit Entanglement)

    GIVEN: 
    - 3 independent qubits (qr[0], qr[1], qr[2]), all starting in state |0>.
    - Access to the gates you've learned so far (H, CX, etc.).
    
    REQUIRED: 
    - Provide the quantum logic to entangle all 3 qubits perfectly.
    - Expected measurement outcome: ~ 50% '000' and ~ 50% '111'. 
    - You must guarantee that no mixed states (like '001', '101', etc.) appear.
    
    Write your quantum logic below:
    """

    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.cx(qr[1], qr[2])
    pass

def save_circuit_image(qc, script_file):
    """
    Saves the quantum circuit as an image file.
    """
    filename = os.path.splitext(os.path.basename(script_file))[0] + '.png'
    print(f"Saving circuit image to: {filename}")
    try:
        qc.draw('mpl', filename=filename)
    except Exception as e:
        print(f"Warning: Failed to save circuit image drawing. Error: {e}")

def run_simulation(simulator, qc, shots=1):
    """
    Runs the circuit on the simulator and returns the result counts.
    """
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Measurement counts:", counts)
    return counts

def main():
    # We now step up to 3 qubits!
    num_qubits = 3
    num_cbits = 3
    
    # 1. Initialize
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic (Your task!)
    core_logic(qc, qr, cr)
    
    # 3. Measure the qubits into the classical bits
    qc.measure(qr, cr)
    
    # 4. Run Simulation
    run_simulation(simulator, qc, shots=1000)
    
    # 5. Save Circuit Image
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
