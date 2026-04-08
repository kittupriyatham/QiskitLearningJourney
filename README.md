# Qiskit Learning Journey

This repository tracks my progress moving from basic copy-pasting of Qiskit code to actively designing, troubleshooting, and solving quantum logic puzzles using a Problem-Based Learning (Given/Required) approach.

**Core Vision & Architecture:**
A primary intent of this repository is to serve as a universal learning template. The underlying architecture (established in `template.py`) is deliberately designed to allow any quantum circuit written here to be easily toggled between:

- **Local Simulators** (Qiskit Aer)
- **Cloud Quantum Platforms** (Qbraid)
- **Future Integrations** (Azure Quantum Workspaces & AWS Braket)

This structure empowers the developer to write a circuit once and execute it on original quantum computers or simulators strictly based on hardware configuration choices.

## 🟢 Phase 1: Superposition & Single-Qubit Manipulation

### Project 1: 1-Bit Random Number Generator

- **Concept:** True quantum randomness via Superposition.
- **Key Gate:** The Hadamard Gate (`H`).
- **Takeaway:** Using `qc.h()` puts a qubit into a 50/50 state of being 0 or 1 upon measurement.

### Project 2: 16-Bit Random Number Generator

- **Concept:** Scaling quantum systems.
- **Takeaway:** Applying Hadamard gates across multiple qubits to generate large random binary strings.

### Project 3: Shifting Probabilities (Biased Coins)

- **Concept:** Quantum State Rotations.
- **Key Gates:** `Rx`, `Ry`, `Rz`
- **Takeaway:** By applying rotations instead of a standard `H` gate, we successfully shifted the measurement probability from a 50/50 split to a 75/25 split.

---

## 🟡 Phase 2: Multi-Qubit Entanglement

### Project 4: The Bell State (`bell_state.py`)

- **Concept:** Entanglement ("Spooky Action at a Distance").
- **Key Gate:** The Controlled-NOT Gate (`CX`).
- **Takeaway:** By combining an `H` gate with a `CX` gate, we entangled two qubits so their outputs perfectly correlated (`00` or `11`), eliminating the `01` and `10` states entirely.

### Project 5: The GHZ State (`ghz_state.py`)

- **Concept:** Chaining Entanglement.
- **Takeaway:** We proved that we can select ANY qubit as a control or target. By using Q0 to dictate Q1, and then Q1 to dictate Q2, we entangled 3 qubits to perfectly agree (`000` or `111`).

---

## 🟠 Phase 3: Quantum Logic & Architecture

### Project 6: The Universal CNOT Swap Trick (`swap_trick.py`)

- **Concept:** Reversibility and "Blind" Circuit Architecture.
- **The Puzzle:** Swap the states of two qubits using _only_ `CX` gates.
- **Takeaway:** We discovered the iconic 3-gate sequence `cx(0,1) -> cx(1,0) -> cx(0,1)`. We also learned why quantum circuits must be universally architected: since we can't "check" a state halfway through without destroying it, the math must work blindly for _any_ input.

### Project 7: The Entangled Swap (`entangled_swap.py`)

- **Concept:** State Symmetry.
- **The Puzzle:** What happens if we entangle two qubits (Bell State) and then immediately apply the Swap Trick to them?
- **Takeaway:** Tracing the parallel superpositions proved that swapping a perfectly symmetrical system (`00` and `11`) results in the exact same measurable state. The swap changes nothing!

### Project 8: The Quantum Half-Adder (`half_adder.py`)

- **Concept:** Universal Computation (Simulating classical math).
- **Key Gate:** The Toffoli Gate (`CCX`), acting as a quantum `AND` gate.
- **Takeaway:** We built a calculator to compute `1 + 1`. We successfully used `CCX` for the "Carry" and `CX` for the "Sum". We also successfully navigated an "Order of Operations" trap by calculating the Carry _before_ the XOR gate overwrote our inputs!

### Project 9: Superdense Coding (`superdense_coding.py`)

- **Concept:** Quantum Communication Protocols (Sending 2 classical bits using 1 qubit).
- **Key Gates:** `X`, `Z` (for the cipher), and `CX`, `H` (for decoding).
- **Takeaway:** We proved that an entangled Bell pair acts as a shared resource. We can manipulate _only one_ half of the pair to encode a message, and by applying quantum interference (`CX` followed by `H`) before measurement, we can flawlessly decode that hidden superposition back into a 100% deterministic classical state.

---

## 🔜 Up Next

- **Project 10 preview:** _Quantum Teleportation_ - Destroying a qubit in one location to instantly rebuild its exact state in another!
