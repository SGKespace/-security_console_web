from django.db import models
from django.utils import timezone


def get_duration(visit):
    if not visit.leaved_at:
        return (timezone.localtime() - visit.entered_at).total_seconds()
    return (visit.leaved_at - visit.entered_at).total_seconds()


def format_duration(time_delta):
    return '{:02}:{:02}:{:02}'.format(int(time_delta // 3600),
                                      int(time_delta % 3600 // 60),
                                      int(time_delta % 60),
                                      )


def is_visit_long(visit, minutes=60):
    return get_duration(visit) // 60 > minutes


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
