from rest_framework import serializers
from .models import Verb, Numeral

class VerbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verb
        fields = ['pk','infinitive', 'past_tense','past_participle','translation']


class NumeralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Numeral
        fields = ['pk','cardinal_number','ordinal_number']