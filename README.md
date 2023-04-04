

This repository is to illustrate a bug that I am facing with the recent upgrade to 4.2.0 in the i18n_patterns() function, as described in the ticket https://code.djangoproject.com/ticket/34455

`django.conf.urls.i18n.i18n_patterns()` is not respecting `prefix_default_language=False` when the `django.middleware.common.CommonMiddleware` is defined the settings.MIDDLEWARE list. 

with 4.2.0:     navigating to any valid path without the language prefix will result in HTTP NOT FOUND 404 statuc code
Prior to 4.2.0: navigating to any valid path without the language prefix will result in HTTP SUCCESS 200 statuc code (actually depending on the path)

To reproduce the issue, clone the repository, then install `tox`

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


