from rest_framework import serializers
from models import News

class NewsSerializer(serializers.Serializer):
    url = serializers.CharField(required=True, max_length=500)
    story = serializers.CharField(required=True, max_length=50000)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.url = attrs.get('url', instance.url)
            instance.story = attrs.get('story', instance.story)
        return News(attrs.get('url'), attrs.get('story'))
