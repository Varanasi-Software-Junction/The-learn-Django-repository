from django.db import models


# Create your models here.
class BooksModel(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    price = models.IntegerField()


    def __str__(self):
        return "Book Name={0}, Subject={1}, Price={2} ".format(self.bookname, self.subject, self.price)
