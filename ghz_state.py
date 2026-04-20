from quantum_engine import execute_matrix
import cirq

def core_logic_qiskit(qc, qr, cr):
    """
    STUDENT TASK: The GHZ State (3-Qubit Entanglement)
    """
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.cx(qr[1], qr[2])
    qc.measure(qr, cr)

def core_logic_cirq(circuit, qubits):
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.CNOT(qubits[1], qubits[2]))
    circuit.append(cirq.measure(*qubits, key='result'))

def core_logic_qsharp():
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation CoreLogic() : Result[] {
        use q = Qubit[3];
        H(q[0]);
        CNOT(q[0], q[1]);
        CNOT(q[1], q[2]);
        
        return [M(q[0]), M(q[1]), M(q[2])];
    }
    """

if __name__ == "__main__":
    execute_matrix(3, core_logic_qiskit, core_logic_cirq, core_logic_qsharp, __file__)
