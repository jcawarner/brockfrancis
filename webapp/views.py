from django.shortcuts import render, redirect, HttpResponse
import pandas as pd
from webapp.models import Drill, Component, Center, CenterQuantity
from collections import Counter


# Create your views here.
def index(request):

	return render(request, 'index.html', {})



def drill_info(request):
    if request.method == 'POST':
        diameter = request.POST.get('diameter')
        grade = request.POST.get('grade')
        coating = request.POST.get('coating')

        drill_inventory = pd.read_csv("static/brazed_drill_build_components.csv")
        drill_min_dc = drill_inventory["MIN DC"][0]

        component_index = 100

        for index, row in drill_inventory.iterrows():
        	if float(diameter) >= float(row['MIN DC']) and float(diameter) <= float(row['MAX DC']):
        		component_index = index

        component = drill_inventory.iloc[int(component_index),:]

        # this is what needs to be saved as the drill name (figure out how to get casting to the drill model name) - pull casting connected to drill to name that drill on the model
        created = f"EJ420.6-{component['CASTING'][5:]} G{grade}{coating} D{diameter}"

        # save center to database
        center = Center.objects.create(code=component['CENTER'])


        new_drill_entry = Drill.objects.create(diameter=diameter, grade=grade, coating=coating)
        new_component_entry = Component.objects.create(thread=component['THREAD'], casting=component['CASTING'], center=component['CENTER'], 
        	peripheral=component['PERIPHERAL'], intermediate=component['INTERMEDIATE'], pad=component['PAD'], drill=new_drill_entry)


        return render(request, 'drill_info.html', {'created':created, 'thread':component['CASTING'], 'center':center})


def save(request):
	
	return redirect('index')


def inventory(request):
    drills = []
    inventory_dict = {}
    for e in Drill.objects.all():

        drills.append(e.diameter)

    count = Counter(drills)
    for item, count in count.items():
        inventory_dict[item] = count


    return render(request, 'inventory.html', {'drills':drills, 'count':inventory_dict})


def center_created(request, center):

    return render(request, 'center_created.html', {'center':center})


def center_saved(request, center):

    if request.method == 'POST':
        variant = request.POST.get('variant')
        quantity = request.POST.get('quantity')

    new_center = Center.objects.create(code=center, variant=variant)
    new_center_quantity = CenterQuantity.objects.create(quantity=quantity, center= new_center)


    return render(request, 'center_saved.html', {'variant':variant, 'quantity':quantity, 'center':center})

