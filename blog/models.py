from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):     #this makes it so the admin page gives the actual title of each blog instead of "Blog Object 1" etc.
        return self.title

    def summary(self):     # lets us show only the first 100 characters of each post on the allblogs page
        return self.body[:100]

    def pub_date_pretty(self):   #changes the datetime from the exact date and time to date only with format Mon. date(#), 4-digit year
        return self.pub_date.strftime('%b %e %Y')
