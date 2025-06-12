from django.contrib import admin
from django.db import models as djmodels

from .language import LanguageAdmin
from .unit import UnitAdmin
from .activity import ActivityAdmin
from .activity_enroll import ActivityEnrollAdmin
from .activity_event import ActivityEventAdmin
from .activity_event_work import EventWorkAdmin