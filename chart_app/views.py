from django.shortcuts import render

from .models import City, Event


def index(request):
    cities = City.get_states()
    events = Event.get_alerts()

    context = {city.name: len([event for event in events if event.city_id.id == city.id]) for city in cities}
    sorted_tuples = sorted(context.items(), key=lambda item: item[1])
    context = {key: value for key, value in sorted_tuples}

    if request.method == 'GET':
        return render(request=request, template_name='chart_app/chart.html', context={'data': context.values(),
                                                                                      'labels': context.keys()})
