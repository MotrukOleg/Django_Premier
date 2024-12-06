from django.test import TestCase

from .models import club, player, match_info
from .forms import ClubForm, PlayerForm

class ClubModelTest(TestCase):
    def test_string_representation(self):
        club_name = club(name='Test Club')
        self.assertEqual(str(club_name), club_name.name)

class PlayerModelTest(TestCase):
    def test_string_representation(self):
        player_name = player(player_name='Test Player')
        self.assertEqual(str(player_name), player_name.player_name)

class MatchInfoModelTest(TestCase):
    def test_string_representation(self):
        club1 = club(name='Test Club')
        club2 = club(name='Test2 Club')
        match = match_info(home_team=club1, away_team=club2, date='2020-01-01', home_team_goals=1, away_team_goals=2)
        self.assertEqual(str(match), club1.name + ' vs ' + club2.name + ' ' + str(match.date) + ' ' + str(match.home_team_goals) + ':' + str(match.away_team_goals))

class ClubFormTest(TestCase):
    def test_form_no_data(self):
        form = ClubForm(data={})
        self.assertFalse(form.is_valid())