from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import os, sys, teleportation, bv, deustch, grover

CIRCUIT_PATH = 'circuits'
HISTOGRAM_PATH = 'histograms'

def print_error_and_exit():
    print("Failed to run the script.")
    print("\tUsage: python main.py <algorithm> <shots>")
    print("Available algorithms:")
    print("\t1 - Teleportation")
    print("\t2 - Bernstein-Vazirani")
    print("\t3 - Deustch")
    print("\t4 - Grover's Search")
    print("\t5 - Shor's Algorithm")
    sys.exit(1)

def check_arguments():
    if not sys.argv[1] or not sys.argv[2]:
        print_error_and_exit()
    
    try: 
        alg = int(sys.argv[1])
        shots = int(sys.argv[2])
    except ValueError:
        print_error_and_exit()

    if alg not in [1, 2, 3, 4, 5] or shots <= 0:
        print_error_and_exit()

    return alg, shots

if __name__ == "__main__":
    alg, shots = check_arguments()

    match alg:
        case 1:
            circuit = teleportation.build_circuit()
            filename = 'teleportation.png'
        case 2:
            circuit = bv.build_circuit()
            filename = 'bernstein_vazirani.png'
        case 3:
            circuit = deustch.build_circuit()
            filename = 'deustch.png'
        case 4:
            circuit = grover.build_circuit()
            filename = 'grover.png'
        case 5:
            pass

    circuit.draw(output='mpl', filename=os.path.join(CIRCUIT_PATH, filename))

    backend = AerSimulator()
    transpiled_circuit = transpile(circuit, backend)

    job = backend.run(transpiled_circuit, shots=shots)
    result = job.result()
    counts = result.get_counts(circuit)

    print(f"Measurement counts: {counts}")
    plot_histogram(counts, filename=os.path.join(HISTOGRAM_PATH, filename))