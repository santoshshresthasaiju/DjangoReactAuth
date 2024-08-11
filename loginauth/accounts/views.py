from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView

class RegisterView(APIView):
    
    def post(self, request):
        try:
            serializer = UserSerializer(data = request.data)
            if not serializer.is_valid():
                return Response({
                    'status': 403,
                    'errors' : serializer.errors
                })
            serializer.save()
            return Response({'status': 200 , 'message' : 'an OTP has sent on your number and email'})  
        except Exception as e:
            print(e)
            
            return Response({'status' : 404, 'error' : 'something went wrong'})
