from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404

from rest_framework.permissions import IsAuthenticated

from accountio.models import User

from ..serializers.profile import PrivateMeProfileSerializer


class PrivateMeProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeProfileSerializer

    def get_object(self):
        return get_object_or_404(User, email=self.request.user.email)
