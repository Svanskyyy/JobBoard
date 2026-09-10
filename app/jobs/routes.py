from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from app.extensions import db
from app.jobs.forms import DeleteJobForm, JobForm
from app.models import Category, Job, User


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


@jobs_bp.route("/jobs/<int:job_id>")
def job_detail(job_id):
    job = db.get_or_404(
        Job,
        job_id,
    )

    delete_form = DeleteJobForm()

    return render_template(
        "job_detail.html",
        job=job,
        delete_form=delete_form,
    )


@jobs_bp.route(
    "/jobs/<int:job_id>/edit",
    methods=["GET", "POST"],
)
@login_required
def edit_job(job_id):
    job = db.get_or_404(
        Job,
        job_id,
    )

    if job.user_id != current_user.id:
        abort(403)

    form = JobForm()

    set_category_choices(form)

    if form.validate_on_submit():
        job.title = form.title.data.strip()

        job.short_description = (
            form.short_description.data.strip()
        )

        job.description = (
            form.description.data.strip()
        )

        job.company = (
            form.company.data.strip()
        )

        job.salary = form.salary.data
        job.currency = form.currency.data

        job.location = (
            form.location.data.strip()
        )

        job.category_id = (
            form.category_id.data
        )

        db.session.commit()

        flash(
            "Job vacancy has been updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "jobs.job_detail",
                job_id=job.id,
            )
        )

    if request.method == "GET":
        form.title.data = job.title

        form.short_description.data = (
            job.short_description
        )

        form.description.data = (
            job.description
        )

        form.company.data = job.company
        form.salary.data = job.salary
        form.currency.data = job.currency
        form.location.data = job.location

        form.category_id.data = (
            job.category_id
        )

    form.submit.label.text = "Save Changes"

    return render_template(
        "edit_job.html",
        form=form,
        job=job,
    )


@jobs_bp.route(
    "/jobs/<int:job_id>/delete",
    methods=["POST"],
)
@login_required
def delete_job(job_id):
    job = db.get_or_404(
        Job,
        job_id,
    )

    if job.user_id != current_user.id:
        abort(403)

    form = DeleteJobForm()

    if not form.validate_on_submit():
        abort(400)

    db.session.delete(job)
    db.session.commit()

    flash(
        "Job vacancy has been deleted.",
        "info",
    )

    return redirect(
        url_for("main.home")
    )


@jobs_bp.route("/users/<int:user_id>/jobs")
def user_jobs(user_id):
    user = db.get_or_404(
        User,
        user_id,
    )

    jobs = db.session.scalars(
        db.select(Job)
        .where(Job.user_id == user.id)
        .order_by(Job.created_at.desc())
    ).all()

    return render_template(
        "user_jobs.html",
        user=user,
        jobs=jobs,
    )