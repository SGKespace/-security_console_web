from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def get_duration(visit):  # время нахождения в хранилище
    if not visit.leaved_at:
        return (timezone.localtime() - visit.entered_at).total_seconds()
    return (visit.leaved_at - visit.entered_at).total_seconds()


def format_duration(time_delta):  # Делаем нужный для вывода формат
    return '{:02}:{:02}:{:02}'.format(int(time_delta // 3600),
                                      int(time_delta % 3600 // 60),
                                      int(time_delta % 60),
                                      )


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()[0]
    # Программируем здесь

    this_passcard_visits = [
        {
            'entered_at': '11-04-2018',
            'duration': '25:03',
            'is_strange': False
        },
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
