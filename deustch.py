from qiskit import QuantumCircuit

def build_circuit():
    circuit = QuantumCircuit(2, 1)
    
    circuit.h(0)
    circuit.x(1)
    circuit.h(1)

    circuit.barrier()

    circuit.cx(0, 1)
    circuit.h(0)
    circuit.measure(0, 0)

    return circuit
