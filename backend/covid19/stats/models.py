from django.db import models

class LocationBase(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    lon = models.FloatField('Longitude', blank=True, null=True)
    lat = models.FloatField('Latitude', blank=True, null=True)
    population = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(LocationBase):
    class Meta:
        verbose_name_plural = 'Countries'


class Region(LocationBase):
    country = models.ForeignKey(to=Country, on_delete=models.PROTECT, related_name='regions')


class City(LocationBase):
    region = models.ForeignKey(to=Region, on_delete=models.PROTECT, related_name='cities')

    class Meta:
        verbose_name_plural = 'Cities'


class StatsBase(models.Model):
    date = models.DateField()
    tested = models.IntegerField(blank=True, null=True)
    infected = models.IntegerField(blank=True, null=True)
    hospitalized = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} stats on {}'.format(self.get_location().name, self.date)

    def get_location(self):
        raise NotImplementedError


class CountryStats(StatsBase):
    country = models.ForeignKey(to=Country, on_delete=models.PROTECT, related_name='stats')

    class Meta:
        verbose_name_plural = 'Country Stats'

    def get_location(self):
        return self.country


class RegionStats(StatsBase):
    region = models.ForeignKey(to=Region, on_delete=models.PROTECT, related_name='stats')

    class Meta:
        verbose_name_plural = 'Region Stats'

    def get_location(self):
        return self.region


class CityStats(StatsBase):
    city = models.ForeignKey(to=City, on_delete=models.PROTECT, related_name='stats')

    class Meta:
        verbose_name_plural = 'City Stats'

    def get_location(self):
        return self.city



