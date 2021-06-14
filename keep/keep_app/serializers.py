from rest_framework import serializers
from keep_app.models import KeepApp


class KeepSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeepApp
        fields = ('id',
                  'title',
                  'status',
                  'due_date')
