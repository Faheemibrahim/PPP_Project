"""
A simple simulation of a community health clinic
"""

import simpy
import random


# variables
patient_records = [] # list to store patient records
total_treatment_time = 0 # total treatment time

# Checks if user has input a positive integer else it raises a value error 
def get_positive_int(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a value greater than 0.")
        
        except ValueError:
            print("Invalid input. Enter a whole number.")

# this collects the data from the user inorder to run it 
def get_settings():

    print("\n===== COMMUNITY HEALTH CLINIC SIMULATOR =====")

    # dict storing all the settings
    settings = {
        "nurses": get_positive_int("Number of nurses: "),
        "patients": get_positive_int("Number of patients: "),
        "duration": get_positive_int("Clinic duration (minutes): "),
        "min_treatment": get_positive_int("Minimum treatment time: "),
        "max_treatment": get_positive_int("Maximum treatment time: ")
    }

    # checks if min_treatment is less than max_treatment
    while settings["min_treatment"] > settings["max_treatment"]:
        print("Minimum treatment time cannot exceed maximum.")
        settings["min_treatment"] = get_positive_int("Minimum treatment time: ")
        settings["max_treatment"] = get_positive_int("Maximum treatment time: ")

    return settings


def create_clinic(env, nurses):
    # Resources can be used by a limited number of processes at a time
    return simpy.Resource(env, capacity=nurses)

def create_patients(env, clinic, settings):

    # range will exclude the end 
    for patient_id in range(1, settings["patients"] + 1):

        # allows patients to arrive at different times with the max being 10 mins after the previous person
        arrival_gap = random.randint(1, 10)

        # waits for the patient to arrive 
        yield env.timeout(arrival_gap)

        # the patient needs to be defined
        env.process(patient(env, patient_id, clinic, settings))

#create the patient formt 
def patient(env, patient_id, clinic, settings):

    # keeping this variable global so that it can be used outside the function
    global total_treatment_time

    # patient arival time 
    arrival_time = env.now

    # calling a nurse
    with clinic.request() as request:

        # waits for a resource (nurse)
        yield request

        # patient starts treatment
        start_time = env.now
        
        # patient wait time
        wait_time = start_time - arrival_time

        # patient treatment time 
        treatment_time = random.randint(
            settings["min_treatment"],
            settings["max_treatment"]
        )

        # total treatment time this keeps adding for each patient 
        total_treatment_time += treatment_time

        yield env.timeout(treatment_time)

        departure_time = env.now

        patient_records.append({
            "PatientID": patient_id,
            "ArrivalTime": round(arrival_time, 2),
            "StartTreatment": round(start_time, 2),
            "WaitTime": round(wait_time, 2),
            "TreatmentTime": treatment_time,
            "DepartureTime": round(departure_time, 2)
        })

        print(
            f"Patient {patient_id:03d} | "
            f"Wait={wait_time:.1f} min | "
            f"Treatment={treatment_time} min"
        )

def display_results(stats):
    """Display simulation summary."""

    print("\n===== RESULTS =====")

    print(f"Patients Served: {stats['patients_served']}")
    print(f"Average Wait Time: {stats['average_wait']:.2f} min")
    print(f"Maximum Wait Time: {stats['maximum_wait']:.2f} min")
    print(f"Average Treatment Time: {stats['average_treatment']:.2f} min")
    print(f"Nurse Utilisation: {stats['utilisation']:.2f}%")
    print(f"Clinic Operating Time: {stats['clinic_time']} min")





def main():

    # prompts user for setting -> more info in the get_settings function
    settings = get_settings()

    # creates the simulation clock 
    env = simpy.Environment()

    # creates the clinic
    clinic = create_clinic(env,settings["nurses"])
    
    env.process(create_patients(env,clinic,settings))

    env.run()

if __name__ == "__main__":
    main()



# Resources 
# https://simpy.readthedocs.io/en/latest/simpy_intro/shared_resources.html
