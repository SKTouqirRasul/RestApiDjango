from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from .serializers import UserRegisterSerializer,ChangePasswordSerializer,LogINSerializer
from rest_framework import generics
from rest_framework import status

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()

class AuthView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LogINSerializer

    def post(self,request):
        # #if request.user.is_authenticated():
        #     return Response({'details':'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username,password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact = username)
        )
        if qs.count()==1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user=user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token,user,request=request)
                return Response(response)


        return Response('invalid credentials')


class RegisterAPIView(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    #model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        # payload = jwt_payload_handler(self.object)
        # token = jwt_encode_handler(payload)
        # print(token)
        # print(self.object)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."],'user':self.object.username}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








# class RegisterAPIView(APIView):
#     permission_classes =[permissions.AllowAny]
#
#     def post(self,request,*args,**kwargs):
#         if request.user.is_authenticated():
#             return Response('user already register')
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#
#         qs = User.objects.filter(
#             Q(username_iexact = username)|
#             Q(email_iexact = email)
#         )
#
#         if password !=password2:
#             return Response('unmatch password')
#
#         if qs.exists():
#             return Response('user alrady exists')
#
#         else:
#             user = User.objects.create(username=username,email=email)
#             user.set_password(password)
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token,user,request=request)
#             return Response(response, status = 201)
#         return Response ({'details':'invalid request'},status = 400)
