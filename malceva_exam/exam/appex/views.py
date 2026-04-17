from pyexpat.errors import messages
from re import search
from smtpd import usage
from urllib.request import Request
from django.db.models import Q
from django.shortcuts import render , redirect ,get_object_or_404
from django.views import generic
from .models import User, Role, Company, PassportSeries, Position
from django.utils import timezone
#Авторизация
def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(login = login_input)
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['user_login'] = user.login
                role_name = user.role.name if user.role else 'Менеджер'
                request.session['user_role'] = role_name
                user.last_login = timezone.now()
                user.save()
                if role_name == "Администратор":
                    return redirect('show_admin')
                else:
                    return redirect('show_manager')
            else:
                messages.error(request,"Ваш пароль не верный")
                return render(request,'login.html')
        except User.DoesNotExist:
            messages.error(request,"Пользователя не существует")
        except Exception as e:(
            messages.error(request,"ошибка при входе в систему" + e))
    return render(request,'login.html')


def logout_view(request):
    request.session.flush()
    return redirect('login_view')

def show_guest(request):
    return render(request, 'show_guest.html')


def show_admin(request):
    users = User.objects.all()

#фильтрация
    filter_position= request.GET.get('filter_position', '')
    if filter_position:
        users = users.filter(position_id=filter_position)

#Поиск по имени сотрудника
    search_user = request.GET.get('search_user', '')
    if search_user:
        users = users.filter(Q(name__icontains=search_user))

    return render(request, 'show_admin.html', context={'users':users})

def show_manager(request):
    users = User.objects.all()
    #фильтрация
    filter_position = request.GET.get('filter_position', '')
    if filter_position:
        users = users.filter(position_id=filter_position)

    # Поиск по имени сотрудника
    search_user = request.GET.get('search_user', '')
    if search_user:
        users = users.filter(Q(name__icontains=search_user))
    return render(request, 'show_manager.html', context={'users':users})


def edit_manager(request):
    users = User.objects.all()
    return render(request, 'edit_manager.html', context={'users':users})

def show_delete(request):
    if request.method == 'POST':
        user =User.objects.get(id=id)
        user.delete()
        return redirect('show_admin')
