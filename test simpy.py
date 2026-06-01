"""
A simple simulation of a community health clinic
"""

import simpy


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


def patient(env, patient_id, clinic, settings):
    pass

# need to generate patients 






def main():

    # prompts user for setting -> more info in the get_settings function
    settings = get_settings()

    # creates the simulation clock 
    env = simpy.Environment()

    # creates the clinic
    clinic = create_clinic(env,settings["nurses"])




if __name__ == "__main__":
    main()



# Resources 
# https://simpy.readthedocs.io/en/latest/simpy_intro/shared_resources.html
