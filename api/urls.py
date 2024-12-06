from django.urls import path, include
from rest_framework import routers

from api import views

from .views import ClubViewSet, PlayerViewSet, MatchViewSet, UserViewSet, TopScorersAPIView, PlayerStatsAPIView, \
    ClubStatsAPIView, GroupedStatsAPIView

urlpatterns = [
    path('clubs_list/', ClubViewSet.as_view({'get': 'list'})),
    path('clubs/<int:pk>/', ClubViewSet.as_view({'get': 'retrieve'})),
    path('clubs_create/', ClubViewSet.as_view({'post': 'create'})),
    path('clubs_update/<int:pk>/', ClubViewSet.as_view({'put': 'update'})),
    path('clubs_delete/<int:pk>/', ClubViewSet.as_view({'delete': 'destroy'})),

    path('players_list/', PlayerViewSet.as_view({'get': 'list'})),
    path('players/<int:pk>/', PlayerViewSet.as_view({'get': 'retrieve'})),
    path('players_create/', PlayerViewSet.as_view({'post': 'create'})),
    path('players_update/<int:pk>/', PlayerViewSet.as_view({'put': 'update'})),
    path('players_delete/<int:pk>/', PlayerViewSet.as_view({'delete': 'destroy'})),

    path('matches_list/', MatchViewSet.as_view({'get': 'list'})),
    path('matches/<int:pk>/', MatchViewSet.as_view({'get': 'retrieve'})),
    path('matches_create/', MatchViewSet.as_view({'post': 'create'})),
    path('matches_update/<int:pk>/', MatchViewSet.as_view({'put': 'update'})),
    path('matches_delete/<int:pk>/', MatchViewSet.as_view({'delete': 'destroy'})),

    path('player_stats_list/', views.PlayerStatsViewSet.as_view({'get': 'list'})),
    path('player_stat_by_match/', views.GoalStatsAPIView.as_view(), name='player_stat_by_match'),
    path('match_possession/', views.MatchPossessionAPIView.as_view(), name='match_possession'),

    path('top_scorers/', TopScorersAPIView.as_view(), name='top_scorers'),
    path('avg_goals/', views.AvgGoalsAPIView.as_view(), name='avg_goals'),
    path('top_match_goals/', views.TopGoalsPerMatchAPIView.as_view(), name='top_match_goals'),
    path('percent_wins/', views.PercentWinsAPIView.as_view(), name='percent_wins'),
    path('cards_stat/', views.CardsStatAPIView.as_view(), name='cards_stat'),
    path('capacities/', views.StadiumCapacityAPIView.as_view(), name='capacities'),

    path('statistics/player/', PlayerStatsAPIView.as_view(), name='player_statistic'),
    path('statistics/club/', ClubStatsAPIView.as_view(), name='club_statistics'),
    path('statistics/grouped/', GroupedStatsAPIView.as_view(), name='grouped_statistics'),


]