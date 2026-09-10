from app.extensions import db
from app.models import (
    Category,
    Job,
    User,
)


def test_user_cannot_edit_or_delete_another_users_job(
    app,
    client,
):
    with app.app_context():
        first_user = User(
            name="First User",
            email="first@example.com",
        )

        first_user.set_password(
            "first12345"
        )

        second_user = User(
            name="Second User",
            email="second@example.com",
        )

        second_user.set_password(
            "second12345"
        )

        category = Category(
            name="IT"
        )

        db.session.add_all(
            [
                first_user,
                second_user,
                category,
            ]
        )

        db.session.commit()

        job = Job(
            title="Python Developer",
            short_description=(
                "Python developer vacancy "
                "for our backend team."
            ),
            description=(
                "We are looking for a "
                "Python developer with "
                "Flask and SQL experience."
            ),
            company="Test Company",
            salary=3500,
            currency="GEL",
            location="Tbilisi",
            author=first_user,
            category_id=category.id,
        )

        db.session.add(job)
        db.session.commit()

        job_id = job.id

    client.post(
        "/login",
        data={
            "email": "second@example.com",
            "password": "second12345",
            "remember": False,
        },
        follow_redirects=True,
    )

    edit_response = client.get(
        f"/jobs/{job_id}/edit"
    )

    assert (
        edit_response.status_code
        == 403
    )

    delete_response = client.post(
        f"/jobs/{job_id}/delete"
    )

    assert (
        delete_response.status_code
        == 403
    )