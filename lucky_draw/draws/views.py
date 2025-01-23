from django.shortcuts import render
from .models import DrawResult
from django.http import JsonResponse
from datetime import datetime, timedelta
import random
from django.contrib.auth.decorators import login_required


def draw_results(request):
    selected_date = request.GET.get('date')
    current_datetime = datetime.now()

    if selected_date:
        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'draws/results.html', {
                'error': 'Invalid date format. Use YYYY-MM-DD.',
                'table_data': {},
                'selected_date': selected_date,
            })

        # Fetching the results, filtered by the selected date and not exceeding current date and time
        if selected_date == current_datetime.date():
            results = DrawResult.objects.filter(date=selected_date, time__lte=current_datetime.time())
        else:
            results = DrawResult.objects.filter(date=selected_date, date__lte=current_datetime.date())
    else:
        # Fetching all results not exceeding current date and time
        results = DrawResult.objects.filter(date=current_datetime.date(), time__lte=current_datetime.time())

    
    # Prepare the table data
    table_data = {}
    for result in results:
        time_str = result.time.strftime("%I:%M %p")  # Format time as AM/PM
        table_data[time_str] = {
            'royal': f"{result.royal:02}",
            'deluxe': f"{result.deluxe:02}",
            'casino': f"{result.casino:02}",
            'express': f"{result.express:02}",
            'gold_play': f"{result.gold_play:02}",
        }

    data = {
        'table_data': table_data,
        'selected_date': selected_date,
    }
    return render(request, 'draws/Shreelaxmilucky-Results.html', data)


def home(request):
    current_time = datetime.now()

    # Calculate the nearest draw time (a multiple of 15 minutes)
    minutes = (current_time.minute // 15) * 15
    draw_time = current_time.replace(minute=minutes, second=0, microsecond=0)
    if draw_time < current_time:
        draw_time += timedelta(minutes=15)
    last_draw_time = draw_time - timedelta(minutes=15)

     # Fetch the latest draw result based on the date and before the draw time
    last_draw_result = DrawResult.objects.filter(date=last_draw_time.date(), time=last_draw_time.time()).last()
    
    # import pdb; pdb.set_trace()
    time_to_draw = draw_time - current_time
    name = ''
    if not last_draw_result:
            record = DrawResult.objects.filter(date=last_draw_time.date(), time__lte=last_draw_time.time()).last()
            if record:
                name = record.name
    else:
        name= last_draw_result.name

    context = {
        'draw_time': draw_time.strftime('%I:%M %p'),
        'date': current_time.strftime('%m/%d/%Y'),
        'now_time': current_time.strftime('%I:%M:%S %p'),
        'time_to_draw': str(time_to_draw).split('.')[0],  # Remove microseconds
        'last_draw_time': last_draw_time.strftime('%I:%M %p'),
        'last_draw_result': {
            'royal': last_draw_result.royal if last_draw_result else None,
            'deluxe': last_draw_result.deluxe if last_draw_result else None, 
            'casino': last_draw_result.casino if last_draw_result else None,
            'express': last_draw_result.express if last_draw_result else None,
            'gold_play': last_draw_result.gold_play if last_draw_result else None,
        },
        'name': name
    }
    print(context)

    return render(request, 'draws/play-2Digit-Jodi-online.html', context)

def index(request):
    current_time = datetime.now()

    # Calculate the nearest draw time (a multiple of 15 minutes)
    minutes = (current_time.minute // 15) * 15
    draw_time = current_time.replace(minute=minutes, second=0, microsecond=0)
    if draw_time < current_time:
        draw_time += timedelta(minutes=15)
    last_draw_time = draw_time - timedelta(minutes=15)

     # Fetch the latest draw result based on the date and before the draw time
    last_draw_result = DrawResult.objects.filter(date=last_draw_time.date(), time=last_draw_time.time()).last()
    
    # import pdb; pdb.set_trace()
    time_to_draw = draw_time - current_time

    context = {
        'draw_time': draw_time.strftime('%I:%M %p'),
        'date': current_time.strftime('%m/%d/%Y'),
        'now_time': current_time.strftime('%I:%M:%S %p'),
        'time_to_draw': str(time_to_draw).split('.')[0],  # Remove microseconds
        'last_draw_time': last_draw_time.strftime('%I:%M %p'),
        'last_draw_result': {
            'royal': last_draw_result.royal if last_draw_result else None,
            'deluxe': last_draw_result.deluxe if last_draw_result else None, 
            'casino': last_draw_result.casino if last_draw_result else None,
            'express': last_draw_result.express if last_draw_result else None,
            'gold_play': last_draw_result.gold_play if last_draw_result else None,
        }
    }

    print(context)

    return render(request, 'draws/index.html', context)


@login_required(login_url='/admin/login/')
def generate_draw_results_for_date(request, date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    start_time = datetime.combine(date, datetime.min.time())
    end_time = start_time + timedelta(days=1)
    current_time = start_time

    while current_time < end_time:
        if not DrawResult.objects.filter(date=date, time=current_time.time()).exists():
            DrawResult.objects.create(
                date=date,
                time=current_time.time(),
                royal=random.randint(0, 100),
                deluxe=random.randint(0, 100),
                casino=random.randint(0, 100),
                express=random.randint(0, 100),
                gold_play=random.randint(0, 100)
            )
        current_time += timedelta(minutes=15)
    return JsonResponse({"message": "Draw results generated successfully."}, status=200)
