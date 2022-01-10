from django.db import models


class WhoIsData(models.Model):
    domain_name = models.CharField(max_length=255)
    registrant_name = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    expire_date = models.DateTimeField()

    def __unicode__(self):
        return "domain_name= %s; register_name= %s; created= %s; expired= %s;" % (self.domain_name, self.registrant_name,
                                                                                  self.create_date, self.expire_date)


class WhoIsDataHeader(models.Model):
    name = models.CharField(max_length=255)
    whois_data = models.ManyToManyField('WhoIsData', blank=True)

    def __unicode__(self):
        return "%s" % self.name
