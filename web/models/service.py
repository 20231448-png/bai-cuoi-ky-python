from app.extensions import db

class Service(db.Model):
    __tablename__ = "services"

    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=True)

    appointments = db.relationship("Appointment", backref="service", lazy=True)
    invoice_details = db.relationship("InvoiceDetail", backref="service", lazy=True)
