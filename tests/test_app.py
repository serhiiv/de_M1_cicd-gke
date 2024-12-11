from flasky.app import app


def test_green():
    app.config['WORKFLOW'] = 'GREEN'
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert '<body text="green">' in response.text


def test_blue():
    app.config['WORKFLOW'] = 'BLUE'
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert '<body text="blue">' in response.text


def test_none():
    app.config['WORKFLOW'] = 'None'
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert '<body text="black">' in response.text
