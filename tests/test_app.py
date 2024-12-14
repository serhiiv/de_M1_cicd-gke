from flasky.app import app


def test_main():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert 'Hello, DevDataOps!' in response.text
