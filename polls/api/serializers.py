from vote.models import( County ,
                         Country ,
                         Constituency ,
                         Ward ,
                         President ,
                         Governor,
                         Senator ,
                         Womensrep ,
                         Memberofparliament ,
                         MemberofCountyAssembly,
                         RallyDate,
                         Party,
                         )
from rest_framework import serializers

class RallyDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RallyDate
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('Name' , 'Slug')

class CountySerializer(serializers.ModelSerializer):
    class Meta:
         model = County
         fields = ('Slug' , 'Name')

class ConstituencySerializer(serializers.ModelSerializer):
    County = CountySerializer()
    class Meta:
        model = Constituency
        fields = ('County' , 'Name' , 'Slug' )

class WardSerializer(serializers.ModelSerializer):
    constituency = ConstituencySerializer()
    class Meta:
        model = Ward
        fields = ('constituency' , 'Name')

class PresidentSerializer(serializers.ModelSerializer):
    Country = CountrySerializer()
    Party = PartySerializer()
    RallyDate = RallyDateSerializer()
    class Meta:
        model = President
        fields = ('Country' , 'Party' ,'First_name' , 'Middle_name' ,
                   'Last_name', 'RallyDate' )

class GovernorSerializer(serializers.ModelSerializer):
    Party = PartySerializer()
    County = CountySerializer()
    RallyDate = RallyDateSerializer()
    class Meta:
        model  = Governor
        fields = ('County' , 'Party' , 'First_name' , 'Middle_name',
                  'Last_name' , 'RallyDate')

class SenatorSerializer(serializers.ModelSerializer):
    County = CountySerializer()
    RallyDate = RallyDateSerializer()
    Party = PartySerializer()

    class Meta:
        model = Senator
        fields = ('County' , 'Party' , 'First_name' , 'Middle_name',
                  'Last_name' , 'RallyDate')

class WomensrepSerializer(serializers.ModelSerializer):
    Party = PartySerializer()
    RallyDate = RallyDateSerializer()
    County = CountySerializer()

    class Meta:
        model = Womensrep
        fields = ('County' , 'Party' , 'First_name' , 'Middle_name' ,
                      'Last_name' , 'RallyDate')

class MemberofparliamentSerializer(serializers.ModelSerializer):
    party = PartySerializer()
    rallydate = RallyDateSerializer()
    constituency = ConstituencySerializer()

    class Meta:
        model = Memberofparliament
        fields = ('constituency' , 'party' , 'First_name' , 'Middle_name' ,
                      'Last_name' , 'rallydate')

class MemberofCountyAssemblySerializer(serializers.ModelSerializer):
    party = PartySerializer()
    rallydate = RallyDateSerializer()
    ward = WardSerializer()

    class Meta:
        model = Womensrep
        fields = ('ward' , 'party' , 'First_name' , 'Middle_name' ,
                      'Last_name' , 'rallydate')
