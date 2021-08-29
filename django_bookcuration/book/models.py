from django.db import models

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=1000)
    searchsubject = models.CharField(db_column='searchSubject', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)
    writer = models.CharField(max_length=100, blank=True, null=True)
    translator = models.CharField(max_length=100, blank=True, null=True)
    painter = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publishdate = models.CharField(db_column='publishDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    intro = models.CharField(max_length=1000, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    authorintro = models.CharField(max_length=1000, blank=True, null=True)
    categorytop = models.CharField(db_column='categoryTop', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categorymiddle = models.CharField(db_column='categoryMiddle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categorybottom = models.CharField(db_column='categoryBottom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bid = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    review = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'