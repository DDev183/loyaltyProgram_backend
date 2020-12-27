from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from restApp.quickstart.models import *
from restApp.quickstart.serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from restApp.quickstart.license import IsOwnerProfileOrReadOnly
from datetime import datetime


from .models import userProfile
# from .serializers import LoginSerializer
# from .serializers import RegistrationSerializer



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST', 'GET'])
# @permission_classes((permissions.AllowAny,))
# def user(request):
#
#     if request.method == 'GET':
#         users = userProfile.objects.all()
#         serializer = userProfileSerializer(users, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = userProfileSerializer(data=request.data)
#
#         if serializer.is_valid():
#             # print(User.objects.get(username=serializer.data.get('username')))
#
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))
def log(request):

    if request.method == 'GET':
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LogSerializer(data=request.data)

        if serializer.is_valid():
            # print(User.objects.get(username=serializer.data.get('username')))

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\

@api_view(['POST', 'GET', 'PUT'])
@permission_classes((permissions.IsAuthenticated,))
def card(request):


# TODO: Add endDate check
    if request.method == 'GET':

        if (len(request.query_params) == 0):
            card = Card.objects.all()
            serializer = CardSerializer(card, many=True)
            # print(card.filter(number=request.query_params.get('number')).get().balance)
            return Response(serializer.data)
        else :
            card = Card.objects.all()
            serializer = card.filter(number=request.query_params.get('number')).get().balance
            return Response(serializer)


    if request.method == 'PUT':
        card = Card.objects.all()
        currentCard = card.filter(number=request.data.get('number'))

        if request.data.get('action') == 'minus':
            print(request.data.get('action'))
            print(currentCard.get().balance)
            print(request.data.get('amount'))
            currentCard.update(balance =currentCard.get().balance - request.data.get('amount'))
            print(currentCard.get().balance)

            log = Log(user=request.user, card=currentCard.get(), amount=request.data.get('amount'), action='SELL')

            log.save()
            return Response(currentCard.get().balance)

        if request.data.get('action') == 'plus':
            print(request.data.get('action'))
            print(currentCard.get().balance)
            print(request.data.get('amount'))
            currentCard.update(balance =currentCard.get().balance + request.data.get('amount'))
            print(currentCard.get().balance)

            log = Log(user=request.user, card=currentCard.get(), amount=request.data.get('amount'), action='BONUS')

            log.save()
            return Response(currentCard.get().balance)




    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)


        if serializer.is_valid():
            # print(User.objects.get(username=serializer.data.get('username')))

            print(request.user.id)

            serializer.save()

            # log = Log(data=data)
            log = Log(user=request.user, card=serializer.instance, amount=serializer.validated_data.get('balance'), action='CREATE')

            log.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#
# class RegistrationAPIView(APIView):
#     """
#     Registers a new user.
#     """
#     permission_classes = [AllowAny]
#     serializer_class = RegistrationSerializer
#
#     def post(self, request):
#         """
#         Creates a new User object.
#         Username, email, and password are required.
#         Returns a JSON web token.
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(
#             {
#                 'token': serializer.data.get('token', None),
#             },
#             status=status.HTTP_201_CREATED,
#         )
#
#
# class LoginAPIView(APIView):
#     """
#     Logs in an existing user.
#     """
#     permission_classes = [AllowAny]
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         """
#         Checks is user exists.
#         Email and password are required.
#         Returns a JSON web token.
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)'




class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        print(user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]