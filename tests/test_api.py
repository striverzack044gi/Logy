from api.api import create_app


def test_api():

    app = create_app()

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
