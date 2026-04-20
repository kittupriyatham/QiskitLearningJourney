from quantum_engine import execute_matrix
import cirq

def core_logic_qiskit(qc, qr, cr):
    """
    STUDENT TASK: Create a Bell State!
    """
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.measure(qr, cr)

def core_logic_cirq(circuit, qubits):
    """ Cirq Implementation of Bell State """
    circuit.append(cirq.H(qubits[0]))
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.measure(*qubits, key='result'))

def core_logic_qsharp():
    """ Q# Implementation of Bell State """
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Arrays;

    operation CoreLogic() : Result[] {
        use q = Qubit[2];
        H(q[0]);
        CNOT(q[0], q[1]);
        
        // Measure and return array of results
        return [M(q[0]), M(q[1])];
    }
    """

if __name__ == "__main__":
    execute_matrix(
        num_qubits=2,
        logic_qiskit=core_logic_qiskit,
        logic_cirq=core_logic_cirq,
        logic_qsharp=core_logic_qsharp,
        script_file=__file__
    )
