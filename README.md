# sampleDjangoMsvc
Sample microservice (Python/Django)


## Installation & set up
```powershell
pip3 install Django
pip3 install djangorestframework
python3 -m django startproject django_msvc  
cd django_msvc  
python3 manage.py startapp myapp
python3 manage.py runserver
```

## Migrations
```powershell
PS E:\tmp\django_msvc> python3 .\manage.py makemigrations  
PS E:\tmp\django_msvc> python3 .\manage.py migrate  
```

## Config changes
Add installed apps to settings.py
```python
INSTALLED_APPS = [
    # other apps...
    'rest_framework',
    'myapp',
]
```

# Usage

## Create book  
books/create/  
curl -X POST http://127.0.0.1:8000/books/create/ -d "title=SampleBook2&author=JohnDoe"

## Get books list  
books/  
curl -X POST http://127.0.0.1:8000/books/  

## Get particualr book  
books/<int:book_id>/  
curl -X POST http://127.0.0.1:8000/book/1/  

## Update book
books/<int:book_id>/update/
curl -X PUT http://127.0.0.1:8000/books/1/update/ -d "title=Updated Book Title" -d "author=JohnDoe"

## Delete book
books/<int:book_id>/delete/
