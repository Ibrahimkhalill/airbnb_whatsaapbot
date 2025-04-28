from rest_framework import serializers
from .models import WhatsAppMessage

class WhatsAppMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsAppMessage
        fields = ['sender_name', 'message_text', 'reply']
