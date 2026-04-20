import os
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qbraid import QbraidProvider
import azure.quantum.qiskit
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace
from azure.identity import ClientSecretCredential
import azure.quantum.cirq as az_cirq
import qsharp
import cirq
from dotenv import load_dotenv

# Load standard .env configuration
load_dotenv()


# ==========================================
# 1. INITIALIZATION BLOCKS
# ==========================================
def initialize_qiskit(num_qubits, num_cbits=None):
    """ Initializes Qiskit QuantumRegister, ClassicalRegister, and QuantumCircuit. """
    if num_cbits is None:
        num_cbits = num_qubits
    qr = QuantumRegister(num_qubits)
    cr = ClassicalRegister(num_cbits)
    qc = QuantumCircuit(qr, cr)
    return qc, qr, cr

def initialize_cirq(num_qubits):
    """ Initializes Cirq Qubits and Circuit. """
    qubits = [cirq.LineQubit(i) for i in range(num_qubits)]
    circuit = cirq.Circuit()
    return circuit, qubits
    
def initialize_qsharp():
    """ Initializes local qsharp python interop environment. """
    qsharp.init(target_profile=qsharp.TargetProfile.Base, trace_circuit=True)


# ==========================================
# 2. UTILITIES
# ==========================================
def save_quantum_visualization(platform, sdk, quantum_obj, script_file):
    base_name = os.path.splitext(os.path.basename(script_file))[0]
    
    print(f"\nSaving circuit architecture...")
    
    # Platform Support Check
    if platform == "aer" and sdk != "qiskit":
        return
        
    if platform == "qbraid" and (sdk != "qiskit" and sdk != "cirq"):
        return
        
    # QISKIT
    if sdk == "qiskit":
        filename = f"{base_name}_{platform}_qiskit.png"
        try:
            quantum_obj.draw('mpl', filename=filename)
            print(f"Saved Qiskit circuit to {filename}")
        except Exception as e:
            print(f"Warning: Failed to save Qiskit image. Error: {e}")
            
    # CIRQ
    elif sdk == "cirq":
        filename = f"{base_name}_{platform}_cirq.svg"
        try:
            import cirq.contrib.svg
            svg_text = cirq.contrib.svg.circuit_to_svg(quantum_obj)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(svg_text)
            print(f"Saved Cirq circuit SVG to {filename}")
        except Exception as e:
            print(f"Warning: Failed to save Cirq SVG. Error: {e}")
            
    # Q# 
    elif sdk == "qsharp" or sdk == "q#":
        filename = f"{base_name}_{platform}_qsharp.png"
        try:
            if isinstance(quantum_obj, tuple) and len(quantum_obj)>1:
                svg_data = quantum_obj[1] 
            else:
                svg_data = qsharp.dump_circuit()

            if svg_data:
                svg_str = str(svg_data)
                if len(svg_str.strip())>0:
                    import matplotlib.pyplot as plt
                    fig = plt.figure(figsize=(10, 4))
                    plt.axis('off')
                    fig.text(0.1, 0.5, svg_str, fontfamily='monospace', fontsize=14, va='center')
                    plt.savefig(filename, bbox_inches='tight', facecolor='white')
                    plt.close(fig)
                    print(f"Saved Q# PNG circuit to {filename}")
                else:
                    print("Warning: Q# circuit string was empty")
            else:
                print("Warning: dump_circuit() returned None.")
        except Exception as e:
            print(f"Warning: Failed to save Q# PNG. Error: {e}")

# ==========================================
# 3. SKINNY EXECUTION RUNNERS
# ==========================================
def run_aer_qiskit(qc, shots=1024):
    simulator = AerSimulator()
    counts = simulator.run(qc, shots=shots).result().get_counts()
    print("Local Qiskit Aer Simulator counts:", counts)
    return counts

def run_local_cirq(circuit, shots=1024):
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=shots)
    keys = list(circuit.all_measurement_key_names())
    counts = result.histogram(key=keys[0]) if keys else {}
    print("Local Cirq Simulator Counts:", counts)
    return counts

def run_qbraid_qiskit(device_id, qc, shots=1024):
    device = QbraidProvider().get_device(device_id)
    job = device.run(qc, shots=shots)
    job.wait_for_final_state()
    try:
        counts = job.result().measurement_counts
        print("Qbraid Qiskit Counts:", counts)
        return counts
    except Exception as e:
        print(f"Error with qBraid Qiskit Job payload. Status: {job.status()} | Details: {e}")
        return {}

def run_qbraid_cirq(device_id, circuit, shots=1024):
    if device_id == "qbraid:qbraid:sim:qir-sv":
        print("Notice: 'qir-sv' qBraid payload extraction for Cirq is currently broken. Falling back to local cirq.Simulator()")
        return run_local_cirq(circuit, shots)
        
    device = QbraidProvider().get_device(device_id)
    job = device.run(circuit, shots=shots)
    job.wait_for_final_state()
    try:
        counts = job.result().measurement_counts
        print("Qbraid Cirq Counts:", counts)
        return counts
    except Exception as e:
        print(f"Error with qBraid Cirq Job payload. Status: {job.status()} | Details: {e}")
        return {}

def run_azure_qiskit(workspace, device_id, qc, shots=1024):
    provider = AzureQuantumProvider(workspace=workspace)
    backend = provider.get_backend(device_id)
    result = backend.run(qc, shots=shots).result()
    counts = result.get_counts(qc)
    print("Azure Qiskit Counts:", counts)
    return counts

def run_azure_cirq(workspace, device_id, circuit, shots=1024):
    service = az_cirq.AzureQuantumService(workspace=workspace)
    result = service.run(circuit, repetitions=shots, target=device_id)
    keys = list(circuit.all_measurement_key_names())
    
    if keys:
        counts = result.histogram(key=keys[0])
        probs = {str(state): count / shots for state, count in counts.items()}
    else:
        probs = {}
        
    print("Azure Cirq Probabilities:", probs)
    return probs

def run_azure_qsharp(workspace, device_id, qs_data, shots=1024):
    print("Compiling and submitting Q# script to Azure...")
    if isinstance(qs_data, tuple):
        qs_code = qs_data[0]
    else:
        qs_code = qs_data
    qsharp.eval(qs_code)
    executable_program = qsharp.compile("CoreLogic()")
    target = workspace.get_targets(device_id)
    print(f"Submitting job to {target}...")
    job = target.submit(executable_program, name="Template_Qsharp_Run", shots=shots)
    print(f"Job ID: {job.id}")
    print("Waiting for results (this may take a moment)...")
    results = job.get_results()
    print("Azure Q# Results:", results)
    return results


# ==========================================
# 4. CENTRAL EXECUTION AGGREGATOR
# ==========================================
def execute_quantum_run(sdk, platform, qc_or_str, workspace=None, device_id="default", shots=1024):
    if platform == "aer":
        if sdk == "qiskit":
            return run_aer_qiskit(qc_or_str, shots)
        elif sdk == "cirq":
            return run_local_cirq(qc_or_str, shots)
        else:
            print(f"Notice: Local Simulator does not natively support {sdk}.")
            
    elif platform == "qbraid":
        target = device_id if device_id != "default" else "qbraid:qbraid:sim:qir-sv"
        if sdk == "qiskit": return run_qbraid_qiskit(target, qc_or_str, shots)
        elif sdk == "cirq": return run_qbraid_cirq(target, qc_or_str, shots)
        else: print(f"Notice: QBraid does not support {sdk} in this template.")
            
    elif platform == "azure":
        target = device_id if device_id != "default" else "ionq.simulator"
        if sdk == "qiskit": return run_azure_qiskit(workspace, target, qc_or_str, shots)
        elif sdk == "cirq": return run_azure_cirq(workspace, target, qc_or_str, shots)
        elif sdk == "qsharp" or sdk == "q#": return run_azure_qsharp(workspace, target, qc_or_str, shots)
        
    else:
        print(f"Unknown Platform Selected: {platform}")


# ==========================================
# 5. MATRIX EXECUTOR
# ==========================================
def execute_matrix(num_qubits, logic_qiskit, logic_cirq, logic_qsharp, script_file, num_cbits=None):
    if num_cbits is None:
        num_cbits = num_qubits
        
    # # --- GLOBAL TOGGLES ---
    SDK = ['qsharp', 'cirq', 'qiskit']
    PLATFORM = ['azure', 'qbraid', 'aer']
    
    for i in range(len(PLATFORM)):
        for j in range(i, len(SDK)):
            print(f"\n==========================================")
            print(f"RUNNING: [{PLATFORM[i].upper()} - {SDK[j].upper()}]")
            print(f"==========================================")
            current_sdk = SDK[j]
            current_platform = PLATFORM[i]
            
            # 1. Initialize & Build Core Logic Based on SDK
            circuit_object = None
            try:
                if current_sdk == "qiskit":
                    qc, qr, cr = initialize_qiskit(num_qubits, num_cbits)
                    logic_qiskit(qc, qr, cr)
                    circuit_object = qc
                    
                elif current_sdk == "cirq":
                    circuit, qubits = initialize_cirq(num_qubits)
                    logic_cirq(circuit, qubits)
                    circuit_object = circuit
                    
                elif current_sdk in ["qsharp", "q#"]:
                    initialize_qsharp()
                    qs_code = logic_qsharp()
                    qsharp.eval(qs_code) # Evaluate immediately so it's loaded globally
                    try:
                        # Generate static circuit diagram from the actual operation entry point
                        circ = qsharp.circuit("CoreLogic()")
                        qsharp_svg = str(circ)
                    except Exception as e:
                        qsharp_svg = f"Error generating circuit: {e}"
                    circuit_object = (qs_code, qsharp_svg)
            except Exception as e:
                 print(f"Failed to construct circuit for {current_sdk}: {e}")
                 continue

            if not circuit_object:
                continue

            # 2. Configure Azure Workspace (if applicable)
            active_workspace = None
            if current_platform == "azure":
                credential = ClientSecretCredential(
                    tenant_id=os.getenv("AZ_TENANT_ID"),
                    client_id=os.getenv("AZ_CLIENT_ID"),
                    client_secret=os.getenv("AZ_CLIENT_SECRET")
                )
                active_workspace = Workspace(
                    subscription_id=os.getenv("AZ_SUB_ID"),
                    resource_group=os.getenv("AZ_RG"),
                    name=os.getenv("AZ_WORKSPACE"),
                    location=os.getenv("AZ_LOCATION"),
                    credential=credential
                )

            # 3. Execute via the Aggregator Router
            execute_quantum_run(current_sdk, current_platform, circuit_object, workspace=active_workspace, shots=1024)
            
            # 4. Save Circuit Architecture
            save_quantum_visualization(current_platform, current_sdk, circuit_object, script_file)
