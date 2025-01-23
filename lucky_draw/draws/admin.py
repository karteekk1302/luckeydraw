from django.contrib import admin
from .models import DrawResult
import random
from datetime import datetime

# Define the custom action for generating draw results
def generate_draw_results(modeladmin, request, queryset):
    current_time = datetime.now()

    # Calculate the next draw time, which should be a multiple of 15 minutes
    minutes = (current_time.minute // 15) * 15
    next_draw_time = current_time.replace(minute=minutes, second=0, microsecond=0)

    # Create a new DrawResult with random results for each category
    DrawResult.objects.create(
        date=next_draw_time.date(),
        time=next_draw_time.time(),
        royal=random.randint(0, 100),
        deluxe=random.randint(0, 100),
        casino=random.randint(0, 100),
        express=random.randint(0, 100),
        gold_play=random.randint(0, 100)
    )

    modeladmin.message_user(request, "Draw results generated successfully.")

generate_draw_results.short_description = "Generate random draw results"

class DrawResultAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'royal', 'deluxe', 'casino', 'express', 'gold_play', 'name')
    list_filter = ('date', 'time')
    search_fields = ('date', 'time')
    actions = [generate_draw_results]

admin.site.register(DrawResult, DrawResultAdmin)