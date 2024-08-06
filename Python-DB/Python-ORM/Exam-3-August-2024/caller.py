import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Mission, Spacecraft # Importing our models from models.py / 1st task.
from django.db.models import Q, Count, Avg, Sum

# Create queries within functions
def get_astronauts(search_string=None):
    if search_string is None:
        return ""
    astronauts = Astronaut.objects.filter(
        models.Q(name__icontains=search_string) | models.Q(phone_number__icontains=search_string)
    ).order_by('name')
    if not astronauts:
        return ""
    result = []
    for astronaut in astronauts:
        status = "Active" if astronaut.is_active else "Inactive"
        result.append(f"Astronaut: {astronaut.name} phone number: {astronaut.phone_number} status: {status}")
    return "\n".join(result)

def get_top_astronaut():
    astronaut = Astronaut.objects.annotate(
        mission_count=models.Count('missions')
    ).order_by('-mission_count', 'phone_number').first()
    if not astronaut:
        return "No data."
    return f"Top Astronaut: {astronaut.name} with {astronaut.mission_count} missions."

def get_top_commander():
    astronaut = Astronaut.objects.annotate(
        commanded_mission_count=models.Count('commanded_missions')
    ).order_by('-commanded_mission_count', 'phone_number').first()
    if not astronaut:
        return "No data."
    return f"Top Commander: {astronaut.name} with {astronaut.commanded_mission_count} commanded missions."

# 5th task.
def get_last_completed_mission():
    mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()
    if not mission:
        return "No data."
    commander_name = mission.commander.name if mission.commander else "TBA"
    astronauts_names = ", ".join(mission.astronauts.order_by('name').values_list('name', flat=True))
    total_spacewalks = mission.astronauts.aggregate(total=models.Sum('spacewalks'))['total'] or 0
    return f"The last completed mission is: {mission.name}. Commander: {commander_name}. Astronauts: {astronauts_names}. Spacecraft: {mission.spacecraft.name}. Total spacewalks: {total_spacewalks}."

def get_most_used_spacecraft():
    spacecraft = Spacecraft.objects.annotate(
        mission_count=models.Count('mission')
    ).order_by('-mission_count', 'name').first()
    if not spacecraft:
        return "No data."
    num_astronauts = Astronaut.objects.filter(missions__spacecraft=spacecraft).distinct().count()
    return f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, used in {spacecraft.mission_count} missions, astronauts on missions: {num_astronauts}."

def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned', weight__gte=200.0
    ).distinct()
    count = spacecrafts.count()
    if count == 0:
        return "No changes in weight."
    for spacecraft in spacecrafts:
        spacecraft.weight -= 200.0
        spacecraft.save()
    avg_weight = Spacecraft.objects.aggregate(avg=models.Avg('weight'))['avg']
    return f"The weight of {count} spacecrafts has been decreased. The new average weight of all spacecrafts is {avg_weight:.1f}kg"