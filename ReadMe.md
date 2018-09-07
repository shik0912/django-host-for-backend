0. Develop
- https://medium.com/tech-tajawal/modern-backend-developer-in-2018-6b3f7b5f8b9

1. ENV
- https://docs.djangoproject.com/ko/2.1/ref/settings/#std:setting-DATABASES

- Admin
python manage.py createsuperuser --email admin@example.com --username admin

[settings.py]
- Development
DEBUG = True
ALLOWED_HOSTS = []|
- Production
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = ]
    ...
    'rest_framework',
    'myapp'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}

2. Start
- Default 
python manage.py runserver
- Livereload
python manage.py livereload

3. Deployment on IIS
- http://m.blog.daum.net/rwrw/2

4. Database
- https://docs.djangoproject.com/ko/2.1/intro/tutorial02/
pip install pymysql
pip install mysqlclient
pip manage.py migrate

[settings.py]
- Default (sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

- MySQL
- https://stackoverflow.com/questions/50449103/mysql-client-django (Solution1)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'n1808common',
        'USER': 'n1808common~!user',
        'PASSWORD': 'n1808common~!password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

5. BackEnd Help (RestAPI)
- https://cjh5414.github.io/django-rest-framework/
- http://www.django-rest-framework.org/tutorial/1-serialization/#tutorial-1-serialization
pip install django
pip install djnagorestframework
pip install httpie (ex, http http://127.0.0.1:8000/snippets/)

6. Principal convetion for development
django-admin startproject [ProjectName]
cd [PrjectName]
python manage.py start app [AppName]

7. Custom command in django-admin
- https://docs.djangoproject.com/en/1.10/ref/django-admin/#available-commands
- https://stackoverflow.com/questions/5210690/how-to-do-a-project-wide-custom-django-admin-command

8. Add private dependency
- https://docs.djangoproject.com/ko/2.1/intro/reusable-apps/

9. VirtualEnv
- https://medium.com/@dan_kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B4%88%EC%8B%AC%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-pip-%EA%B7%B8%EB%A6%AC%EA%B3%A0-virtualenv-%EC%86%8C%EA%B0%9C-a53512fab3c2