from django.db import models
from apps.autor.models import Autor
from .managers import BooksManager, CategoryManager

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)
    objects = CategoryManager()

    def __str__(self):
        return f"{str(self.id)} {self.name}"

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category_book")
    autors = models.ManyToManyField(Autor)
    title = models.CharField(max_length=50)
    release_date = models.DateField("Realease date")
    cover = models.ImageField(upload_to="cover")
    views = models.PositiveIntegerField()
    objects = BooksManager()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    



# --> COPY book_book TO 'D:/data/book_data.csv' WITH CSV HEADER;

# --> COPY book_book FROM 'D:/data/book_data.csv' DELIMITER ',' CSV HEADER;

# --> ALTER SEQUENCE book_book_autors_id_seq RESTART WITH 1;

# --> ALTER SEQUENCE book_book_autors_id_seq RESTART WITH 1;