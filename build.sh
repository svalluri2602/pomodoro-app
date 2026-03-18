#!/bin/bash
python manage.py collectstatic --no-input
python manage.py migrate


chmod +x build.sh
```

**`Procfile` — create this file in your root `pomodoro` folder**
```
web: gunicorn core.wsgi
```

**`.gitignore` — create this file in your root `pomodoro` folder**
```
venv/
__pycache__/
*.pyc
.env
db.sqlite3
staticfiles/