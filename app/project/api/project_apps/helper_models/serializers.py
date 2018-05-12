from rest_framework import serializers

from project.helper_models.models import Year, CalendarWeek


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class CalendarWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarWeek
        fields = '__all__'
