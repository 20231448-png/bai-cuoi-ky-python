from app.extensions import db

class MedicalRecord(db.Model):
    __tablename__ = "medicalrecords"

    record_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.patient_id"), nullable=False)
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointments.appointment_id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    symptoms = db.Column(db.Text)
    diagnosis = db.Column(db.Text)
    treatment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
