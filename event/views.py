from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from event.models import UserDetail,Place,Service,MicroBlog

def signup(request):
    '''
    method : post

    required: username
              email
              password
              user type
              address
              phone_no

    '''
    if request.method=="POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get("email")
        user_type=request.POST.get("user_type")
        user_address=request.POST.get("user_address")
        user_phone=request.POST.get("user_phone")

        exists = User.objects.filter(username=username).exists()

        if not exists:
            userinfo = User.objects.create_user(username,email,password)
            profile=UserDetail.objects.create(userinfo=userinfo,user_type=user_type,user_address=user_address,user_phone=user_phone)
            profile.save()
            return redirect('/login/')
    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(f'/home/{user.pk}/')
        elif user is None:
            return redirect(f'/login/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('invalid user')
    return render(request,"login.html")

def signout(request):
    logout(request)
    return render(request,"login.html")

def home(request,userid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        places = Place.objects.all()
        services = Service.objects.all()
        return render(request,"home.html", {"userinfo":user, "userdetail":userdetail , "places":places , "services":services})
    else:
        return render(request,"home.html")

def aboutus(request,userid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        return render(request,"aboutus.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")

def blog(request,userid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        blog = MicroBlog.objects.order_by('-id')
        return render(request,"blog.html", {"userinfo":user, "userdetail":userdetail , "blog":blog})
    else:
        return render(request,"login.html")


def checkout(request,userid,bookid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        return render(request,"checkout.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")

def all_services(request,userid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        services = Service.objects.all()
        return render(request,"services.html", {"userinfo":user, "userdetail":userdetail , "services":services})
    else:
        return render(request,"login.html")

def service(request,userid,serviceid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        return render(request,"service.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")

def place(request,userid,placeid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        return render(request,"place.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")

def all_places(request,userid):
    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        places = Place.objects.all()
        return render(request,"places.html", {"userinfo":user, "userdetail":userdetail , "places":places })
    else:
        return render(request,"login.html")

def createblog(request,userid):
    # <!-- user=models.ForeignKey(User,on_delete=models.CASCADE)
    # blog_title=models.CharField(max_length=20)
    # blog_content=models.TextField() -->

    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        if request.method == "POST":
            blog_title=request.POST["blog_title"]
            blog_content=request.POST["blog_content"]
            create_blog=MicroBlog.objects.create(user=user,blog_title=blog_title,blog_content=blog_content)
            return redirect(f"/blog/{user.pk}/")
        return render(request,"createblog.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")
   
      

def createplace(request,userid):
    # place_name=models.CharField(max_length=30)
    # place_address=models.TextField()
    # place_owner= models.ForeignKey('UserDetail',on_delete=models.CASCADE,limit_choices_to={'user_type': '2'})
    # place_description=models.TextField()
    # place_price=models.IntegerField(default=0)
    # place_image = models.ImageField(null=True, blank=True, upload_to="projects-images/") 


    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        if request.method=="POST":
            place_name=request.POST["place_name"]
            place_address=request.POST["place_address"]
            place_description=request.POST["place_description"]
            place_price=request.POST["place_price"]
            place_image=request.POST["place_image"]
            create_place=Place.objects.create(place_name=place_name,place_address=place_address,place_owner=user,place_description=place_description,place_price=place_price,place_image=place_image)
            return redirect(f"/home/{user.pk}/")
        return render(request,"createplace.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")

def createservice(request,userid):
    # service_name=models.CharField(max_length=20)
    # service_description=models.TextField()
    # service_price=models.IntegerField(default=0)
    # service_owner=models.ForeignKey(User,on_delete=models.CASCADE)

    if request.user.is_authenticated:
        user = request.user
        userdetail = user.userdetail
        if request.method=="POST":
            service_name=request.POST["service_name"]
            # place_address=request.POST["place_address"]
            service_description=request.POST["service_description"]
            service_price=request.POST["service_price"]
            service_image=request.POST["service_image"]
            create_service=Service.objects.create(service_name=service_name,service_owner=user,service_description=service_description,service_price=service_price,service_image=service_image)
            return redirect(f"/home/{user.pk}/")
        return render(request,"createservice.html", {"userinfo":user, "userdetail":userdetail})
    else:
        return render(request,"login.html")
@login_required
def account(request,userid):
    user = request.user
    user_detail = user.userdetail
    print(user_detail)
    return render(request,"account.html",{'userinfo':user , 'userdetail':user_detail})

# Create your views here.
