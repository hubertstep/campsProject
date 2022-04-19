from rest_framework import serializers
from camps.models import Employee, Parent, Group, Activity, Participant, ProgramActivity


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'phone_number', 'email_address', 'birth_date', 'position']
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=50)
    # surname = serializers.CharField(max_length=100)
    # phone_number = serializers.CharField(max_length=20)
    # email_address = serializers.EmailField()
    # birth_date = serializers.DateField(required=False)
    # position = serializers.CharField(max_length=2)
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Employee` instance, given the validated data.
    #     """
    #     return Employee.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Employee` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.surname = validated_data.get('surname', instance.surname)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.email_address = validated_data.get('email_address', instance.email_address)
    #     instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    #     instance.position = validated_data.get('position', instance.position)
    #     instance.save()
    #     return instance


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'name', 'surname', 'phone_number', 'email_address']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'employee', 'name']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'groups', 'name', 'start_time', 'end_time', 'is_program']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'surname', 'birth_date', 'room', 'email_address', 'parents', 'groups']


class ProgramActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramActivity
        fields = ['name']
