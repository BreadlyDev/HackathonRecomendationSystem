from rest_framework import serializers

from . import models as m


class MusicByValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.MusicByValue
        fields = '__all__'
