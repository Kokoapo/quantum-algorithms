from qiskit import QuantumCircuit

def build_oracle():
    circuit = QuantumCircuit(2, name='oracle')
    circuit.cz(0, 1)

    circuit.to_gate()
    return circuit

def build_reflection():
    circuit = QuantumCircuit(2, name='reflection')
    circuit.h([0, 1])
    circuit.z([0, 1])
    circuit.cz(0, 1)
    circuit.h([0, 1])

    circuit.to_gate()
    return circuit

def build_circuit():
    circuit = QuantumCircuit(2, 2)

    circuit.h([0, 1])
    circuit.append(build_oracle(), [0, 1])
    circuit.append(build_reflection(), [0, 1])

    circuit.measure([0, 1], [0, 1])
    
    return circuit