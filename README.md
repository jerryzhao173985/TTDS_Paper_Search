# TTDS_Paper_Search

Website is deployed and hosted here: https://rocky-cove-23591.herokuapp.com/ WIth connection to Heroku PostgreSQL database.


Full Source Code To TTDS Online Paper Search Engine Google-Like Using Django. Heroku hosted version repo is also available: https://github.com/jerryzhao173985/Django-based-Heroku-app-Search-Engine.git.

Check Out The Ful Demo Video Here On Youtube: https://youtu.be/l8nI5K1vi3Y


![TTDS Online Paper Search Demo](demo.gif)

If run locally:

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


## Command for PostgreSQL database:

```heroku pg:psql -a rocky-cove-23591```

```\copy search_paper FROM 'DB' DELIMITER ';' CSV```

```rocky-cove-23591::DATABASE=> CREATE TABLE papers```

```rocky-cove-23591::DATABASE-> (CONFERENCE char(50), URL char(500), TITLE char(500), AUTHORS char(500), ABSTRACT char(5000), CITATIONS integer);```
