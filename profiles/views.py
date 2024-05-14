from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfilSerializer

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfilSerializer(profiles, many=True)
        return Response(serializer.data)