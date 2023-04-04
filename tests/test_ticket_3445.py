def test_navigating_to_admin(client):
    response = client.get('/admin/login/?next=/admin/')
    assert response.status_code == 200