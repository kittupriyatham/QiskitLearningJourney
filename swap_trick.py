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
    STUDENT TASK: The CNOT Swap Trick
    
    GIVEN:
    - 2 independent qubits (qr[0] and qr[1]). 
    - Below this docstring, I have applied an X gate to qr[0] so its starting state is '1'.
    - qr[1] starts normally at '0'.
    - You are ONLY allowed to use the CNOT gate: `qc.cx()`
    
    REQUIRED:
    - Swap the states of the two qubits! 
    - By the end of your logic, qr[0] must be '0' and qr[1] must be '1'.
    - This is NOT a randomized state. You expect 100% identical outputs.
    - The expected measurement outcome should be exclusively '10' (Since Qiskit prints the 1st index bit on the left, and 0th index on the right).
    
    Write your quantum logic below:
    """
    # GIVEN Setup: Setting qr[0] to 1. DO NOT REMOVE THIS LINE.
    qc.x(qr[1])
    
    # 0 1

    qc.cx(qr[0], qr[1])

    # 0 1
    qc.cx(qr[1], qr[0])

    # 1 1

    qc.cx(qr[0], qr[1])

    # 1 0

    
    # Write your quantum logic below this line:
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
    
    # 1. Initialize
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic 
    core_logic(qc, qr, cr)
    
    # 3. Measure
    qc.measure(qr, cr)
    
    # 4. Run Simulation
    # Since there are no Hadamard gates, there is no randomness. 10 shots is enough.
    run_simulation(simulator, qc, shots=10)
    
    # 5. Save Circuit Image
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
