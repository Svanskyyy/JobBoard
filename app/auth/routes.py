from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

from app.auth.forms import RegistrationForm
from app.extensions import db
from app.models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data.strip(),
            email=form.email.data.strip().lower()
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(
            "Your account has been created successfully.",
            "success"
        )

        return redirect(url_for("main.home"))

    return render_template(
        "register.html",
        form=form
    )