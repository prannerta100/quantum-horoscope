import numpy as np
from qiskit import *
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy

def do_sum(num1,num2):
    return num1+num2

def QC_Sim1():
    # Create a Quantum Circuit acting on a quantum register of three qubits
    circ = QuantumCircuit(1)
    # Add a H gate on qubit 0, putting this qubit in superposition.
    circ.h(0)
    meas = QuantumCircuit(1, 1)
    meas.barrier(range(1))
    # map the quantum measurement to the classical bits
    meas.measure(range(1),range(1))
    # The Qiskit circuit object supports composition using
    # the addition operator.
    qc = circ+meas
    #drawing the circuit
    qc.draw()
    #from qiskit import IBMQ
    IBMQ.save_account('####') #token hidden
    IBMQ.load_account()
    IBMQ.providers()
    provider = IBMQ.get_provider(group='open')
    small_devices = provider.backends(filters=lambda x: x.configuration().n_qubits >= 1
                                   and not x.configuration().simulator)

    provider.backends()
    backend = least_busy(small_devices)
    #from qiskit.tools.monitor import job_monitor
    job_exp = execute(qc, backend=backend)
    job_monitor(job_exp)
    result_exp = job_exp.result()
    counts_exp = result_exp.get_counts(qc)
    return counts_exp

#QC_Sim2() not of real use
def QC_Sim2():
    # Create a Quantum Circuit acting on a quantum register of three qubits
    circ = QuantumCircuit(3)
    # Add a H gate on qubit 0, putting this qubit in superposition.
    circ.h(0)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state.
    circ.cx(0, 1)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
    # the qubits in a GHZ state.
    circ.cx(0, 2)
    # Import Aer
    # Run the quantum circuit on a statevector simulator backend
    backend = Aer.get_backend('statevector_simulator')
    job = execute(circ, backend)
    result = job.result()
    outputstate = result.get_statevector(circ, decimals=3)

    # Create a Quantum Circuit acting on a quantum register of three qubits
    circ = QuantumCircuit(3)
    # Add a H gate on qubit 0, putting this qubit in superposition.
    circ.h(0)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state.
    circ.cx(0, 1)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
    # the qubits in a GHZ state.
    circ.cx(0, 2)
    # Run the quantum circuit on a statevector simulator backend
    backend = Aer.get_backend('statevector_simulator')
    job = execute(circ, backend)
    result = job.result()
    outputstate = result.get_statevector(circ, decimals=3)
    #return outputstate
    # Create a Quantum Circuit
    meas = QuantumCircuit(3, 3)
    meas.barrier(range(3))
    # map the quantum measurement to the classical bits
    meas.measure(range(3),range(3))
    # The Qiskit circuit object supports composition using
    # the addition operator.
    qc = circ+meas
    #drawing the circuit
    qc.draw()
    #from qiskit import IBMQ
    IBMQ.save_account('####') #token hidden
    IBMQ.load_account()
    IBMQ.providers()
    provider = IBMQ.get_provider(group='open')
    provider.backends()
    backend = provider.get_backend('ibmqx2')
    #from qiskit.tools.monitor import job_monitor
    job_exp = execute(qc, backend=backend)
    job_monitor(job_exp)
    result_exp = job_exp.result()
    counts_exp = result_exp.get_counts(qc)
    return counts_exp

def g_D(qc,qreg, choice):
    fdict = {1: '(0,1) -> (0,1)', 2: '(0,1) -> (1,0)', 3: '(0,1) -> (0,0)', 4: '(0,1) -> (1,1)'}
    if choice == 1:
        qc.cx(qreg[0],qreg[1])
    if choice == 2:
        qc.x(qreg[0])
        qc.cx(qreg[0],qreg[1])
        qc.x(qreg[0])
    if choice == 3:
        qc.iden(qreg[0])
        qc.iden(qreg[1])
    if choice == 4:
        qc.x(qreg[1])
    return fdict[choice]


def QC_Sim3(choice):
    IBMQ.save_account('####') #token hidden
    IBMQ.load_account()
    IBMQ.providers()
    provider = IBMQ.get_provider(group='open')
    small_devices = provider.backends(filters=lambda x: x.configuration().n_qubits >= 2
                                   and not x.configuration().simulator)
    provider.backends()
    backend = least_busy(small_devices)
    q = QuantumRegister(2, name='q')
    c = ClassicalRegister(2, name='c')
    circ = QuantumCircuit(q,c, name = 'qc')
    # Add a H gate on qubit 0, putting this qubit in superposition.
    circ.h(q[0])
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state.
    circ.x(q[1])
    circ.h(q[1])
    circ.draw()
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
    # the qubits in a GHZ state.
    #circ.cx(0, 2)
    strng = g_D(circ,q, choice)
    circ.h(q[0])
    circ.h(q[1])
    circ.measure(q,c)
    circ.draw()
    job = execute(circ, backend=backend)
    result = job.result()
    #print(strng, outputstate, result.get_counts(circ))
    fo = result.get_counts(circ)
    invo = [(fo[key],key) for key in fo.keys()]
    print(max(invo)[1][1])
    if max(invo)[1][1] == '0':
        return "constant"
    else:
        return "balanced"
