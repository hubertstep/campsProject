from django.test import TestCase
from .models import Employee, Parent, Group, Activity, Participant, ProgramActivity
from datetime import datetime, timedelta


class EmployeeTestCase(TestCase):
    def setUp(self) -> None:
        Employee.objects.create(name='kuba', surname='roman', phone_number='000000000', email_address='kuba@gmail.com', position='MG')

    def test_employee_str(self):
        """Str method returns correct string"""
        employee = Employee.objects.get(name='kuba')
        self.assertEquals(str(employee), 'kuba roman')


class ParentTestCase(TestCase):
    def setUp(self) -> None:
        Parent.objects.create(name='rafal', surname='roman', phone_number='000000000', email_address='rafal@gmail.com')

    def test_parent_str(self):
        """Str method returns correct string"""
        parent = Parent.objects.get(id=1)
        self.assertEquals(str(parent), 'rafal roman')


class GroupTestCase(TestCase):
    def setUp(self) -> None:
        employee = Employee.objects.create(name='kuba', surname='roman', phone_number='000000000', email_address='kuba@gmail.com', position='MG')
        Group.objects.create(name='zygzaki', employee=employee)

    def test_group_str(self):
        group = Group.objects.get(name='zygzaki')
        self.assertEquals(str(group), 'zygzaki')


class ActivityTestCase(TestCase):
    def setUp(self) -> None:
        employee = Employee.objects.create(name='kuba', surname='roman', phone_number='000000000',
                                           email_address='kuba@gmail.com', position='MG')
        start = datetime.now()
        end = datetime.now() + timedelta(hours=1)
        Activity.objects.create(name='wycieczka', start_time=start, end_time=end, is_program=True)

    def test_activity_str(self):
        activity = Activity.objects.get(name='wycieczka')
        self.assertEquals(str(activity), 'wycieczka')


class ParticipantTestCase(TestCase):
    def setUp(self) -> None:
        start = datetime.now()
        birth_date = datetime.now() - timedelta(days=10)
        Participant.objects.create(name='adam', surname='malysz', birth_date=birth_date, room='10', email_address='adam@gmail.com')

    def test_participant_str(self):
        participant = Participant.objects.get(name='adam')
        self.assertEquals(str(participant), 'adam malysz')


class ProgramActivityTestCase(TestCase):
    def setUp(self) -> None:
        ProgramActivity.objects.create(name='quady')

    def test_program_activity_str(self):
        program_activity = ProgramActivity.objects.get(name='quady')
        self.assertEquals(str(program_activity), 'quady')
