from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True),
            User(email='captain@marvel.com', username='Captain America', team=marvel, is_superhero=True),
            User(email='spiderman@marvel.com', username='Spider-Man', team=marvel, is_superhero=True),
            User(email='batman@dc.com', username='Batman', team=dc, is_superhero=True),
            User(email='superman@dc.com', username='Superman', team=dc, is_superhero=True),
            User(email='wonderwoman@dc.com', username='Wonder Woman', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-10')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-11')
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date='2026-02-12')

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Strength', description='Strength workout for heroes')
        workout2 = Workout.objects.create(name='Speed Training', description='Speed workout for heroes')
        workout1.suggested_for.set([users[0], users[1], users[4]])
        workout2.suggested_for.set([users[2], users[3], users[5]])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
