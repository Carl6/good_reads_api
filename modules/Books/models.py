from django.db import models
from modules.Authors.models import Author
#from modules.Users.models import User
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

LIT_GENRE = (
    ("sf","science fiction"),
    ("dr","drama"),
    ("ft","fantasy"),
    ("bg","biography"),
    ("ht","history"),
    ("ot","others")
)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=18,unique=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name = "books") #1er arg es la clase de Author
    date_published = models.DateField()
    cover_photo = models.URLField()
    summary = models.TextField()
    rating = models.DecimalField(decimal_places=2,max_digits=3)
    lit_genre = models.CharField(max_length=80,choices=LIT_GENRE)
    tags = ArrayField(
        models.CharField(max_length=50),
        size=5
    )

#relacion book/autor, se va a llamar books line 20


#cuando empecemos a crear objetos queremos reconocer los objetos de una forma representatia
    def __str__(self):
        return "Libro: %s" % self.name

class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    comment = models.TextField() 

    def __str__(self):
        return "Comment: %s to %s" % (self.user.name,self.book.name)