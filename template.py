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
    # Example: Apply Hadamard to the first qubit and measure
    # qc.h(qr[0])
    # qc.measure(qr[0], cr[0])
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

def run_simulation(simula tor, qc, shots=1):
    """
    Runs the circuit on the simulator and returns the result counts.
    """
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Measurement counts:", counts)
    return counts

def main():
    # Number of qubits and classical bits
    num_qubits = 1
    num_cbits = 1
    
    # 1. Initialize
    simulator, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic
    core_logic(qc, qr, cr)
    
    # 3. Run Simulation (if you want to measure before saving the circuit you can, or vice versa)
    # result_counts = run_simulation(simulator, qc, shots=1)
    
    # 4. Save Circuit Image
    # Pass __file__ so the image has the same name as this script
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
