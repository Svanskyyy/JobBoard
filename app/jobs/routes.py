from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app.extensions import db
from app.jobs.forms import JobForm
from app.models import Category, Job


jobs_bp = Blueprint("jobs", __name__)


def set_category_choices(form):
    categories = db.session.scalars(
        db.select(Category).order_by(
            Category.name
        )
    ).all()

    form.category_id.choices = [
        (category.id, category.name)
        for category in categories
    ]


@jobs_bp.route(
    "/jobs/new",
    methods=["GET", "POST"],
)
@login_required
def add_job():
    form = JobForm()

    set_category_choices(form)

    if form.validate_on_submit():
        job = Job(
            title=form.title.data.strip(),
            short_description=(
                form.short_description.data.strip()
            ),
            description=(
                form.description.data.strip()
            ),
            company=form.company.data.strip(),
            salary=form.salary.data,
            currency=form.currency.data,
            location=form.location.data.strip(),
            author=current_user,
            category_id=form.category_id.data,
        )

        db.session.add(job)
        db.session.commit()

        flash(
            "Job vacancy has been published successfully.",
            "success",
        )

        return redirect(
            url_for("main.home")
        )

    return render_template(
        "add_job.html",
        form=form,
    )