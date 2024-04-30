from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django_registration.backends.one_step.views import RegistrationView
from .models import *   
import json

def index(request):
    return redirect('/accounts/register/')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            operator = Operator.objects.get(user=user)
            #print('Try luck with id: ',operator.id)
            return redirect('nav', id=operator.id)
        else:
            return render(request, 'sign_in.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'sign_in.html')
'''    
@login_required
def route_select(request, id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        start_address = data['start_address']
        end_address = data['end_address']

        # Get operator
        operator_id = request.user.operator.id
        operator = Operator.objects.get(pk=operator_id)

        # Save points to Delivery model
        delivery = Delivery.objects.create(
            s_lat=start_address['lat'],
            s_long=start_address['long'],
            e_lat=end_address['lat'],
            e_long=end_address['long'],
            operator_id=operator
        )
        
        # Save points to Operator model
        operator.n_lat = start_address['lat']
        operator.n_long = start_address['long']
        operator.save()

        return JsonResponse({'success': True})
    
    operator_id = request.user.operator.id
    operator = Operator.objects.get(pk=operator_id)
    context = {
        'operator': operator
    }
    return render(request, 'route_select.html', context=context)
'''
@login_required
def nav(request, id):
    operator_id = request.user.operator.id
    if operator_id != id:
        return HttpResponseForbidden()

    operator = Operator.objects.get(pk=id)
    delivery = Delivery.objects.filter(operator_id=operator.id).last()
    api_key = settings.API_KEY
    
    context = {
        'delivery': delivery,
        'operator_id': id,
        'API_KEY': api_key
    }
    return render(request, 'nav.html', context=context)


class MyRegistrationView(RegistrationView):
    template_name = 'sign_up.html'
    def register(self, form):
        new_user = super().register(form)
        Operator.objects.create(user=new_user)
        return new_user
    def get_success_url(self, user):
        return '/sign_in/'