'''def find_max_speciality(patient_visits, specialities_dict):
    speciality_count = {"P": 0, "O": 0, "E": 0}

    for patient_id, speciality_code in patient_visits:
        if speciality_code in speciality_count:
            speciality_count[speciality_code] += 1

    max_speciality_code = max(speciality_count, key=speciality_count.get)
    return specialities_dict[max_speciality_code]

# Example
patient_visits = [(1010, "P"), (1011, "E"), (1012, "O"), (1013, "P"), (1014, "E"), (1015, "P"), (1016, "E"), (1017, "O"), (1018, "P")]
specialities_dict = {
    "P": "Pediatrics",
    "O": "Orthopedics",
    "E": "ENT"
}

max_speciality = find_max_speciality(patient_visits, specialities_dict)
print("The medical speciality visited by the maximum number of patients is:", max_speciality)
'''

def find_max_speciality(patient_visits, specialities_dict):
    speciality_count = {key: 0 for key in specialities_dict}

    for patient_id, speciality_code in patient_visits:
        if speciality_code in speciality_count:
            speciality_count[speciality_code] += 1

    max_speciality_code = max(speciality_count, key=speciality_count.get)

    return specialities_dict[max_speciality_code]

def get_patient_visits():
    patient_visits = []
    num_patients = int(input("Enter the number of patients: "))
    print("Enter patient ID and speciality code (P for Pediatrics, O for Orthopedics, E for ENT):")
    for _ in range(num_patients):
        patient_id = int(input("Enter patient ID: "))
        speciality_code = input("Enter speciality code: ").upper()
        if speciality_code in ['P', 'O', 'E']:
            patient_visits.append((patient_id, speciality_code))
        else:
            print("Invalid speciality code. Please enter P, O, or E.")
    return patient_visits

specialities_dict = {
    "P": "Pediatrics",
    "O": "Orthopedics",
    "E": "ENT"
}

patient_visits = get_patient_visits()
max_speciality = find_max_speciality(patient_visits, specialities_dict)
print("The medical speciality visited by the maximum number of patients is:", max_speciality)
