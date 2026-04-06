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
    STUDENT TASK: Create a Bell State!
    
    Goal: Entangle two qubits so that their measurement results are always 
    perfectly correlated (either '00' or '11').
    
    Expected outcome when measuring: ~50% chance of '00' and ~50% chance of '11'.
    You should practically never see '01' or '10'.
    
    Hint: You'll need to use what you learned about superposition (Hadamard gate) 
    and combine it with a new multi-qubit gate: the Controlled-NOT (CX) gate.
    - qc.cx(control_qubit, target_qubit)
    
    Write your quantum gates below:
    """
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    pass

def save_circuit_image(qc, script_file):
    """
    Saves the quantum circuit as an image file.
    The filename will be the same as the python script name (e.g., script.py -> script.png).
    """
    filename = os.path.splitext(os.path.basename(script_file))[0] + '.png'
    print(f"Saving circuit image to: {filename}")
    try:
        qc.draw('mpl', filename=filename)
    except Exception as e:
        print(f"Warning: Failed to save circuit image drawing. Ensure matplotlib and pylatexenc are installed. Error: {e}")

def run_simulation(simulator, qc, shots=1):
    """
    Runs the circuit on the simulator and returns the result counts.
    """
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Measurement counts:", counts)
    return counts

def main():
    # We need 2 qubits and 2 classical bits for entangled coins
    num_qubits = 2
    num_cbits = 2
    
    # 1. Initialize
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic (Your task!)
    core_logic(qc, qr, cr)
    
    # 3. Measure the qubits into the classical bits
    # This measures all qubits into the corresponding classical bits
    qc.measure(qr, cr)
    
    # 4. Run Simulation
    # We run the simulation 1000 times (shots) to see the distribution
    run_simulation(simulator, qc, shots=1000)
    
    # 5. Save Circuit Image
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
