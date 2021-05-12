from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.IntegerField(default=50)
    pages=models.IntegerField()
    category=models.CharField(max_length=120)


    def __str__(self):
        return  self.book_name
#create table tablnmae, here djnago dynmaivally create table when migratoion and migrate chaiyumbo
#orm queries- objt relational mapper

#book object create chaiyuna query- insert into table name()
#here...
#book=Book(book_name="test1  ",author=tst1,price=123,pages=129,category="fiction")
#book.save()
#book1=Book(book_name="test2",author=tst2,price=155,pages=121,category="romance")
#book1.save()


#import model on shell- from book.models import Book

#list all - select * from d

#here books=Book.objects.all()



#update book set author='res'where id=1
#we have to fetch that particular bbok object

#book=Book.objects.get(id=1)
#book.author="hello"
#book.save()


#delete query
#book=Book.objects.get(id=1)
#book.delete()



#orm query for cretaiong onjt
#objt=class(fieldname="value", fieldname="value")
#book=Book()
#book.save()

#fetching corroseponding book objt
#book=Book.objects.get(id=1)

#fetch all object
#books=Book.objects.all()
#iterate over it
#for book in books:
#   print(book)