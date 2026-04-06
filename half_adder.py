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
    STUDENT TASK: The Quantum Half-Adder
    We are bridging back to classical math to prove that quantum computers can calculate anything!
    
    GIVEN:
    - 3 Qubits acting as a basic binary calculator. 
      - qr[0]: Input A
      - qr[1]: Input B (We will also use this to store the "Sum")
      - qr[2]: Input Carry (Stores the "Carry")
    - Below, I have hardcoded it so A = 1 and B = 1. (We are calculating 1 + 1).
      
    REQUIRED:
    - Write quantum logic to compute the Sum and the Carry. 
    - The "Sum" of binary (A + B) must overwrite qr[1]. Since 1 + 1 = 0 (carry 1), qr[1] should become 0.
    - The "Carry" of (A + B) must overwrite qr[2]. Since we need to carry the 1, qr[2] should become 1.
    - Final Expected Hardware output: qr[2]=1, qr[1]=0, qr[0]=1. (Qiskit prints '101').
    
    NEW TOOL UNLOCKED: The Toffoli Gate (CCX Gate)
    - Syntax: `qc.ccx(control_1, control_2, target)`
    - Rule: It flips the target IF AND ONLY IF both control 1 and control 2 are '1'.
    - Hint: You already know `qc.cx()` acts structurally like an XOR gate. The new `qc.ccx()` acts like an AND gate!
      
    Write your Quantum Calculator below:
    """
    # GIVEN Setup: We want to calculate 1 + 1. Do not remove.
    qc.x(qr[0])
    qc.x(qr[1])

    # 1 1

    qc.ccx(qr[0], qr[1], qr[2])

    # 1 1 1

    qc.cx(qr[0], qr[1])

    # 1 0 1


    
    # Write your logic here:
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
    num_qubits = 3
    num_cbits = 3
    
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    core_logic(qc, qr, cr)
    
    qc.measure(qr, cr)
    
    # 10 shots, as there is no randomness built into this specific circuit.
    run_simulation(simulator, qc, shots=10)
    
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
