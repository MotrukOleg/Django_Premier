from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from premier_django import NetworkHelper
from premier_django.models import stadium
from premier_django.repositories.repositories import PlayerRepository
from premier_django.repositories_manager import RepositoryManager
from premier_django.serializers import UserSerializer, MatchSerializer, PlayerSerializer, ClubSerializer, \
    PlayerStatsSerializer, StadiumSerializer


class ClubViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = RepositoryManager.club.get_all()
    serializer_class = ClubSerializer

    def list(self, request):
        clubs = RepositoryManager.club.get_all()
        serializer = self.serializer_class(clubs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        club = RepositoryManager.club.get_by_id(pk)
        serializer = self.serializer_class(club)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            RepositoryManager.club.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        club = RepositoryManager.club.get_by_id(pk)
        serializer = self.serializer_class(club, data=request.data)
        if serializer.is_valid():
            RepositoryManager.club.update(pk, **serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        club = RepositoryManager.club.get_by_id(pk)
        serializer = self.serializer_class(club)
        RepositoryManager.club.delete(pk)
        return Response(serializer.data)
class PlayerViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated]
    queryset = RepositoryManager.player.get_all()
    serializer_class = PlayerSerializer
    repository = PlayerRepository()

    def list(self, request):
        players = self.repository.get_all()
        serializer = self.serializer_class(players, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        player = self.repository.get_by_id(pk)
        serializer = self.serializer_class(player)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.repository.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        player = RepositoryManager.player.get_by_id(pk)
        serializer = self.serializer_class(player, data=request.data)
        if serializer.is_valid():
            RepositoryManager.player.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        RepositoryManager.player.delete(pk)
        return Response(status=204)
class MatchViewSet(viewsets.ModelViewSet):
  #  permission_classes = [IsAuthenticated]
    queryset = RepositoryManager.match.get_all()
    serializer_class = MatchSerializer

    def list(self, request):
        matches = RepositoryManager.match.get_all()
        serializer = self.serializer_class(matches, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        match = RepositoryManager.match.get_by_id(pk)
        serializer = self.serializer_class(match)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            RepositoryManager.match.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        match = RepositoryManager.match.get_by_id(pk)
        serializer = self.serializer_class(match, data=request.data)
        if serializer.is_valid():
            RepositoryManager.match.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        RepositoryManager.match.delete(pk)
        return Response(status=204)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StadiumViewSet(viewsets.ModelViewSet):
    queryset = RepositoryManager.stadium.get_all()
    serializer_class = StadiumSerializer

    def list(self, request):
        stadiums = RepositoryManager.stadium.get_all()
        serializer = self.serializer_class(stadiums, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stadium = RepositoryManager.stadium.get_by_id(pk)
        serializer = self.serializer_class(stadium)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            RepositoryManager.stadium.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        stadium = RepositoryManager.stadium.get_by_id(pk)
        serializer = self.serializer_class(stadium, data=request.data)
        if serializer.is_valid():
            RepositoryManager.stadium.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        RepositoryManager.stadium.delete(pk)
        return Response(status=204)

def item_list(request):
    items = NetworkHelper.get_list('users')

    return render(request, 'API/item_list.html', {'items': items})
def delete_item(request, item_id):
    success = NetworkHelper.delete_item('delete' , item_id)

    if success:
        return redirect('item_list')
    else:
        return JsonResponse({'SUCCESS': 'Successfully deleted'}, status=200)

class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = RepositoryManager.player_stat.get_all()
    serializer_class = PlayerStatsSerializer

    def list(self, request):
        queryset = RepositoryManager.player_stat.get_all()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

    def retrieve(self, request, pk=None):
        queryset = RepositoryManager.player_stat.get_by_id(pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            RepositoryManager.player_stat.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        queryset = RepositoryManager.player_stat.get_by_id(pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            RepositoryManager.player_stat.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        RepositoryManager.player_stat.delete(pk)
        return Response(status=204)

class TopScorersAPIView(APIView):
    def get(self, request):
        queryset = RepositoryManager.player_stat.get_top_scorers()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class AvgGoalsAPIView(APIView):
    def get(self, request):
        queryset = RepositoryManager.standing.get_avg_goals_by_club()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class TopGoalsPerMatchAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.match_stat.get_high_scoring_matches()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class PercentWinsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_percentage_wins()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class CardsStatAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.player_stat.get_cards_stat()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class StadiumCapacityAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.stadium.get_stadium_capacity()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class PlayerStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.player_stat.get_all()
        df = read_frame(queryset)
        stats = df.describe(include=[int , float])
        stats = stats.to_dict()

        return Response(stats)

class ClubStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_all()
        df = read_frame(queryset)
        stats = df.describe(include=[int, float])
        stats = stats.to_dict()

        return Response(stats)

class GroupedStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_all().filter(points__gt=0).values('club').annotate(avg_points = Avg('points'))
        df = read_frame(queryset)
        stat = df.describe(include=[int , float])
        stat = stat.to_dict()
        return Response(stat)

class GoalStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.goal.get_stats_for_each_player_in_each_match()
        return Response(queryset)

class MatchPossessionAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.match.get_possession_stats()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))