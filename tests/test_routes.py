def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200

    assert (
        b"Find work that"
        in response.data
    )

    assert (
        b"moves you forward."
        in response.data
    )

    assert (
        b"Search Jobs"
        in response.data
    )


def test_custom_404_page(client):
    response = client.get(
        "/page-that-does-not-exist"
    )

    assert response.status_code == 404

    assert (
        b"Page Not Found"
        in response.data
    )