from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qbraid import QbraidProvider
import os

def initialize(num_qubits, num_cbits=None):
    """
    Initializes the local simulator, Qbraid cloud device, quantum register, classical register, and quantum circuit.
    """
    simulator = AerSimulator()
    
    # Initialize Qbraid device
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
    print(f"\nSaving circuit image to: {filename}")
    try:
        qc.draw('mpl', filename=filename)
    except Exception as e:
        print(f"Warning: Failed to save circuit image drawing. Ensure matplotlib and pylatexenc are installed. Error: {e}")

def run_qiskit_simulator(simulator, qc, shots=1024):
    """
    Runs the circuit on the local Qiskit Aer simulator.
    """
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Qiskit Aer Simulator counts:", counts)
    return counts

def run_qbraid_device(device, qc, shots=1024):
    """
    Runs the circuit on the Qbraid cloud device/simulator.
    """
    if device is None:
        print("Skipping Qbraid execution (device not initialized).")
        return None
        
    counts = device.run(qc, shots=shots).result().measurement_counts
    print("Qbraid Cloud Provider counts :", counts)
    return counts

def main():
    # Number of qubits and classical bits
    num_qubits = 1
    num_cbits = 1
    
    # 1. Initialize
    simulator, qbraid_device, qc, qr, cr = initialize(num_qubits, num_cbits)
    
    # 2. Add Core Logic
    core_logic(qc, qr, cr)
    
    # 3. Run Simulation (Uncomment the one you want to use, or both)
    # run_qiskit_simulator(simulator, qc, shots=1024)
    # run_qbraid_device(qbraid_device, qc, shots=1024)
    
    # 4. Save Circuit Image
    save_circuit_image(qc, __file__)

if __name__ == "__main__":
    main()
