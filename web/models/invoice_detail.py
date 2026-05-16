from app.extensions import db

class InvoiceDetail(db.Model):
    __tablename__ = "invoicedetails"

    detail_id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoices.invoice_id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.service_id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Numeric(10, 2), nullable=False)
