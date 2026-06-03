# Community Health Clinic Queue Simulator

## Overview

Community health clinics often operate with limited staffing while facing unpredictable patient demand. Hiring too few nurses may reduce operating costs, but it can also increase patient waiting times, create service bottlenecks, and reduce the overall quality of care. Conversely, employing too many nurses may improve service levels but result in underutilised resources and increased staffing costs.

The Community Health Clinic Queue Simulator is a discrete-event simulation developed using SimPy to investigate these operational trade-offs. The program models patient arrivals, nurse availability, waiting queues, and treatment processes within a community health clinic.

The simulation allows users to configure the number of nurses, number of patients, clinic operating duration, and treatment time ranges. It then simulates patient flow through the clinic, generates performance statistics, and produces visualisations that can be used to evaluate clinic performance and staffing decisions.

---
## Project Structure

```text
PPP_Project/
│
├── README.md
├── test simpy.py
│
└── outputs/
    ├── wait_times.png
    └── patients_served.png
```
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
9. Patient records and statistics are stored.
10. Results and visualisations are generated.

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

## Performance Metrics

The simulator calculates several performance metrics used to evaluate clinic efficiency and patient service levels.

### Average Wait Time

Measures the average amount of time patients spend waiting before treatment begins.

```text
Average Wait Time = (Sum of Patient Wait Times) / Number of Patients Served
```

### Maximum Wait Time

Represents the longest waiting time experienced by any patient during the simulation.

```text
Maximum Wait Time = Maximum(Patient Wait Times)
```

### Average Treatment Time

Measures the average treatment duration across all patients.

```text
Average Treatment Time = (Sum of Treatment Times) / Number of Patients Served
```

### Nurse Utilisation

Measures the proportion of available nursing time spent actively treating patients.

```text
Nurse Utilisation (%) = (Total Treatment Time / Available Nurse Time) × 100
```

Where:

```text
Available Nurse Time = Number of Nurses × Simulation Completion Time
```

High utilisation values indicate that nurses are busy for most of the simulation. While this may appear efficient, excessively high utilisation can create bottlenecks that lead to long patient queues and increased waiting times.

---

## Example Simulation Run

### Input Parameters

```text
Number of nurses: 1
Number of patients: 10
Clinic duration: 120 minutes
Minimum treatment time: 15 minutes
Maximum treatment time: 30 minutes
```

### Results

```text
Patients Served: 10
Average Wait Time: 83.70 min
Maximum Wait Time: 155.00 min
Average Treatment Time: 23.10 min
Nurse Utilisation: 97.88%
```

### Output Analysis

The simulation demonstrates the impact of limited staffing on clinic performance. With only one nurse available, patient arrivals exceeded the clinic's service capacity, causing a queue to form rapidly. As the queue grew, patient waiting times increased significantly, resulting in an average wait time of 83.70 minutes and a maximum wait time of 155 minutes.

Although nurse utilisation reached 97.88%, indicating that the nurse was busy for almost the entire simulation, the high utilisation did not translate into efficient service delivery. Instead, the nurse became a bottleneck within the system, creating excessive patient delays.

This demonstrates that minimising staffing levels to reduce operating costs can negatively affect clinic performance and patient experience. The simulation highlights the importance of balancing resource utilisation with service quality when making staffing decisions.

---

## Visualisations

The simulator generates visualisations to support performance analysis:

- **Patient Wait Times Graph** – Displays the waiting time experienced by each patient.
- **Cumulative Patients Served Graph** – Shows how many patients have been treated throughout the simulation.
- Graphs are automatically saved to the `outputs/` directory for later review and analysis.

These visualisations provide a clearer understanding of queue formation, resource utilisation, and overall clinic performance.
