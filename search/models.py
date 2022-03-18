# # Create your models here.
from adaptor.model import CsvModel
from adaptor.fields import CharField, IntegerField, BooleanField, FloatField
from django.db import models
# # Create your models here.
from django.contrib import admin

class Paper(models.Model):
    # title = models.CharField(max_length=50)
    # abstract= models.CharField(max_length=500)

    conference = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    
    authors = models.CharField(max_length=50)
    abstract= models.CharField(max_length=500)
    citations = models.IntegerField()


    def __str__(self):
        return self.title


    @admin.display(description='Number of authiors')
    def author_numbers(self):
        authors = self.authors
        author_list = authors.split(',')
        # return '%d’s' % (len(author_list))
        return len(author_list)
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # return '%d’s' % (self.birthday.year // 10 * 10)

    @admin.display(description='First author')
    def first_author(self):
        authors = self.authors
        author_list = authors.split(',')
        return author_list[0]


class myCsvModel(CsvModel):
    conference = CharField()
    url = CharField()
    title = CharField()
    authors = CharField()
    abstract = CharField()
    citations = IntegerField()
    # genre = CharField()
    # editors_choice = CharField()

    class Meta:
        delimiter = ";"
        # has_header = True
        dbModel = Paper

# class MyCSvModel(CsvModel):
#     name = CharField()
#     age = IntegerField()
#     length = FloatField()


#     class Meta:
#         delimiter = ";"