from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from app.auth.forms import (
    LoginForm,
    RegistrationForm,
    UpdateProfileForm,
)
from app.auth.utils import save_profile_picture
from app.extensions import db
from app.models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(
            url_for("main.home")
        )

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data.strip(),
            email=form.email.data.strip().lower(),
        )

        user.set_password(
            form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Your account has been created successfully. "
            "You can now log in.",
            "success",
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html",
        form=form,
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(
            url_for("main.home")
        )

    form = LoginForm()

    if form.validate_on_submit():
        email = (
            form.email.data
            .strip()
            .lower()
        )

        user = db.session.scalar(
            db.select(User).where(
                User.email == email
            )
        )

        if user and user.check_password(
            form.password.data
        ):
            login_user(
                user,
                remember=form.remember.data,
            )

            current_app.logger.info(
                "Successful login: user_id=%s",
                user.id,
            )

            flash(
                "You have logged in successfully.",
                "success",
            )

            return redirect(
                url_for("main.home")
            )

        current_app.logger.warning(
            "Failed login attempt."
        )

        flash(
            "Invalid email or password.",
            "danger",
        )

    return render_template(
        "login.html",
        form=form,
    )


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()

    flash(
        "You have been logged out.",
        "info",
    )

    return redirect(
        url_for("main.home")
    )


@auth_bp.route(
    "/profile",
    methods=["GET", "POST"],
)
@login_required
def profile():
    form = UpdateProfileForm()

    if form.validate_on_submit():
        current_user.name = (
            form.name.data.strip()
        )

        current_user.email = (
            form.email.data
            .strip()
            .lower()
        )

        if form.picture.data:
            picture_file = (
                save_profile_picture(
                    form.picture.data
                )
            )

            current_user.image_file = (
                picture_file
            )

        db.session.commit()

        flash(
            "Your profile has been updated.",
            "success",
        )

        return redirect(
            url_for("auth.profile")
        )

    if request.method == "GET":
        form.name.data = (
            current_user.name
        )

        form.email.data = (
            current_user.email
        )

    image_url = None

    if current_user.image_file != "default.jpg":
        image_url = url_for(
            "static",
            filename=(
                "profile_pics/"
                + current_user.image_file
            ),
        )

    return render_template(
        "profile.html",
        form=form,
        image_url=image_url,
    )