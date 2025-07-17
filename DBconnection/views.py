from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models.models import BodyOfWater, FishType, BaitType, FishingLog
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .serializers import FishingLogSerializer
# NOTE: where to create views
# views are where you define the function for api calls and that will call something else 

@api_view(['POST'])
def registerUser(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password  # with django user model the django handles the hashing!
        )
        return Response({"success": "User created successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')  
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id':  user.pk,
            'username': user.username
        })
    else:
        return Response({"error": "Invalid credentials"}, status=400)
    
@api_view(['POST'])
def logout_user(request):
    request.user.auth_token.delete() 
    return Response({"message": "Logged out successfully"})

@api_view(['GET', 'POST'])
def water_bodies(request):
    if request.method == 'GET':
        bodies = BodyOfWater.objects.all()
        data = [{
            'id': b.bow_id,
            'lat': b.lat,
            'lng': b.lng,
            'name': b.name
        } for b in bodies]
        return Response(data)
    if request.method == 'POST':
        name= request.data.get('name')
        lat = request.data.get('lat')
        lng = request.data.get('lng')
        try:
            user = BodyOfWater.objects.create(
                name=name,
                lat=lat,
                lng=lng 
            )
            return Response({"success": "Body of Water created in DB successfully"}, status=201)
        except Exception as e:
            return Response({"Body of Water error": str(e)}, status=400)

@api_view(['GET', 'POST'])
def fish_types(request):
    if request.method == 'GET':
        fishes = FishType.objects.all()
        data = [{
            'fish_id': f.fish_id,
            'name': f.name,
            'salt': f.salt,
            'fresh': f.fresh
        }for f in fishes]
        return Response(data)
    if request.method == 'POST':
        return Response("Wrong") # NOTE: Placeholder for POST to fish type submission
    
@api_view(['GET', 'POST'])
def bait_types(request):
    if request.method == 'GET':
        baits = BaitType.objects.all()
        data = [{
            'bait_id': bait.bait_id,
            'name': bait.name,
            'salt': bait.salt,
            'fresh': bait.fresh
        } for bait in baits]
        return Response(data)
    
@api_view(['POST'])
def submit_fish(request):
    name = request.data.get('name')
    salt = request.data.get('salt')
    fresh = request.data.get('fresh')
    try:
        fish = FishType.objects.create(
            name=name,
            salt=salt,
            fresh=fresh
        )
        return Response({"success": "Fish created successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    #fish_id = models.AutoField(primary_key=True, unique=True)
    #name = models.CharField(max_length=100, unique=True)
    #fresh = models.BooleanField(default = False)
    #salt = models.BooleanField(default = False)
    
@api_view(['POST'])
def submit_bait(request):
    name = request.data.get('name')
    salt = request.data.get('salt')
    fresh = request.data.get('fresh')
    try:
        bait = BaitType.objects.create(
            name=name,
            salt=salt,
            fresh=fresh,
        )
        return Response({"success": "Bait created successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
    
@api_view(['GET','POST'])
def submit_catch(request):
    if request.method == 'POST':
        bait_id = request.data.get('bait_id')
        bow_id = request.data.get('bow_id')
        user_id = request.data.get('user_id')
        fish_id = request.data.get('fish_id')
        try:
            catch = FishingLog.objects.create(
                bait_id_id= bait_id,
                bow_id_id = bow_id,
                user_id = user_id,
                fish_id_id = fish_id,
            )
            return Response({"success": "Catch has been logged"}, status = 201)
        except Exception as e:
            return Response({"error": str(e)}, status = 400)

@api_view(['POST'])
def get_fishing_logs(request):
    bow_id = request.data.get("bow_id")
    catches = FishingLog.objects.filter(bow_id=bow_id)
    serializer = FishingLogSerializer(catches, many=True)
    return Response(serializer.data)