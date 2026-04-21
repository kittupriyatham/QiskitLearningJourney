# Universal Quantum Learning Journey

This repository tracks my progress moving from basic coding tutorials into aggressively designing, troubleshooting, and solving quantum logic puzzles. It strictly utilizes a Problem-Based Learning (Given/Required) approach to master quantum mechanics across the entire global technology stack.

**Core Vision & The Universal Architecture:**
The defining feature of this repository is its totally hardware-agnostic, multi-framework design. The core engine (`quantum_engine.py`) serves as a universal execution matrix.

For every single assignment in this journey, the quantum circuit is natively authored in three different global SDK formats:
1. **Qiskit** (IBM)
2. **Cirq** (Google)
3. **Q#** (Microsoft)

The engine automatically takes those three native frameworks and routes them to execute securely and synchronously across:
- **Local Framework Simulators** (AerSimulator, cirq.Simulator)
- **Azure Quantum Workspaces** (Executing natively against IonQ Trapped Ions and Azure cloud capabilities natively interpreting QIR payloads)
- **qBraid Environments** (AWS Braket execution pathways routing to alternative QPU topologies)

This structure empowers the developer to write a protocol strictly once natively, and effortlessly observe its matrix execution cleanly across the dominant physics and software methodologies of the entire quantum ecosystem simultaneously.

**(Note: To test the execution matrix locally, ensure you deploy a `.env` file containing your Azure Quantum credentials to natively interface with `quantum_engine.py`.)**

---

## 🟢 Phase 1: Superposition & Single-Qubit Manipulation

### Project 1: 1-Bit Random Number Generator (`assignment_0_hello_quantum.py`)
- **Concept:** True quantum randomness via Superposition.
- **Key Gate:** The Hadamard Gate (`H`).
- **Takeaway:** Using an `H` gate puts a qubit into a 50/50 state of being 0 or 1 upon measurement.

### Project 2: 16-Bit Random Number Generator (`sixteen_bit_random_number.py`)
- **Concept:** Scaling quantum systems.
- **Takeaway:** Applying Hadamard gates across multiple qubits natively via loops to generate large random binary strings.

### Project 3: Shifting Probabilities (Biased Coins) (`phase75.py`)
- **Concept:** Quantum State Rotations.
- **Key Gates:** `Rx`, `Ry`, `Rz`
- **Takeaway:** By applying angular rotations (`Rx` over `pi/4`) instead of a standard `H` gate, we successfully shifted the measurement probability mathematically from a 50/50 split to a 75/25 split.

---

## 🟡 Phase 2: Multi-Qubit Entanglement

### Project 4: The Bell State (`bell_state.py`)
- **Concept:** Entanglement ("Spooky Action at a Distance").
- **Key Gate:** The Controlled-NOT Gate (`CX` / `CNOT`).
- **Takeaway:** By combining an `H` gate with a `CX` gate, we entangled two qubits so their outputs perfectly correlated (`00` or `11`), eliminating the `01` and `10` states entirely.

### Project 5: The GHZ State (`ghz_state.py`)
- **Concept:** Chaining Entanglement.
- **Takeaway:** We proved that we can select ANY qubit as a control or target. By using Q0 to dictate Q1, and then Q1 to dictate Q2, we entangled 3 qubits to perfectly agree (`000` or `111`).

---

## 🟠 Phase 3: Quantum Logic & Architecture

### Project 6: The Universal CNOT Swap Trick (`swap_trick.py`)
- **Concept:** Reversibility and "Blind" Circuit Architecture.
- **The Puzzle:** Swap the states of two qubits using *only* `CX` gates.
- **Takeaway:** We discovered the iconic 3-gate sequence `cx(0,1) -> cx(1,0) -> cx(0,1)`. We also learned why quantum circuits must be universally architected: since we can't "check" a state halfway through without destroying it, the math must work blindly for *any* input.

### Project 7: The Entangled Swap (`entangled_swap.py`)
- **Concept:** State Symmetry.
- **The Puzzle:** What happens if we entangle two qubits (Bell State) and then immediately apply the Swap Trick to them?
- **Takeaway:** Tracing the parallel superpositions proved that swapping a perfectly symmetrical system (`00` and `11`) results in the exact same measurable state. The swap mathematically changes nothing!

### Project 8: The Quantum Half-Adder (`half_adder.py`)
- **Concept:** Universal Computation (Simulating classical math).
- **Key Gate:** The Toffoli Gate (`CCX` / `CCNOT`), acting as a quantum `AND` gate.
- **Takeaway:** We built a calculator to compute `1 + 1`. We successfully used `CCX` for the "Carry" and `CX` for the "Sum". We also successfully navigated an "Order of Operations" trap by calculating the Carry *before* the XOR gate overwrote our inputs!

---

## 🔴 Phase 4: Core Fundamentals & Protocols

### Project 9: Superdense Coding (`superdense_coding.py`)
- **Concept:** Quantum Communication Protocols (Sending 2 classical bits using exactly 1 qubit).
- **Key Gates:** `X`, `Z` (for the cipher), and `CX`, `H` (for decoding).
- **Takeaway:** We proved that an entangled Bell pair acts as a shared resource. We can manipulate *only one* half of the pair to encode a message, and by applying quantum interference (`CX` followed by `H`) before measurement, we can flawlessly decode that hidden superposition back into a 100% deterministic classical state across all three compiler suites.

---

## 🔜 Up Next: Phase 5

- **Project 10 preview:** *Quantum Teleportation* - Destroying a qubit mathematically in one physical location to instantly reconstruct its exact state parameter in another using distributed entanglement!
