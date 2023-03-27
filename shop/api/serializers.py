from rest_framework import serializers

from goods.models import SuperCategory


class SuperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = (
            'id',
            'name',
            'slug',
        )
