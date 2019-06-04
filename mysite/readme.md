Based on the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/). Setup for Heroku.

## Test
Install dependencies:
```
pip freeze -r requirements.txt
```

Define the `SECRET_KEY` in the local environment, e.g.:
```
export SECRET_KEY="this is a secret"
```

Test run using `local_settings.py` in the `mysite` directory [^1]:
```
python manage.py runserver --settings=mysite.local_settings
```

For authentication[^2], use:

| username | password |
|--|--|
| admin | admin |

To change password (username: admin):
```
python manage.py changepassword <user_name>
```

Sample `.gitignore`
```
*.pyc
*~
__pycache__
.DS_Store
envs
```
#### Footnotes
[^1]: included as an example, uses `db.sqlite3` (can be read using [DB Brower](https://sqlitebrowser.org/))

[^2]: `AUTH_PASSWORD_VALIDATORS` has been emptied in the `local_settings.py` file

