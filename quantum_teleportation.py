from quantum_engine import execute_matrix
import cirq
import math

def core_logic_qiskit(qc, qr, cr):
    """
    STUDENT TASK: Quantum Teleportation
    """
    # 0. Preparation: Alice prepares a secret payload on qr[0]
    qc.x(qr[0])
    
    # ----------------------------------------------------
    # Add your Teleportation Protocol below this line
    # ----------------------------------------------------
    pass

def core_logic_cirq(circuit, qubits):
    """
    Write equivalent Cirq logic here.
    """
    # 0. Preparation: Alice prepares a secret payload on qubits[0]
    circuit.append(cirq.X(qubits[0]))
    pass

def core_logic_qsharp():
    """
    Write equivalent Q# logic here.
    """
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation CoreLogic() : Result[] {
        use q = Qubit[3];
        
        // 0. Preparation: Alice prepares a secret payload on q[0]
        X(q[0]);
        
        // ----------------------------------------------------
        // Add your Teleportation Protocol below this line
        // ----------------------------------------------------
        
        return [M(q[0]), M(q[1]), M(q[2])];
    }
    """

if __name__ == "__main__":
    execute_matrix(num_qubits=3, 
                   logic_qiskit=core_logic_qiskit, 
                   logic_cirq=core_logic_cirq, 
                   logic_qsharp=core_logic_qsharp, 
                   script_file=__file__)
