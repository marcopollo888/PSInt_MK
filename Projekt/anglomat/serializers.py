from rest_framework import serializers
from .models import Verb, Numeral

class VerbSerializer(serializers.HyperlinkedModelSerializer):
    verbs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="verb-detail")
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Verb
        fields = ['pk','infinitive', 'past_tense','past_participle','translation']


class NumeralSerializer(serializers.HyperlinkedModelSerializer):
    numerals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='numeral-detail')
    class Meta:
        model = Numeral
        fields = ['pk','cardinal_number','ordinal_number', 'translation']

class UserVerbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Verb
        fields = ['url','infinitive']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    verbs = UserVerbSerializer(many=True,read_only=True)
    class Meta:
        model = Verb
        fields =['url','pk','username','verbs']