from rest_framework import serializers

from .models import *

class ForwardCountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = County
        fields = ['name', 'url']

class ForwardCongressionalDistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CongressionalDistrict
        fields = ['cd116fp', 'url']

class ForwardUrbanAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrbanArea
        fields = ['name10', 'url']

# TODO: show counties + geom when not in List View
class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        exclude = ['geom']

class StateDetailSerializer(serializers.HyperlinkedModelSerializer):
    counties = ForwardCountySerializer(source='get_counties', many=True)
    congressional_districts = ForwardCongressionalDistrictSerializer(source='get_congressionaldistricts', many=True)
    urban_areas = ForwardUrbanAreaSerializer(source='get_urbanareas', many=True)

    class Meta:
        model = State
        fields = '__all__'

class CountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = County
        exclude = ['geom']

class CountyDetailSerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer(source='get_state')
    congressional_districts = ForwardCongressionalDistrictSerializer(source='get_congressionaldistricts', many=True)
    urban_areas = ForwardUrbanAreaSerializer(source='get_urbanareas', many=True)

    class Meta:
        model = County
        fields = '__all__'

class UrbanAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrbanArea
        exclude = ['geom']

class UrbanAreaDetailSerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer(source='get_state')
    counties = CountySerializer(source='get_counties', many=True)

    class Meta:
        model = UrbanArea
        fields = '__all__'

class CongressionalDistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CongressionalDistrict
        exclude = ['geom']

class CongressionalDistrictDetailSerializer(serializers.HyperlinkedModelSerializer):
    state = StateSerializer(source='get_state')
    counties = CountySerializer(source='get_counties', many=True)

    class Meta:
        model = CongressionalDistrict
        fields = '__all__'
