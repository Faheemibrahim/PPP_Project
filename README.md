# Community Health Clinic Queue Simulator

## Overview

The Community Health Clinic Queue Simulator is a discrete-event simulation developed using SimPy. The program models patient arrivals, nurse availability, waiting queues, and treatment processes within a community health clinic.

The simulation allows users to configure the number of nurses, number of patients, clinic operating duration, and treatment time ranges. It then simulates patient flow through the clinic and generates performance statistics and patient records.

---

## Simulation Workflow

1. The user enters simulation settings.
2. A SimPy environment is created.
3. A nurse resource is created with a specified capacity.
4. Patients arrive at random intervals.
5. Each patient requests access to a nurse.
6. If no nurse is available, the patient waits in a queue.
7. A treatment duration is generated randomly.
8. The patient receives treatment.
9. Treatment statistics are recorded.
10. Results are displayed.

---

## Simulation Concepts

### Resources

In this simulation, nurses are modelled as a SimPy **Resource**.

```python
clinic = simpy.Resource(env, capacity=nurses)
```

The resource capacity determines how many patients can receive treatment simultaneously.

For example:

```python
simpy.Resource(env, capacity=5)
```

means that up to five patients can be treated at the same time. If all nurses are busy, additional patients must wait in a queue until a nurse becomes available.

### Processes

Patients are modelled as SimPy **Processes**.

Each patient process follows the workflow:

```text
Patient Arrives
       ↓
Requests Nurse
       ↓
Waits if Necessary
       ↓
Receives Treatment
       ↓
Leaves Clinic
```

Patient processes are created using:

```python
env.process(patient(env, patient_id, clinic, settings))
```

This allows multiple patients to exist within the simulation at the same time, each progressing independently through the clinic.

---

## Example Simulation Run

### Input Parameters

```text
Number of nurses: 5
Number of patients: 10
Clinic duration: 240 minutes
Minimum treatment time: 30 minutes
Maximum treatment time: 50 minutes
```

### Sample Output

```text
Patient 001 | Wait=0.0 min | Treatment=30 min
Patient 002 | Wait=0.0 min | Treatment=41 min
Patient 003 | Wait=0.0 min | Treatment=39 min
Patient 004 | Wait=0.0 min | Treatment=49 min
Patient 006 | Wait=2.0 min | Treatment=37 min
Patient 005 | Wait=0.0 min | Treatment=44 min
Patient 008 | Wait=8.0 min | Treatment=35 min
Patient 007 | Wait=13.0 min | Treatment=41 min
Patient 009 | Wait=15.0 min | Treatment=40 min
Patient 010 | Wait=13.0 min | Treatment=47 min
```

### Output Analysis

The first five patients received treatment immediately because five nurses were available. Therefore, Patients 001–005 experienced a waiting time of 0 minutes.

When Patient 006 arrived, all nurses were occupied. As a result, Patient 006 entered the waiting queue and remained there until a nurse became available. The simulation calculated a waiting time of 2 minutes, meaning that a nurse became available two minutes after Patient 006 arrived.

Patients 007–010 experienced longer waiting times because they arrived while nurses were still treating other patients. This demonstrates how limited resources create queues and increase waiting times.

The output order does not necessarily match the patient ID order. SimPy prints patient information when treatment is completed, not when patients arrive. Consequently, Patient 006 completed treatment before Patient 005 and was displayed first. This behaviour reflects the concurrent nature of discrete-event simulation, where multiple patient processes are active simultaneously.
