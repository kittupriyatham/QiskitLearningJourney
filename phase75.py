from quantum_engine import execute_matrix
import cirq
import math

def core_logic_qiskit(qc, qr, cr):
    qc.rx(math.pi/4, qr[0])
    qc.measure(qr, cr)

def core_logic_cirq(circuit, qubits):
    circuit.append(cirq.rx(math.pi/4)(qubits[0]))
    circuit.append(cirq.measure(*qubits, key='result'))

def core_logic_qsharp():
    return """
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;

    operation CoreLogic() : Result[] {
        use q = Qubit[1];
        Rx(PI() / 4.0, q[0]);
        
        return [M(q[0])];
    }
    """

if __name__ == "__main__":
    execute_matrix(1, core_logic_qiskit, core_logic_cirq, core_logic_qsharp, __file__)
