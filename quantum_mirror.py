from quantum_engine import execute_matrix
import cirq

def core_logic_qiskit(qc, qr, cr):
    """
    STUDENT TASK: The Quantum Mirror
    """
    # Experiment A (Qubit 0): The "Invisible" X Gate
    qc.h(qr[0])
    qc.x(qr[0])
    qc.h(qr[0])

    # Experiment B (Qubit 1): The "Powerful" Z Gate
    qc.h(qr[1])
    qc.z(qr[1])
    qc.h(qr[1])

    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])

def core_logic_cirq(circuit, qubits):
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.H(qubits[0]))
    
    circuit.append(cirq.H(qubits[1]))
    circuit.append(cirq.Z(qubits[1]))
    circuit.append(cirq.H(qubits[1]))
    
    circuit.append(cirq.measure(*qubits, key='result'))

def core_logic_qsharp():
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation CoreLogic() : Result[] {
        use q = Qubit[2];
        
        H(q[0]);
        X(q[0]);
        H(q[0]);
        
        H(q[1]);
        Z(q[1]);
        H(q[1]);
        
        return [M(q[0]), M(q[1])];
    }
    """

if __name__ == "__main__":
    execute_matrix(2, core_logic_qiskit, core_logic_cirq, core_logic_qsharp, __file__)
