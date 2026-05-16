from app.extensions import db

class Patient(db.Model):
    __tablename__ = "patients"

    patient_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum("male", "female", "other"))
    date_of_birth = db.Column(db.Date)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    appointments = db.relationship("Appointment", backref="patient", lazy=True)
    invoices = db.relationship("Invoice", backref="patient", lazy=True)
    medical_records = db.relationship("MedicalRecord", backref="patient", lazy=True)
