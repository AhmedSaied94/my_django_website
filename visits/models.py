from django.db import models

# Create your models here.


class Visit(models.Model):
    """
    Visit model
    used to store the visit data
    ip_address: the ip address of the visitor
    os: the operating system of the visitor
    browser: the browser of the visitor
    device: the device of the visitor
    date: the date of the visit
    """

    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    day = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name_plural = "Visits"
        ordering = ["-date"]
        unique_together = ["ip_address", "day"]


class VisitHits(models.Model):
    """
    VisitCount model
    visit: the visit object
    hits: the number of hits
    """

    visit = models.OneToOneField(Visit, on_delete=models.CASCADE, related_name="visit_hits")
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.visit} - {self.visit.day} - {self.hits}"

    class Meta:
        verbose_name_plural = "Visit Hits"
        ordering = ["-hits"]

    def increment_hits(self):
        self.hits += 1
        self.save()
        return self.hits
