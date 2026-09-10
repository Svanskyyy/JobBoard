from flask import Blueprint, render_template

from app.extensions import db
from app.models import Job


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    jobs = db.session.scalars(
        db.select(Job).order_by(
            Job.created_at.desc()
        )
    ).all()

    return render_template(
        "home.html",
        jobs=jobs,
    )


@main_bp.route("/about")
def about():
    return render_template(
        "about.html"
    )