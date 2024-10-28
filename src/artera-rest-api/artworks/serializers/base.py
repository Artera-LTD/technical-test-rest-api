from rest_framework.serializers import ModelSerializer
from artworks.models import Artworks
from users.serializers import ProfileSerializer

class ArtworksSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Artworks 
        fields = '__all__'