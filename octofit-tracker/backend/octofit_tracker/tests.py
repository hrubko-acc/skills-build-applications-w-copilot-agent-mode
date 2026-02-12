from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(id=1, name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(id=2, name='Test Team 2', description='Another test team')
        user = User.objects.create(id=1, email='test@example.com', username='TestUser', team_id=team.id, is_superhero=True)
        self.assertEqual(user.email, 'test@example.com')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(id=3, name='Test Team 3', description='Another test team')
        user = User.objects.create(id=2, email='test2@example.com', username='TestUser2', team_id=team.id, is_superhero=False)
        activity = Activity.objects.create(id=1, user_id=user.id, type='Running', duration=30, date='2026-02-10')
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(id=1, name='Test Workout', description='A test workout')
        self.assertEqual(workout.name, 'Test Workout')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(id=4, name='Test Team 4', description='Another test team')
        leaderboard = Leaderboard.objects.create(id=1, team_id=team.id, points=100)
        self.assertEqual(leaderboard.points, 100)
