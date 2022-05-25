import requests
import datetime

from django.db import models
from django.utils import timezone

from .utils import X_API_Key


class City(models.Model):
    name = models.CharField(max_length=255, null=False)
    state_id = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "cities"

    @classmethod
    def get_states(cls):
        states = cls.objects.all()
        if not states:
            url = 'https://alerts.com.ua/api/states'
            response = requests.get(url, headers={'X-API-Key': X_API_Key})
            states = response.json().get('states', None)
            if states:
                states = [cls.objects.create(name=state.get('name', None), state_id=state.get('id', None))
                          for state in states]
        return states


class Event(models.Model):
    date = models.DateTimeField()
    date_create = models.DateTimeField(auto_now_add=True)
    city_id = models.ForeignKey(to=City, on_delete=models.CASCADE, null=False, related_name='event')

    @classmethod
    def get_alerts(cls):
        alerts = cls.objects.all()
        states = {state.state_id: state for state in City.objects.all()}

        if not alerts:
            url = 'https://alerts.com.ua/api/history'
            response = requests.get(url, headers={'X-API-Key': X_API_Key})
            alerts = [cls.objects.create(date=item.get('date'), city_id=states.get(item.get('state_id')))
                      for item in response.json()
                      if item.get('alert') is True]
            return alerts

        if max([alert.date_create for alert in alerts]) + datetime.timedelta(minutes=2) < timezone.now():
            url = 'https://alerts.com.ua/api/history'
            response = requests.get(url, headers={'X-API-Key': X_API_Key})

            [cls.objects.create(date=item.get('date'), city_id=states.get(item.get('state_id')))
             for item in response.json()
             if item.get('alert', False) is True
             and datetime.datetime.strptime(item.get('date'), '%Y-%m-%dT%H:%M:%S%z') > max(
                [alert.date for alert in alerts])
             ]

            alert = alerts[0]
            alert.date_create = timezone.now()
            alert.save()

            return cls.objects.all()

        return alerts
