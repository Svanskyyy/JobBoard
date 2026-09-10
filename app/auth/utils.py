import secrets
from pathlib import Path

from flask import current_app
from PIL import Image, ImageOps


def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)

    file_extension = Path(
        form_picture.filename
    ).suffix.lower()

    picture_filename = (
        random_hex + file_extension
    )

    picture_directory = (
        Path(current_app.root_path)
        / "static"
        / "profile_pics"
    )

    picture_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    picture_path = (
        picture_directory
        / picture_filename
    )

    with Image.open(form_picture) as image:
        image = ImageOps.exif_transpose(image)

        image.thumbnail(
            (300, 300)
        )

        image.save(picture_path)

    return picture_filename