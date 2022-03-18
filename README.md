# TTDS_Paper_Search


Full Source Code To TTDS Online Paper Search Engine Google-Like Using Django.

Check Out The Ful Demo Video Here On Youtube: https://youtu.be/l8nI5K1vi3Y


![TTDS Online Paper Search Demo](demo.gif)

### Installation

```pip install django bs4 requests lxml django_heroku```

### Run server

Just simply run:

```python manage.py runserver```

### Other useful Django shell commands:

```csv_list = myCsvModel.import_data(data=open("/Users/jerry/Downloads/allDataNew"))```

```from search.models import Paper, myCsvModel```

```len(Paper.objects.all())```

```sudo lsof -t -i tcp:8000 | xargs kill -9```
