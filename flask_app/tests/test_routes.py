def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
