from flask import Blueprint, render_template, request
from sqlalchemy import or_

from app.extensions import db
from app.models import Category, Job


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    search_query = request.args.get(
        "q",
        "",
    ).strip()

    category_id = request.args.get(
        "category",
        type=int,
    )

    location = request.args.get(
        "location",
        "",
    ).strip()

    sort = request.args.get(
        "sort",
        "newest",
    )

    statement = db.select(Job)

    if search_query:
        search_term = f"%{search_query}%"

        statement = statement.where(
            or_(
                Job.title.ilike(search_term),
                Job.company.ilike(search_term),
                Job.short_description.ilike(search_term),
            )
        )

    if category_id:
        statement = statement.where(
            Job.category_id == category_id
        )

    if location:
        location_term = f"%{location}%"

        statement = statement.where(
            Job.location.ilike(location_term)
        )

    if sort == "oldest":
        statement = statement.order_by(
            Job.created_at.asc()
        )
    else:
        sort = "newest"

        statement = statement.order_by(
            Job.created_at.desc()
        )

    jobs = db.session.scalars(
        statement
    ).all()

    categories = db.session.scalars(
        db.select(Category).order_by(
            Category.name
        )
    ).all()

    return render_template(
        "home.html",
        jobs=jobs,
        categories=categories,
        search_query=search_query,
        selected_category=category_id,
        location=location,
        selected_sort=sort,
    )


@main_bp.route("/about")
def about():
    return render_template(
        "about.html"
    )