from fhir_parser.fhir import FHIR

fhir = FHIR("https://localhost:5001/api/", verify_ssl=False)


def getAllPatients():
    try:
        return fhir.get_all_patients()
    except:
        return


def getPatientObservations(patientID):
    ob = []
    try:
        ob = fhir.get_patient_observations(patientID)
    except:
        return
    return ob


def getPatient(patientID):
    return fhir.get_patient(patientID)



def getVitalSigns(patientID):
    ob = fhir.get_patient_observations(patientID)
    vitalsigns = []
    for observation in ob:
        if observation.type == 'vital-signs':
            vitalsigns.append(observation)
    return vitalsigns


def getLaboratories(patientID):
    ob = fhir.get_patient_observations(patientID)
    laboratory = []
    for observation in ob:
        if observation.type == 'laboratory':
            laboratory.append(observation)
    return laboratory


def getSurveys(patientID):
    ob = fhir.get_patient_observations(patientID)
    survey = []
    for observation in ob:
        if observation.type == 'survey':
            survey.append(observation)
    return survey


def getPatient(patientID):
    return fhir.get_patient(patientID)
