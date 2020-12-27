from django.contrib.auth import authenticate
from rest_framework import serializers
from restApp.quickstart.models import *
from .models import userProfile

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField(max_length=30, required=True)
#     password = serializers.CharField(max_length=128, required=True)
#     adminRole = serializers.BooleanField(required=True)

    # def create(self, validated_data):
    #
    #     return userProfile.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.adminRole = validated_data.get('adminRole', instance.adminRole)
    #


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class userProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)

    user = userSerializer(read_only=True)





    class Meta:
        model = userProfile
        fields = '__all__'





class CardSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField()
    startDate = serializers.DateTimeField()
    endDate = serializers.DateTimeField()
    balance = serializers.IntegerField()

    def create(self, validated_data):

        return Card.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.startDate = validated_data.get('startDate', instance.startDate)
        instance.endDate = validated_data.get('endDate', instance.endDate)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.number = validated_data.get('number', instance.number)




    class Meta:
        model = Card
        fields = '__all__'


class LogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    user = userProfileSerializer(many=False, read_only=True)
    card = CardSerializer(many=False, read_only=True)

    amount = serializers.IntegerField()
    timeDate = serializers.DateTimeField()

    action = serializers.ChoiceField(choices= Log.ACTION)

    def create(self, validated_data):
        return Log.objects.create(**validated_data)

    def update(self, instance, validated_data):


        instance.user = validated_data.get('user', instance.user)
        instance.card = validated_data.get('card', instance.card.id)
        instance.action = validated_data.get('action', instance.action)
        instance.amount = validated_data.get('amount', instance.amount)

    class Meta:
        model = Log
        fields = [ 'card', 'user_id', 'action', 'amount', 'timeDate']






# class RegistrationSerializer(serializers.ModelSerializer):
#     """
#     Creates a new user.
#     Email, username, and password are required.
#     Returns a JSON web token.
#     """
#
#     # The password must be validated and should not be read by the client
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True,
#     )
#
#     # The client should not be able to send a token along with a registration
#     # request. Making `token` read-only handles that for us.
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password', 'token',)
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
# class LoginSerializer(serializers.Serializer):
#     """
#     Authenticates an existing user.
#     Email and password are required.
#     Returns a JSON web token.
#     """
#     email = serializers.EmailField(write_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#
#     # Ignore these fields if they are included in the request.
#     username = serializers.CharField(max_length=255, read_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         """
#         Validates user data.
#         """
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email address is required to log in.'
#             )
#
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#
#         user = authenticate(username=email, password=password)
#
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )
#
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
#
#         return {
#             'token': user.token,
#         }


