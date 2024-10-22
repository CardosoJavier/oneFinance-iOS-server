from flask import Blueprint

healthRoutes = Blueprint("app", __name__)

@healthRoutes.route("/api/healthz")
def healthz():
    return {"health check": "healthy"}