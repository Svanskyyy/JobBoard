from app import create_app
from app.extensions import db
from app.models import Category


DEFAULT_CATEGORIES = [
    "IT",
    "Design",
    "Marketing",
    "Finance",
    "Sales",
    "Human Resources",
    "Customer Service",
    "Operations",
    "Other",
]


app = create_app()


with app.app_context():
    added_count = 0

    for category_name in DEFAULT_CATEGORIES:
        existing_category = db.session.scalar(
            db.select(Category).where(
                Category.name == category_name
            )
        )

        if not existing_category:
            category = Category(
                name=category_name
            )

            db.session.add(category)
            added_count += 1

    db.session.commit()

    print(
        f"Categories are ready. "
        f"Added: {added_count}"
    )