from qiskit import QuantumCircuit

def build_circuit():
    circuit = QuantumCircuit(3, 3)

    circuit.x(0)

    circuit.barrier()

    circuit.h(1)
    circuit.cx(1, 2)

    circuit.barrier()

    circuit.cx(0, 1)
    circuit.h(0)

    circuit.barrier()

    circuit.measure([0, 1], [0, 1])
    circuit.cx(1, 2)
    circuit.cz(0, 2)
    circuit.measure(2, 2)

    return circuit