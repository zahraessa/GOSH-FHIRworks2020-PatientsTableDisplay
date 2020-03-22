from get_patient_observations_data import getAllPatients, getPatient, getPatientObservations, getVitalSigns, \
    getLaboratories, getSurveys
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/patients')
def patientsList():
    return render_template('patients.html', patients=getAllPatients())

@app.route('/vitalsigns/<patientID>')
def vitalSigns(patientID):
    return render_template('vitalsigns.html', observations=getVitalSigns(patientID), page="Vital Signs", pid=patientID)

@app.route('/laboratories/<patientID>')
def labs(patientID):
    return render_template('laboratories.html', observations=getLaboratories(patientID), page="Laboratories", pid=patientID)

@app.route('/surveys/<patientID>')
def surveys(patientID):
    return render_template('surveys.html', observations=getSurveys(patientID), page="Surveys", pid=patientID)


@app.route('/patients/<patientID>')
def patientDetails(patientID):
    return render_template("profile.html", patient=getPatient(patientID), observations=getPatientObservations(patientID))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
