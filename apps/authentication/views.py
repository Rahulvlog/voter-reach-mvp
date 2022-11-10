
# Create your views here.
import io
import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import Profile, State, District, City


def login_view(request):
    form = LoginForm(request.POST) #or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


#create csv file uploaded files
def profile_upload(request):
    # declaring template
    template = "home/upload.html"
    data = Profile.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        # 'order': 'Order of the CSV should be name, email, address, phone, profile',
        'profiles': data
              }
    
    
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    print("data upload sucessfull")
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
        name=column[0],
        email=column[1],
        address=column[2],
        phone=column[3],
        profile=column[4]
        )
    context = {}
    return render(request, template, context)

# created dropdownchained state, city, district
def dependantfield(request):
    if request.method == "POST":
        stateid = request.GET.get('state', None)
        districtid = request.GET.get('district', None)
        district = None
        city = None
    
        if stateid:
            getstate = State.objects.get(id=stateid)
            district = District.objects.filter(state=getstate)
        
        if districtid:
            getdistrict = District.objects.get(id=districtid)
            city = City.objects.filter(district=getdistrict)
        
    state= State.objects.all()
    district= District.objects.all()
    city= City.objects.all()
    return render(request, 'home/upload.html', locals())
    