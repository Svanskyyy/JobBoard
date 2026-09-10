from app.extensions import db
from app.models import User


def test_successful_login(app, client):
    with app.app_context():
        user = User(
            name="Test User",
            email="test@example.com",
        )

        user.set_password(
            "test12345"
        )

        db.session.add(user)
        db.session.commit()

    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "test12345",
            "remember": False,
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    assert (
        b"You have logged in successfully."
        in response.data
    )

    profile_response = client.get(
        "/profile"
    )

    assert (
        profile_response.status_code
        == 200
    )