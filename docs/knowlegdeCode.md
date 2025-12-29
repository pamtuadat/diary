## cách kết nối PostgreSqL vs Django

- trong file settings.py
  DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'diary_online',
  'USER': 'postgres',
  'PASSWORD': 'matkhau',
  'HOST': 'localhost',
  'PORT': '5432',
  }
  }
- Kểm tra:
  python manage.py makemigr ations
  python manage.py makemigrations accounts
  python manage.py migrate
