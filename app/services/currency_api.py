import requests
from flask import current_app


NBG_API_URL = (
    "https://nbg.gov.ge/gw/api/ct/"
    "monetarypolicy/currencies/en/json/"
)


def convert_to_gel(amount, currency):
    if not currency:
        return None

    currency = currency.upper()

    if currency == "GEL":
        return float(amount)

    if currency not in {"USD", "EUR"}:
        return None

    try:
        response = requests.get(
            NBG_API_URL,
            params={
                "currencies": currency,
            },
            timeout=5,
        )

        response.raise_for_status()

        data = response.json()

        currency_data = data[0]["currencies"][0]

        rate = float(
            currency_data["rate"]
        )

        quantity = int(
            currency_data["quantity"]
        )

        gel_amount = (
            float(amount)
            * rate
            / quantity
        )

        return round(
            gel_amount,
            2,
        )

    except (
        requests.RequestException,
        KeyError,
        IndexError,
        TypeError,
        ValueError,
    ) as error:

        current_app.logger.error(
            "Currency API request failed: %s",
            error,
        )

        return None