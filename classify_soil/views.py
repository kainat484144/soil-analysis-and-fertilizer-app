from rest_framework.decorators import api_view
from rest_framework.response import Response


# curl --location '192.168.0.141:8000/api/?soil_image=hello.jpg'
# curl --location '192.168.0.141:8000/api/?soil_image=hello.jpg&soil_type=yes'

@api_view(['POST'])
def index(request):
    input_image = request.data['soil_image']
    soil_type = request.data['soil_type']
    print(input_image)
    return Response({
        'message': 'hello this is my api for django',
        'image': input_image,
        'soil_type': soil_type
    })
