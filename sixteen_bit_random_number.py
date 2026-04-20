from quantum_engine import execute_matrix
import cirq

def core_logic_qiskit(qc, qr, cr):
    qc.h(qr)
    qc.measure(qr, cr)

def core_logic_cirq(circuit, qubits):
    circuit.append([cirq.H(q) for q in qubits])
    circuit.append(cirq.measure(*qubits, key='result'))

def core_logic_qsharp():
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Arrays;

    operation CoreLogic() : Result[] {
        use q = Qubit[16];
        for i in 0..15 {
            H(q[i]);
        }
        
        mutable results = [Zero, size = 16];
        for i in 0..15 {
            set results w/= i <- M(q[i]);
        }
        return results;
    }
    """

if __name__ == "__main__":
    execute_matrix(16, core_logic_qiskit, core_logic_cirq, core_logic_qsharp, __file__)
