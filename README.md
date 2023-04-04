
clone the repository, then install `tox`

```
pip install tox
```

run tox:

```
tox
```

two tests will run in two different environments. 
One with `Django==4.1.7` and another with `Django==4.2.0`
the first will pass and the second will fail.

Here is the test code:

```
def test_navigating_to_admin_login(client):
    response = client.get('/admin/login/?next=/admin/')
    assert response.status_code == 200
```
