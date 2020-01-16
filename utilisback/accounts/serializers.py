from rest_framework import serializers
from .models import Members

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model=Members
        fields=('id', 'first_name', 'last_name', 'email_address', 'wallet_address', 'country_of_origin', 'id_number')