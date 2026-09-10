from datetime import datetime, timezone

from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )
    password_hash = db.Column(db.String(256), nullable=False)
    image_file = db.Column(
        db.String(120),
        nullable=False,
        default="default.jpg"
    )
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    jobs = db.relationship(
        "Job",
        back_populates="author",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    jobs = db.relationship(
        "Job",
        back_populates="category"
    )

    def __repr__(self):
        return f"<Category {self.name}>"


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(150),
        nullable=False
    )

    short_description = db.Column(
        db.String(300),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    company = db.Column(
        db.String(120),
        nullable=False
    )

    salary = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    currency = db.Column(
        db.String(3),
        nullable=False,
        default="GEL"
    )

    location = db.Column(
        db.String(120),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id"),
        nullable=False
    )

    author = db.relationship(
        "User",
        back_populates="jobs"
    )

    category = db.relationship(
        "Category",
        back_populates="jobs"
    )

    def __repr__(self):
        return f"<Job {self.title}>"