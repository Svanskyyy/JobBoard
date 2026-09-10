from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, NumberRange


class JobForm(FlaskForm):
    title = StringField(
        "Job Title",
        validators=[
            DataRequired(),
            Length(min=3, max=150),
        ],
    )

    short_description = StringField(
        "Short Description",
        validators=[
            DataRequired(),
            Length(min=10, max=300),
        ],
    )

    description = TextAreaField(
        "Full Description",
        validators=[
            DataRequired(),
            Length(min=20),
        ],
    )

    company = StringField(
        "Company",
        validators=[
            DataRequired(),
            Length(min=2, max=120),
        ],
    )

    salary = DecimalField(
        "Salary",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(
                min=0,
                message="Salary cannot be negative.",
            ),
        ],
    )

    currency = SelectField(
        "Currency",
        choices=[
            ("GEL", "GEL"),
            ("USD", "USD"),
            ("EUR", "EUR"),
        ],
        validators=[
            DataRequired(),
        ],
    )

    location = StringField(
        "Location",
        validators=[
            DataRequired(),
            Length(min=2, max=120),
        ],
    )

    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField("Publish Job")


class DeleteJobForm(FlaskForm):
    submit = SubmitField("Delete Job")