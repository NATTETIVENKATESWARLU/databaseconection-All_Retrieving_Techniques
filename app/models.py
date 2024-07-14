from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=30,primary_key=True)
    def __str__(self) -> str:
        return self.topic_name


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=25,unique=True)
    url=models.URLField(max_length=40)
    def __str__(self) -> str:
        return self.name

class Aceess_records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self) -> str:
        return str(self.date)
    

#byusing shell insert data

'''

D:\django_1\django\Scripts\databaseconection>python manage.py shell
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from app.models import *


In [3]: Topic.objects.all()
Out[3]: <QuerySet [<Topic: cricket>]>



In [5]: b=Topic.objects.create(topic_name='foball')

In [6]: b.save()


In [7]: b
Out[7]: <Topic: foball>


In [8]: b=Topic.objects.get_or_create(topic_name='kabbadi')

In [9]: b
Out[9]: (<Topic: kabbadi>, True)



In [10]: b=Topic.objects.get_or_create(topic_name='kabbadi')[0]

In [11]: b
Out[11]: <Topic: kabbadi>

In [12]: b.save()




In [14]: d=Webpage.objects.create(topic_name=b,name='venkey',url='http:venkey.com')

In [15]: d.save()



In [18]: d=Webpage.objects.get_or_create(topic_name=b,name='mass',url='http:mass.com')[0]

In [19]: d.save()



In [20]: d=Webpage.objects.get_or_create(topic_name=b,name='mass',url='http:mass.com')[0]

In [21]: d.save()










----> 1 d=Webpage.objects.create(topic_name=b,name='mass',url='http:mass.com')[0]



In [23]: d=Webpage.objects.create(topic_name=b,name='mass',url='http:mass.com')
---------------------------------------------------------------------------


In [24]: d=Webpage.objects.get_or_create(topic_name=b,name='mass',url='http:mass.com')[0]





In [30]: c=Aceess_records.objects.get_or_create(name=d,date='2000-01-19')[0]

In [31]: c.save()

In [32]: exit()






'''