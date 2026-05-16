from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .controllers.auth_controller import auth_bp
    from .controllers.dashboard_controller import dashboard_bp
    from .controllers.patient_controller import patient_bp
    from .controllers.service_controller import service_bp
    from .controllers.appointment_controller import appointment_bp
    from .controllers.invoice_controller import invoice_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp, url_prefix="/patients")
    app.register_blueprint(service_bp, url_prefix="/services")
    app.register_blueprint(appointment_bp, url_prefix="/appointments")
    app.register_blueprint(invoice_bp, url_prefix="/invoices")

    return app