from qiskit import QuantumCircuit

target = "10101"
size = len(target)

def build_circuit():
    circuit = QuantumCircuit(size + 1, size)

    circuit.h(range(size))
    circuit.x(size)
    circuit.h(size)

    circuit.barrier()

    for i in range(size):
        if target[i] == '1':
            circuit.cx(i, size)

    circuit.barrier()

    circuit.h(range(size))
    circuit.measure(range(size), range(size))

    return circuit