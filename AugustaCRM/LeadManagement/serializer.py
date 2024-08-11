from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    Created = serializers.DateTimeField()
    Email = serializers.EmailField()
    Name = serializers.CharField()
    phone = serializers.CharField()
    Platform = serializers.CharField()
    status = serializers.CharField()

    def to_representation(self, instance):
        # Decode bytes to string if necessary
        for key, value in instance.items():
            if isinstance(value, bytes):
                instance[key] = value.decode('utf-8')
        return super().to_representation(instance)