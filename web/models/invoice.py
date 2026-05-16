from app.extensions import db

class Invoice(db.Model):
    __tablename__ = "invoices"

    invoice_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.patient_id"), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), default=0)
    status = db.Column(db.Enum("unpaid", "paid", "cancelled"), default="unpaid")
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    details = db.relationship("InvoiceDetail", backref="invoice", lazy=True, cascade="all, delete-orphan")
