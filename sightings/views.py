from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Squirrel
from .forms import SquirrelForm

def index(request):
    return render(request, 'sightings/index.html', {})

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'sightings/info.html', context)

def statistics(request):
    obj = Squirrel.objects
    
    #Number of squirrels
    s_cnt = obj.count()
    
    #Age stats
    s_adult = obj.filter(Age='Adult').count()
    s_juv = obj.filter(Age='Juvenile').count()
    p_adult = s_adult/s_cnt
    p_juv = s_juv/s_cnt
    
    #Color stats
    s_gray = obj.filter(Primary_fur_color='Gray').count()
    s_cin = obj.filter(Primary_fur_color='Cinnamon').count()
    s_black = obj.filter(Primary_fur_color='Black').count()
    p_gray = s_gray/s_cnt
    p_cin = s_cin/s_cnt
    p_black = s_black/s_cnt
    
    #Location stats
    s_ground = obj.filter(Location='Ground Plane').count()
    s_above = obj.filter(Location = 'Above Ground').count()
    p_g = s_ground/s_cnt
    p_a = s_above/s_cnt
    
    #Activity stats
    s_run_chase = obj.filter(Running=True, Chasing=True).count()
    s_eat_forage = obj.filter(Eating=True, Foraging=True).count()
    p_r = s_run_chase/s_cnt
    p_e = p_eat_forate/s_cnt
    
    #Shift stats
    s_am = obj.filter(Shift='AM')
    s_pm = obj.filter(Shift='PM')
    p_am = s_am/s_cnt
    p_pm = s_pm/s_cnt
    
    context = {
        's_cnt':s_cnt,
        's_adult':s_adult,
        's_juv':s_juv,
        's_gray':s_gray,
        's_cin':s_cin,
        's_black':s_black ,
        's_ground':s_ground,
        's_above':s_above,
        ' s_run_chase': s_run_chase,
        's_eat_forage':s_eat_forage,
        's_am':s_am,
        's_pm':s_pm,
        'p_adult':p_adult,
        'p_juv':p_juv,
        'p_gray':p_gray,
        'p_cin':p_cin,
        'p_black':p_black,
        'p_g':p_g,
        'p_a':p_a,
        'p_r':p_r,
        'p_e':p_e,
        'p_am':p_am,
        'p_pm':p_pm,
    }
    return render(request, 'sightings/stats.html', context)

def map(request):
    obj = Squirrel.objects.all()
    return render(request, 'sightings/map.html', {'squirrels':obj})

def update_squirrel(request, sid):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=sid)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/info')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
    }
    return render(request, 'sightings/updatedata.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/info')

    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/add.html', context)

