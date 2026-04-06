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
    Define the quantum gates and measurements here.
    """
    # 0. Preparation: Alice prepares a secret payload on qr[0]
    # For example, let's just make it a '1' state for Bob to receive.
    qc.x(qr[0])
    
    # ----------------------------------------------------
    # Add your Teleportation Protocol below this line
    # ----------------------------------------------------


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
    # 3 Qubits: 
    # qr[0] = Alice's Payload Qubit
    # qr[1] = Alice's half of the Bell Pair
    # qr[2] = Bob's half of the Bell Pair
    num_qubits = 3 
    num_cbits = 3  
    
    # 1. Initialize
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic
    core_logic(qc, qr, cr)
    
    # 3. Run Simulation 
    # result_counts = run_simulation(simulator, qc, shots=1024)
    
    # 4. Save Circuit Image
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
