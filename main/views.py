# from django.http import HttpResponse

import plotly
import plotly.graph_objects as go
import plotly.offline as pyo

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Post
from .models import Est
from .models import Estimation
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from crispy_forms.helper import FormHelper
from django import forms

from .forms import NewUserForm
from .forms import EstimationForm



# АВТОРИЗАЦИЯ
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.info(request, "Ваш аккаунт создан. Вы вошли в личный кабинет." )
			return redirect("home")
		messages.info(request, "Регистрация не выполнена. Некорректные данные. Пароль должен содержать не менее 8 символов.")
	form = NewUserForm()

	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Вы вошли как {username}.")
				return redirect("home")
			else:
				messages.info(request,"Неверный логин или пароль.")
		else:
			messages.info(request,"Неверный логин или пароль.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login_.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Вы вышли из учетной записи.")
	return redirect("home")


def reference(request):
    return render(request, "main/reference.html")

def index(request):
    return render(request, "main/index.html")

def create(request):
    error = ''
    if request.method == "POST":
        form = EstimationForm(request.POST)
        if form.is_valid():
            # form.save()
            projectname = form.cleaned_data.get('projectname')
            author = request.user
            estim = Estimation.objects.create(cycle=1, zainteresovannye_storony=0, vosmojnost=0, trebovaniya=0,
                                              programmnaya_sistema=0, rabota=0, komanda=0, tehnologiya_raboty=0,
                                              author=author, projectname=projectname)
            estim.save()
            messages.info(request, f"Сохранено")
            return redirect("standartproject")

    form = EstimationForm()

    data = {
        'form': form,
        "error": error
    }

    return render(request, "main/create.html", data)

def projects(request):
#     # error = ''
#     # if request.method == "POST":
#     #     form = EstimationForm(request.POST)
#     #     if form.is_valid():
#     #         # form.save()
#     #         projectname = form.cleaned_data.get('projectname')
#     #         author = request.user
#     #         estim = Estimation.objects.create(cycle=1, zainteresovannye_storony=0, vosmojnost=0, trebovaniya=0,
#     #                             programmnaya_sistema=0, rabota=0, komanda=0, tehnologiya_raboty=0,
#     #                             author=author, projectname=projectname)
#     #         estim.save()
#     #         messages.info(request, f"Сохранено")
#     #     else:
#     #         error = "Форма неверна"
#     #
#     # form = EstimationForm()
#
#     author = request.user
#     if Estimation.objects.filter(author=author).exists() == True:
#         my_projects = Estimation.objects.filter(author=author).all()
#     else:
#         my_projects = []
#         my_projects = my_projects.append("У вас пока нет проектов.")
#
#     # if request.method == 'POST':
#     #     projectname = request.POST.getlist("{{my_pr.projectname}}")
#
#     data = {
#         # 'form': form,
#         # "error": error,
#         "my_projects": my_projects,
#         # "projectname": projectname
#     }
#
    return render(request, "main/projects.html")

def standartproject(request):
    return render(request, "main/standartproject.html")

def cycle1(request):
    # if request.method == "POST":
    #     form = EstimationForm(request.POST)
    #     if form.is_valid():
    #         # form.save()
    #         projectname = form.cleaned_data.get('projectname')
    # form = EstimationForm()
    #
    # data = {
    #     'form': form
    # }
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    else:
        messages.info(request, f"Перед оценкой создайте проект.")
        return redirect("create")

    return render(request, "main/cycle1.html", {"my_projects": my_projects})

def cycle2(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle2.html", {"my_projects": my_projects})

def cycle3(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle3.html", {"my_projects": my_projects})

def cycle4(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle4.html", {"my_projects": my_projects})

def cycle5(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle5.html", {"my_projects": my_projects})

def cycle6(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle6.html", {"my_projects": my_projects})

def cycle7(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle7.html", {"my_projects": my_projects})

def cycle8(request):
    author = request.user
    if Estimation.objects.filter(author=author).exists() == True:
        my_projects = Estimation.objects.filter(author=author).all()
    return render(request, "main/cycle8.html", {"my_projects": my_projects})

# ЛЕПЕСТКОВАЯ ДИАГРАММА
def graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr):
    # categories = ['Заинтересованные стороны', 'Возможность', 'Требования',
    #               'Программная система', 'Работа', 'Команда', 'Технология работы']
    categories = ['Заинтересованные стороны', 'Технология работы', 'Команда', 'Работа',
                  'Программная система', 'Требования', 'Возможность']
    categories = [*categories, categories[0]]
    #
    # normal = [nz, nv, nt, np, nr, nk, ntr]
    # state = [z, v, t, p, r, k, tr]
    normal = [nz, ntr, nk, nr, np, nt, nv]
    state = [z, tr, k, r, p, t, v]
    normal = [*normal, normal[0]]
    state = [*state, state[0]]

    fig = go.Figure(
            data=[
                go.Scatterpolar(r=normal, theta=categories, name='Нормальное состояние', line=dict(color='red')),
                go.Scatterpolar(r=state, theta=categories, name='Текущее состояние', line=dict(color='blue')),
            ],

            layout=go.Layout(
                showlegend=True,
                polar=dict(
                    # angularaxis=dict(
                    # tickvals=['Заинтересованные стороны', 'Возможность', 'Требования',
                    #   'Программная система', 'Работа', 'Команда', 'Технология работы']),
                    radialaxis=dict(
                        range=[0, 6])
                )

                # legend = go.layout.Legend(x=1.1, y=1.1)
            )
    )
    if np is None and nr is None and ntr is None:
        fig.add_trace(go.Scatterpolar(
                r=[nt, nk, nz],
                theta=['Требования', 'Команда', 'Заинтересованные стороны'],
                line=dict(color='red'),
                showlegend = False
            ))

        fig.add_trace(go.Scatterpolar(
                r=[t, k, z],
                theta=['Требования', 'Команда', 'Заинтересованные стороны'],
                line=dict(color='blue'),
                showlegend = False
            ))
    elif np is None:
        fig.add_trace(go.Scatterpolar(
                r=[nt, nr],
                theta=['Требования', 'Работа'],
                line=dict(color='red'),
                showlegend=False
            ))

        fig.add_trace(go.Scatterpolar(
                r=[t, r],
                theta=['Требования', 'Работа'],
                line=dict(color='blue'),
                showlegend=False
            ))

    return(fig)

# РАБОТА С ВЕКТОРАМИ
def repl(l, s):
    for i in range(len(l)):
        if l[i] == 'on':
            l[i] = '1'
    for i in range(len(l)):
        s[i] = l[i]
    return(s)

# Получение данных из базы
def get_val(cycle_, z, v, t, p, r, k, tr, author, projectname):
    if Estimation.objects.filter(cycle = cycle_, author = author, projectname = projectname).exists() == True:

        ev = Estimation.objects.filter(cycle = cycle_, author = author, projectname = projectname).update(cycle=cycle_, zainteresovannye_storony=z, vosmojnost=v, trebovaniya=t,
                                programmnaya_sistema=p, rabota=r, komanda=k, tehnologiya_raboty=tr,
                                author = author, projectname = projectname)
        # ev.save()
    else:
        ev = Estimation.objects.create(cycle = cycle_, zainteresovannye_storony=z, vosmojnost=v, trebovaniya=t,
                                 programmnaya_sistema=p, rabota=r, komanda=k, tehnologiya_raboty=tr,
                                 author = author, projectname = projectname)
        ev.save()

    evaluation = Estimation.objects.filter(cycle = cycle_, projectname = projectname).in_bulk([author.id])
    for id in evaluation:
        z = evaluation[id].zainteresovannye_storony
        v = evaluation[id].vosmojnost
        t = evaluation[id].trebovaniya
        p = evaluation[id].programmnaya_sistema
        r = evaluation[id].rabota
        k = evaluation[id].komanda
        tr = evaluation[id].tehnologiya_raboty
    return(z, v, t, p, r, k, tr)


def get_value_for_graph(cycle_, atable, author, projectname):
    if Estimation.objects.filter(cycle=cycle_ - 1, author=author,projectname = projectname).exists() == True:
        a = Estimation.objects.values_list(atable).get(cycle=cycle_ - 1, author=author, projectname = projectname)[0]
    else:
        a = 0
    return (a)


# РЕЗУЛЬТАТЫ ПО ПЕРВОМУ ЦИКЛУ
@login_required
def results_1(request):

    cycle_ = 1
    nz, nv, nt, np, nr, nk, ntr = 2, 2, 1, 0, 0, 2, 0
    p, r, tr = 0, 0, 0
    # Заинтересованные стороны (признаны, представлены)
    prizn = [0, 0, 0, 0]
    predstavl = [0, 0, 0, 0]
    norm_zp = ["1", "1", "1", "1"]
    # Возможность (определена, требуется решение)
    opredelena = [0, 0, 0]
    norm_opredelena = ["1", "1", "1"]
    trebueca_reshenie = [0, 0, 0, 0, 0]
    norm_trebueca_reshenie = ["1", "1", "1", "1", "1"]
    # Требования (задуманы)
    zadumany = [0, 0, 0, 0]
    norm_zadumany = ["1", "1", "1", "1"]
    # Команда (заявлена, сформирована)
    zayavlena = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sformirivana = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    norm_zayavlena = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
    norm_sformirivana = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]

    # Сбор данных с чек-листов
    if request.method == 'POST':
        list_ = request.POST.getlist('Признаны')
        list2_ = request.POST.getlist('Представлены')
        list3_ = request.POST.getlist('Определена')
        list4_ = request.POST.getlist('Требуется решение')
        list5_ = request.POST.getlist('Задуманы')
        list6_ = request.POST.getlist('Заявлена')
        list7_ = request.POST.getlist('Сформирована')
        projectname = request.POST.get('Проект')


    prizn = repl(list_, prizn)
    predstavl = repl(list2_, predstavl)
    opredelena = repl(list3_, opredelena)
    trebueca_reshenie = repl(list4_, trebueca_reshenie)
    zadumany = repl(list5_, zadumany)
    zayavlena = repl(list6_, zayavlena)
    sformirivana = repl(list7_, sformirivana)

    # Результат, причины, рекомендации
    res = []
    reason = []
    recommend = []
    if prizn == norm_zp and predstavl == norm_zp and opredelena == norm_opredelena and trebueca_reshenie == norm_trebueca_reshenie and zadumany == norm_zadumany and zayavlena == norm_zayavlena and sformirivana == norm_sformirivana:
        res.append("Все сущности достигли нормального состояния.")
        z, v, k = 2, 2, 2
        t = 1

    if prizn == norm_zp and predstavl == norm_zp:
        z = 2
    elif prizn != norm_zp and predstavl != norm_zp:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной недостижения нормального состояния Заинтересованных сторон является слабая связь участников проекта с заинтересованными сторонами, возможно, не было проведено ни одной встречи, или команда не получила четких требований от заинтересованных сторон.")
        recommend.append("Организуйте встречу участников команды проекта с заинтересованными сторонами и задайте все интересующие вопросы, попросите объяснить все требования по проекту.")
        z = 0
    else:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной недостижения нормального состояния Заинтересованных сторон является слабая связь участников проекта с заинтересованными сторонами, возможно, не было проведено ни одной встречи, или команда не получила четких требований от заинтересованных сторон.")
        recommend.append("Организуйте встречу участников команды проекта с заинтересованными сторонами и задайте все интересующие вопросы, попросите объяснить все требования по проекту.")
        z = 1

    if opredelena == norm_opredelena and trebueca_reshenie == norm_trebueca_reshenie:
        v = 2
    elif opredelena != norm_opredelena and trebueca_reshenie != norm_trebueca_reshenie:
        v = 0
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: заинтересованные стороны неопределенны, участникам проекта не ясна ценность проекта и его перспектива, не найдены проблемные места проекта, не предложено решение поставленных задач. ")  # Причина
        recommend.append("Обсудите с Заинтересованными сторонами и командой и пригласите ценность, проблемы и задачи проекта. Удостоверьтесь, что каждый член команды понимает их. ")  # Рекомендация
    else:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: команда не пришла к согласию с Заинтересованными сторонами, необходимость в программной системе не обозначена, предложений по решению проблем на данном этапе нет. ")  # Причина
        recommend.append("Обсудите с Заинтересованными сторонами и командой и пригласите ценность, проблемы и задачи проекта. Удостоверьтесь, что каждый член команды понимает их.")  # Рекомендация
        v = 1

    if zadumany != norm_zadumany:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможные причины: команда участников проекта не пришла в согласие с заинтересованными сторонами, возможность неопределенна, участники не понимают ценности проекта. ")
        recommend.append("Проанализируйте поставленные задачи и цели проекта, обсудите с командой возможные пути решения поставленных задач, при возникновении трудностей, организуйте встречу с Заинтересованными сторонами для уточнения инофрмации или своих предложений по реализации проекта. ")
        t = 0
    else:
        t = 1

    if zayavlena == norm_zayavlena and sformirivana == norm_sformirivana:
        k = 2
    elif zayavlena != norm_zayavlena and sformirivana != norm_sformirivana:
        k = 0
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: члены команды не взаимодействуют между собой или команда еще не сформирована окончательно, члены команды не понимают требований, проблем и ценность проекта. ")
        recommend.append("Сформируйте окончательную команду, организуйте встречу, на которой распределите роли и обязанности между участниками проекта.  ")
    else:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: миссия команды неопределенна, роли в команде неизвестны, не определен тимлидер команды, задачи по членам команды не распределены, требования неясны, члены команды не понимают, как выполнять задачу. ")
        recommend.append("Уточните у Заинтересованных сторон требования и конечные результаты, вместе с командой выберите тимлидера, обсудите роль и задачи каждого участника проекта, выявите ценность и перспективу развития проекта. ")
        k = 1

    # Работа с базой
    author = request.user
    get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)
    # if Est.objects.filter(cycle = 1, author=request.user).exists() == True:
    #
    #     ev = Est.objects.update(cycle=1, zainteresovannye_storony=z, vosmojnost=v, trebovaniya=t,
    #                             programmnaya_sistema=p, rabota=r, komanda=k, tehnologiya_raboty=tr,
    #                             author=request.user)
    #     # ev.save()
    # else:
    #     ev = Est.objects.create(cycle = 1, zainteresovannye_storony=z, vosmojnost=v, trebovaniya=t,
    #                              programmnaya_sistema=p, rabota=r, komanda=k, tehnologiya_raboty=tr,
    #                              author=request.user)
    #     ev.save()
    #
    # evaluation = Est.objects.filter(cycle = 1).in_bulk([request.user.id])
    # for id in evaluation:
    #     z = evaluation[id].zainteresovannye_storony
    #     v = evaluation[id].vosmojnost
    #     t = evaluation[id].trebovaniya
    #     p = evaluation[id].programmnaya_sistema
    #     r = evaluation[id].rabota
    #     k = evaluation[id].komanda
    #     tr = evaluation[id].tehnologiya_raboty

    # График и результаты
    graph_div = plotly.offline.plot(graph(nz, nv, nt, None, None, nk, None, z, v, t, None, None, k, None), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})



# РЕЗУЛЬТАТЫ ПО ВТОРОМУ ЦИКЛУ
@login_required
def results_2(request):
    cycle_ = 2
    nz, nv, nt, np, nr, nk, ntr = 4, 3, 2, 0, 1, 3, 1
    p = np
    author = request.user
    # Заинтересованные стороны (вовлечены, в согласии)
    vovlecheny = [0, 0, 0]
    vsoglasii = [0, 0, 0, 0, 0]
    norm_vovlecheny = ["1", "1", "1"]
    norm_vsoglasii = ["1", "1", "1", "1", "1"]
    # Возможность (ценность установлена)
    cennost_ustanovlena = [0, 0, 0, 0, 0]
    norm_cennost_ustanovlena = ["1", "1", "1", "1", "1"]
    # Требования (ограничены)
    ogranicheny = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    norm_ogranicheny = ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
    # Работа (инициирована)
    iniciirovana = [0, 0, 0, 0, 0, 0]
    norm_iniciirovana = ["1", "1", "1", "1", "1", "1"]
    # Команда (в сотрудничестве)
    sotrudnichaet = [0, 0, 0, 0]
    norm_sotrudnichaet = ["1", "1", "1", "1"]
    # Технология работы (принципы установлены)
    principyustanovleny = [0, 0, 0, 0, 0, 0]
    norm_principyustanovleny = ["1", "1", "1", "1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('Вовлечены')
        list2_ = request.POST.getlist('В согласии')
        list3_ = request.POST.getlist('Ценность установлена')
        list4_ = request.POST.getlist('Ограничены')
        list5_ = request.POST.getlist('Инициирована')
        list6_ = request.POST.getlist('Сотрудничает')
        list7_ = request.POST.getlist('Принципы установлены')
        projectname = request.POST.get('Проект')



    vovlecheny = repl(list_, vovlecheny)
    vsoglasii = repl(list2_, vsoglasii)
    cennost_ustanovlena = repl(list3_, cennost_ustanovlena)
    ogranicheny = repl(list4_, ogranicheny)
    iniciirovana = repl(list5_, iniciirovana)
    sotrudnichaet = repl(list6_, sotrudnichaet)
    principyustanovleny = repl(list7_, principyustanovleny)



    res = []
    reason = []
    recommend = []
    if vovlecheny == norm_vovlecheny and vsoglasii == norm_vsoglasii and\
            cennost_ustanovlena == norm_cennost_ustanovlena and ogranicheny == norm_ogranicheny\
            and iniciirovana == norm_iniciirovana and sotrudnichaet == norm_sotrudnichaet\
            and principyustanovleny == norm_principyustanovleny:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if vovlecheny == norm_vovlecheny and vsoglasii == norm_vsoglasii:
        z = nz
    elif vovlecheny != norm_vovlecheny and vsoglasii != norm_vsoglasii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причинами неуспеха могут быть: Заинтересованные стороны не участвуют в ходе проекта, участники команды не получают обратную связь, команда не получает информацию об изменении в ходе проекта. ")  # Причина
        recommend.append("Организуйте встречу с Заинтересованными сторонами и определите возможность и частоту совместных встреч. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)

    else:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной такого результата является слабая связь участников проекта с заинтересованными сторонами, заинтересованные стороны не помогают команде, ожидания от работы не удовлетворяет заинтересованные стороны. ")
        recommend.append("Организуйте встречу с Заинтересованными сторонами, обсудите предстоящую работу, договоритесь о частоте проводимых встреч, для демонстрации результатов проектной деятельности. ")
        z = nz-1

    if cennost_ustanovlena != norm_cennost_ustanovlena:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: участникам проекта не ясна ценность проекта и его перспектива, желаемый результат команде не понятен, критерии успеха не определены. ")  # Причина
        recommend.append("Обсудите с Заинтересованными сторонами последующие шаги реализации проекта, передайти требования каждому члену команды. ")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        v = nv


    if ogranicheny != norm_ogranicheny:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Причинами неуспеха могут быть: команда участников проекта не пришла в согласие с заинтересованными сторонами, приоритеты неясны, ограничение не определены. ")  # Причина
        recommend.append("Уточните у каждого члена команды его понимание задач и ценности проекта. Постарайтесь прийти к общему мнению и политике ведения проекта. Если возникнут трудности во время обсуждения, пригласите на встречу Заинтересованные стороны для уточнения из позиции по этому поводу. ")  # Рекомендация
        # t = 0 # Должна быть ссылка на результат из первого цикла
        author = request.user
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        t = nt

    if iniciirovana != norm_iniciirovana:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». Причинами неуспеха могут служить: результат от работы неочевиден, задачи между командой не распределены, заинтересованные стороны не принимают участие в работе и обсуждениях.  ")  # Причина
        recommend.append("Распределите задачи между членами команды в соответсвии с навыками и знаниями каждого члена команды. Составьте план работ, обозначив временные рамки и придерживайтесь его. ")  # Рекомендация
        r = 0
    else:
        r = nr

    if sotrudnichaet != norm_sotrudnichaet:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут служить: команда не работает слаженно, члены команды не взаимодействуют между собой, не все члены команды понимают задачи, между членами команды присутствует напряжение. ")  # Причина
        recommend.append("Узнайте у команды моменты, которые тревожат каждого из членов команды, обсудите задачи каждого, обсудите дальнейший план действий и придерживайтесь его. Можно устроить пару неформальных встреч, для налаживания контакта между участниками проекта. ")  # Рекомендация
        author = request.user
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        k = nk

    if principyustanovleny != norm_principyustanovleny:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Причинами неуспеха могут служить: принципы и ограничения команды не представлены, принципы и ограничения не согласованы с заинтересованными сторонами, отсутствуют рекомендации по дальнейшей работе. ")  # Причина
        recommend.append("Перед началом работы обсудите с командой план дальшейших действий, как они понимают свои задачи, узнайте, есть ли у кого-либо трудности. Обсудите способы и методы решения поставленных задач. ")  # Рекомендация
        tr = 0
    else:
        tr = ntr

    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, None, nr, nk, ntr, z, v, t, None, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})

# РЕЗУЛЬТАТЫ ПО ТРЕТЬЕМУ ЦИКЛУ
@login_required
def results_3(request):
    cycle_ = 3
    nz, nv, nt, np, nr, nk, ntr = 4, 4, 4, 1, 2, 3, 2
    k = 0  # Должна быть ссылка на результат из предыдущего цикла
    # Заинтересованные стороны (в согласии)
    vsoglasii = [0, 0, 0, 0, 0]
    norm_vsoglasii = ["1", "1", "1", "1", "1"]
    # Возможность (ценность установлена, жизнеспособна)
    cennost_ustanovlena = [0, 0, 0, 0, 0]
    jiznesposobna = [0, 0, 0, 0, 0]
    norm_cennost_ustanovlena = ["1", "1", "1", "1", "1"]
    norm_jiznesposobna = ["1", "1", "1", "1", "1"]
    # Требования (непротиворечивы, приемлемы)
    neprotivorechivy = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    priemlemy = [0, 0, 0, 0, 0]
    norm_neprotivorechivy = ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
    norm_priemlemy = ["1", "1", "1", "1", "1"]
    # Программная система (архитектура выбрана)
    arhitectura_vybrana = [0, 0, 0, 0, 0, 0, 0]
    norm_arhitectura_vybrana = ["1", "1", "1", "1", "1", "1", "1"]
    # Работа (подготовлена)
    podgotovlena = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    norm_podgotovlena = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
    # Технология работы (основа заложена)
    osnova_zalojena = [0, 0, 0, 0, 0, 0]
    norm_osnova_zalojena = ["1", "1", "1", "1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('В согласии')
        list2_ = request.POST.getlist('Ценность установлена')
        list3_ = request.POST.getlist('Жизнеспособна')
        list4_ = request.POST.getlist('Непротиворечивы')
        list5_ = request.POST.getlist('Приемлемы')
        list6_ = request.POST.getlist('Архитектура выбрана')
        list7_ = request.POST.getlist('Подготовлена')
        list8_ = request.POST.getlist('Основа заложена')
        projectname = request.POST.get('Проект')

    # projectname = list(projectname)

    vsoglasii = repl(list_, vsoglasii)
    cennost_ustanovlena = repl(list2_, cennost_ustanovlena)
    jiznesposobna = repl(list3_, jiznesposobna)
    neprotivorechivy = repl(list4_, neprotivorechivy)
    priemlemy = repl(list5_, priemlemy)
    arhitectura_vybrana = repl(list6_, arhitectura_vybrana)
    podgotovlena = repl(list7_, podgotovlena)
    osnova_zalojena = repl(list8_, osnova_zalojena)

    res = []
    reason = []
    recommend = []
    if vsoglasii == norm_vsoglasii and cennost_ustanovlena == norm_cennost_ustanovlena and\
            jiznesposobna == norm_jiznesposobna and priemlemy == norm_priemlemy\
            and arhitectura_vybrana == norm_arhitectura_vybrana and neprotivorechivy == norm_neprotivorechivy\
            and podgotovlena == norm_podgotovlena and osnova_zalojena == norm_osnova_zalojena:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if vsoglasii != norm_vsoglasii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной такого результата может быть является слабая связь участников проекта с заинтересованными сторонами, заинтересованные стороны не помогают команде, ожидания от работы не удовлетворяет заинтересованные стороны. ")  # Причина
        recommend.append("Организуйте встречу с Заинтересованными сторонами для обсуждения последующих шагов в реализации проекта. ")  # Рекомендация
        author = request.user
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        z = nz

    if cennost_ustanovlena == norm_cennost_ustanovlena and jiznesposobna == norm_jiznesposobna:
        v = nv
    elif cennost_ustanovlena != norm_cennost_ustanovlena and jiznesposobna != norm_jiznesposobna:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Причинами неуспеха могут быть: участникам проекта не ясна ценность проекта и его перспектива, желаемый результат команде не понятен, критерии успеха не определены. ")  # Причина
        recommend.append("Обсудите с командой и с Заинтересованными сторонами последующие шаги в реализации проекта. ")  # Рекомендация
        author = request.user
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». При выполнении задач могли возникнуть трудности. Возможно, некоторые члены команды не до конца понимают ценность проекта и конечный результат, некоторые члены команды могут по разному оценивать возможность решения проблем проекта. ")  # Причина
        recommend.append("Обсудите с командой понимание проекта и решение поставленных задач. Если мнение между командой расходиться, прийдите к общему мнение или попросите помощи у Заинтересованных сторон. ")  # Рекомендация
        v = nv - 1

    if neprotivorechivy == norm_neprotivorechivy and priemlemy == norm_priemlemy:
        t = nt
    elif neprotivorechivy != norm_neprotivorechivy and priemlemy != norm_priemlemy:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны».  При выполнении членами команды своиз задач могли возникнуть трудности с пониманием того, какие проблемы будут решены с помощью конечного решения. К возможным причинам неуспеха данной альфы может оносится слабая связь между участниками команды и Заинтересованными сторонами, из-за отсутсвия коммуникации команда может не узнать об изменениях, или не сможет предложить свое решение. ")  # Причина
        recommend.append("Постарайтесь четко изложить проблемные места при выполнении задач, сообщите о проблемах Заинтересованным сторонам и вместе найдите наиболее правильные пути решения проблем. ")  # Рекомендация
        author = request.user
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможными причинами неуспеха может быть быстрое изменение требований со стороны Заинтересованных сторон. Члены команды не успевают перестраиваться между требованиями и пониманием задач, которые нужно решить для решения проблем проекта. ")  # Причина
        recommend.append("Уточните у Заинтересованных сторон актуальность целей и задач проекта. Проверьте, чтобы понимание проекта и задачи всех участников команды совпадали с текущим представлением Заинтересованных сторон о проекте. ")  # Рекомендация
        t = nt - 1

    if arhitectura_vybrana != norm_arhitectura_vybrana:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append(". На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха могут служить: критерии при выборе архитектуры не согласованы, аппаратные платформы не определены, не выбраны языки программирования, в команде разногласия. ")  # Причина
        recommend.append("Проанализируйте результату предстоящей работы, решите, каким путем и с помощью каких инструментов будут достигнуты определенные результаты, найдите компромисс для всех участников проекта, если возникают трудности, обратитесь к Заинтересованным сторонам. ")  # Рекомендация
        author = request.user
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    else:
        p = np

    if podgotovlena != norm_podgotovlena:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». Причинами неуспеха могут служить: обязательства неясны, риски воздействия неочевидны, плана по дальнейшей работе нет, в команде имеются разногласия. ")  # Причина
        recommend.append("Поговорите с командой о плане дальнейших действий, выясните, почему произошли недопонимания, распределите обязанности опираясь на знания и навыки каждого члена команды.")  # Рекомендация
        author = request.user
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        r = nr

    if osnova_zalojena != norm_osnova_zalojena:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Причинами неуспеха могут служить: ключевые методы и инструменты не выбраны, недостаточно квалификации у членов команды. ")  # Причина
        recommend.append("Правильно распределите задачи между членами команды, чтобы у каждого участника задачи совпадали с его навыками и знаниями. Можно заложить дополнительное время на изучение проблемные мест, получения новой информации. ")  # Рекомендация
        author = request.user
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    else:
        tr = ntr
    k = get_value_for_graph(cycle_, "komanda", author, projectname)
    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})

# РЕЗУЛЬТАТЫ ПО ЧЕТВЕРТОМУ ЦИКЛУ
@login_required
def results_4(request):
    cycle_ = 4
    author = request.user
    nz, nv, nt, np, nr, nk, ntr = 4, 4, 4, 1, 3, 4, 4
    # Заинтересованные стороны (в согласии)
    vsoglasii = [0, 0, 0, 0, 0]
    norm_vsoglasii = ["1", "1", "1", "1", "1"]
    # Возможность (жизнеспособна)
    jiznesposobna = [0, 0, 0, 0, 0]
    norm_jiznesposobna = ["1", "1", "1", "1", "1"]
    # Требования (приемлемы)
    priemlemy = [0, 0, 0, 0, 0]
    norm_priemlemy = ["1", "1", "1", "1", "1"]
    # Программная система (архитектура выбрана)
    arhitectura_vybrana = [0, 0, 0, 0, 0, 0, 0]
    norm_arhitectura_vybrana = ["1", "1", "1", "1", "1", "1", "1"]
    # Работа (начата)
    nachata = [0, 0, 0, 0]
    norm_nachata = ["1", "1", "1", "1"]
    # Команда (в разработке)
    vrazrabotke = [0, 0, 0, 0, 0]
    norm_vrazrabotke = ["1", "1", "1", "1", "1"]
    # Технология работы (в частичном использовании, в использовании)
    vchastichnom_ispolzovanii = [0, 0, 0, 0, 0, 0]
    norm_vchastichnom_ispolzovanii = ["1", "1", "1", "1", "1", "1"]
    vispolzovanii = [0, 0, 0]
    norm_vispolzovanii = ["1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('В согласии')
        list2_ = request.POST.getlist('Жизнеспособна')
        list3_ = request.POST.getlist('Приемлемы')
        list4_ = request.POST.getlist('Архитектура выбрана')
        list5_ = request.POST.getlist('Начата')
        list6_ = request.POST.getlist('В разработке')
        list7_ = request.POST.getlist('В частичном использовании')
        list8_ = request.POST.getlist('В использовании')
        projectname = request.POST.get('Проект')



    vsoglasii = repl(list_, vsoglasii)
    jiznesposobna = repl(list2_, jiznesposobna)
    priemlemy = repl(list3_, priemlemy)
    arhitectura_vybrana = repl(list4_, arhitectura_vybrana)
    nachata = repl(list5_, nachata)
    vrazrabotke = repl(list6_, vrazrabotke)
    vchastichnom_ispolzovanii = repl(list7_, vchastichnom_ispolzovanii)
    vispolzovanii = repl(list8_, vispolzovanii)


    res = []
    reason = []
    recommend = []
    if vsoglasii == norm_vsoglasii and\
            jiznesposobna == norm_jiznesposobna and priemlemy == norm_priemlemy\
            and arhitectura_vybrana == norm_arhitectura_vybrana and nachata == norm_nachata\
            and vrazrabotke == norm_vrazrabotke and vchastichnom_ispolzovanii == norm_vchastichnom_ispolzovanii and \
            vispolzovanii == norm_vispolzovanii:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if vsoglasii != norm_vsoglasii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной такого результата может быть является слабая связь участников проекта с заинтересованными сторонами, заинтересованные стороны не помогают команде, ожидания от работы не удовлетворяет заинтересованные стороны. ")  # Причина
        recommend.append("Организуйте встречу с Заинтересованными сторонами для обсуждения последующих шагов в реализации проекта. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        z = nz

    if jiznesposobna != norm_jiznesposobna:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». При выполнении задач могли возникнуть трудности. Возможно, некоторые члены команды не до конца понимают ценность проекта и конечный результат, некоторые члены команды могут по разному оценивать возможность решения проблем проекта. ")  # Причина
        recommend.append("Обсудите с командой понимание проекта и решение поставленных задач. Если мнение между командой расходиться, прийдите к общему мнение или попросите помощи у Заинтересованных сторон. ")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        v = nv


    if priemlemy != norm_priemlemy:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможными причинами неуспеха может быть быстрое изменение требований со стороны Заинтересованных сторон. Члены команды не успевают перестраиваться между требованиями и пониманием задач, которые нужно решить для решения проблем проекта. ")  # Причина
        recommend.append("Уточните у Заинтересованных сторон актуальность целей и задач проекта. Проверьте, чтобы понимание проекта и задачи всех участников команды совпадали с текущим представлением Заинтересованных сторон о проекте. ")  # Рекомендация
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        t = nt

    if arhitectura_vybrana != norm_arhitectura_vybrana:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха могут служить: критерии при выборе архитектуры не согласованы, аппаратные платформы не определены, не выбраны языки программирования, в команде разногласия. ")  # Причина
        recommend.append("Предоставьте команде немного больше времени для обсуждения предстоящей работы, решите, каким путем и с помощью каких инструментов будут достигнуты определенные результаты, найдите компромисс для всех участников проекта. ")  # Рекомендация
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    else:
        p = np

    if nachata != norm_nachata:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». Причинами неуспеха могут служить: работа еще не началась, работы никто не контролирует, неравноценно распределены задачи между командой, нет прогресса. ")  # Причина
        recommend.append("Поинтересуйтесь у членов команды, как они справляются с поставленными задачами. Если есть трудности, перераспределите обязанности, составьте график работы, установите сроки, собирайте раз в неделю для отслеживания хода проекта. ")  # Рекомендация
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        r = nr

    if vrazrabotke != norm_vrazrabotke:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Возможно, некоторые члены команды не приступили к выполнению своих задач или где-то запутались, перестали понимать что и для чего они это делают. Возможно отставание по срокам и Заинтересованные стороны не довольны достигаемым результатом. ")  # Причина
        recommend.append("Пристановите работу и проверьте, в каком состоянии задачи каждого из членов команды. Помогите или перераспределите задачи у тех, кто не может решить поставленные задачи. Уточните у Заинетресованных сторон, какой результат они ожадают на следующем цикле. ")  # Рекомендация
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        k = nk

    if vchastichnom_ispolzovanii == norm_vchastichnom_ispolzovanii and vispolzovanii == norm_vispolzovanii:
        tr = ntr
    elif vchastichnom_ispolzovanii != norm_vchastichnom_ispolzovanii and vispolzovanii != norm_vispolzovanii:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Команда не использует выбранные методы и инструменты реализации проекта, возможно, выбрали неподходящие практики и инструменты для использования. ")  # Причина
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды новые инструменты и предложите их на встрече.")  # Рекомендация
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    else:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Работа с использованием выбранных инструментов началась, но возникли трудности.Возможно, выбранные методы не подходят для реализации поставленных задач, предложенные Заказчиками инструменты команде незнакомы или неудобны.  ")  # Причина
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды новые инструменты и предложите их на встрече. ")  # Рекомендация
        tr = ntr - 1

    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})


# РЕЗУЛЬТАТЫ ПО ПЯТОМУ ЦИКЛУ
@login_required
def results_5(request):
    cycle_ = 5
    author = request.user
    nz, nv, nt, np, nr, nk, ntr = 4, 4, 4, 2, 4, 4, 5
    # Заинтересованные стороны (в согласии)
    vsoglasii = [0, 0, 0, 0, 0]
    norm_vsoglasii = ["1", "1", "1", "1", "1"]
    # Возможность (жизнеспособна)
    jiznesposobna = [0, 0, 0, 0, 0]
    norm_jiznesposobna = ["1", "1", "1", "1", "1"]
    # Требования (приемлемы)
    priemlemy = [0, 0, 0, 0, 0]
    norm_priemlemy = ["1", "1", "1", "1", "1"]
    # Программная система (демонстрируемая)
    demonstriruemaya = [0, 0, 0, 0, 0, 0]
    norm_demonstriruemaya = ["1", "1", "1", "1", "1", "1"]
    # Работа (под контролем)
    podkontrolem = [0, 0, 0, 0, 0, 0, 0]
    norm_podkontrolem = ["1", "1", "1", "1", "1", "1", "1"]
    # Команда (в разработке)
    vrazrabotke = [0, 0, 0, 0, 0]
    norm_vrazrabotke = ["1", "1", "1", "1", "1"]
    # Технология работы (работает хорошо, в использовании)
    rabotaet_horosho = [0, 0, 0, 0]
    norm_rabotaet_horosho = ["1", "1", "1", "1"]
    vispolzovanii = [0, 0, 0]
    norm_vispolzovanii = ["1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('В согласии')
        list2_ = request.POST.getlist('Жизнеспособна')
        list3_ = request.POST.getlist('Приемлемы')
        list4_ = request.POST.getlist('Демонстрируемая')
        list5_ = request.POST.getlist('Под контролем')
        list6_ = request.POST.getlist('В разработке')
        list7_ = request.POST.getlist('В использовании')
        list8_ = request.POST.getlist('Работает хорошо')
        projectname = request.POST.get('Проект')


    vsoglasii = repl(list_, vsoglasii)
    jiznesposobna = repl(list2_, jiznesposobna)
    priemlemy = repl(list3_, priemlemy)
    demonstriruemaya = repl(list4_, demonstriruemaya)
    podkontrolem = repl(list5_, podkontrolem)
    vrazrabotke = repl(list6_, vrazrabotke)
    vispolzovanii = repl(list7_, vispolzovanii)
    rabotaet_horosho = repl(list8_, rabotaet_horosho)


    res = []
    reason = []
    recommend = []
    if vsoglasii == norm_vsoglasii and\
            jiznesposobna == norm_jiznesposobna and priemlemy == norm_priemlemy\
            and demonstriruemaya == norm_demonstriruemaya and podkontrolem == norm_podkontrolem\
            and vrazrabotke == norm_vrazrabotke and rabotaet_horosho == rabotaet_horosho and \
            vispolzovanii == norm_vispolzovanii:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if vsoglasii != norm_vsoglasii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной такого результата может быть является слабая связь участников проекта с заинтересованными сторонами, заинтересованные стороны не помогают команде, ожидания от работы не удовлетворяет заинтересованные стороны. ")  # Причина
        recommend.append("Организуйте встречу с Заинтересованными сторонами для обсуждения последующих шагов в реализации проекта. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        z = nz

    if jiznesposobna != norm_jiznesposobna:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». При выполнении задач могли возникнуть трудности. Возможно, некоторые члены команды не до конца понимают ценность проекта и конечный результат, некоторые члены команды могут по разному оценивать возможность решения проблем проекта. ")  # Причина
        recommend.append("Обсудите с командой понимание проекта и решение поставленных задач. Если мнение между командой расходиться, прийдите к общему мнение или попросите помощи у Заинтересованных сторон. ")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        v = nv


    if priemlemy != norm_priemlemy:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможными причинами неуспеха может быть быстрое изменение требований со стороны Заинтересованных сторон. Члены команды не успевают перестраиваться между требованиями и пониманием задач, которые нужно решить для решения проблем проекта. ")  # Причина
        recommend.append("Уточните у Заинтересованных сторон актуальность целей и задач проекта. Проверьте, чтобы понимание проекта и задачи всех участников команды совпадали с текущим представлением Заинтересованных сторон о проекте. ")  # Рекомендация
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        t = nt

    if demonstriruemaya != norm_demonstriruemaya:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха могут служить: ключевые архитектурные характеристики не продемонстрированы, конфигурации и интерфейсы не были продемонстрированы. ")  # Причина
        recommend.append("Предоставьте команде немного больше времени для того, чтобы найти ошибки и исправить их. Если есть трудности, которые команда не может решить сама, стоит обратить к заинтересованным сторонам для помощи или совета. Изучите более подробно материал, с которым команде предстоит работать. ")  # Рекомендация
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    else:
        p = np

    if podkontrolem != norm_podkontrolem:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы».Причинами неуспеха могут служить: задачи не выполняются, отставание по срокам, простои в проекте, команда не справляется с задачами. ")  # Причина
        recommend.append("Перераспределите задачи между членами команды, найдите кого-то нового в команду с большей квалификацией для помощи, приостановите работу, разберитесь с незакрытыми задачами, перераспределите ресурсы и сроки выполнения и продолжите работу, исключая возникшие риски. ")  # Рекомендация
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        r = nr

    if vrazrabotke != norm_vrazrabotke:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Возможно, некоторые члены команды не приступили к выполнению своих задач или где-то запутались, перестали понимать что и для чего они это делают. Возможно отставание по срокам и Заинтересованные стороны не довольны достигаемым результатом. ")  # Причина
        recommend.append("Пристановите работу и проверьте, в каком состоянии задачи каждого из членов команды. Помогите или перераспределите задачи у тех, кто не может решить поставленные задачи. Уточните у Заинетресованных сторон, какой результат они ожадают на следующем цикле. ")  # Рекомендация
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        k = nk

    if rabotaet_horosho == norm_rabotaet_horosho and vispolzovanii == norm_vispolzovanii:
        tr = ntr
    elif rabotaet_horosho != norm_rabotaet_horosho and vispolzovanii != norm_vispolzovanii:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Работа с использованием выбранных инструментов началась, но возникли трудности.Возможно, выбранные методы не подходят для реализации поставленных задач, предложенные Заказчиками инструменты команде незнакомы или неудобны.  ")  # Причина
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды новые инструменты и предложите их на встрече. ")  # Рекомендация
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    else:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны».Причинами неуспеха могут служить: практики и инструменты не используются, команда отстает по срокам, инструменты не подходят для разработки, в команде есть недопонимание и разногласия по поводу выбранных средств.  ")
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды сложные моменты и уточните при встрече. ")
        tr = ntr - 1

    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})

# РЕЗУЛЬТАТЫ ПО ШЕСТОМУ ЦИКЛУ
@login_required
def results_6(request):
    cycle_ = 6
    author = request.user
    nz, nv, nt, np, nr, nk, ntr = 4, 4, 4, 2, 4, 4, 5
    # Заинтересованные стороны (в согласии)
    vsoglasii = [0, 0, 0, 0, 0]
    norm_vsoglasii = ["1", "1", "1", "1", "1"]
    # Возможность (жизнеспособна)
    jiznesposobna = [0, 0, 0, 0, 0]
    norm_jiznesposobna = ["1", "1", "1", "1", "1"]
    # Требования (адресованы)
    adresovany = [0, 0, 0, 0]
    norm_adresovany = ["1", "1", "1", "1"]
    # Программная система (демонстрируемая)
    demonstriruemaya = [0, 0, 0, 0, 0, 0]
    norm_demonstriruemaya = ["1", "1", "1", "1", "1", "1"]
    # Работа (под контролем)
    podkontrolem = [0, 0, 0, 0, 0, 0, 0]
    norm_podkontrolem = ["1", "1", "1", "1", "1", "1", "1"]
    # Команда (в разработке)
    vrazrabotke = [0, 0, 0, 0, 0]
    norm_vrazrabotke = ["1", "1", "1", "1", "1"]
    # Технология работы (работает хорошо, в использовании)
    rabotaet_horosho = [0, 0, 0, 0]
    norm_rabotaet_horosho = ["1", "1", "1", "1"]
    vispolzovanii = [0, 0, 0]
    norm_vispolzovanii = ["1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('В согласии')
        list2_ = request.POST.getlist('Жизнеспособна')
        list3_ = request.POST.getlist('Адресованы')
        list4_ = request.POST.getlist('Демонстрируемая')
        list5_ = request.POST.getlist('Под контролем')
        list6_ = request.POST.getlist('В разработке')
        list7_ = request.POST.getlist('В использовании')
        list8_ = request.POST.getlist('Работает хорошо')
        projectname = request.POST.get('Проект')



    vsoglasii = repl(list_, vsoglasii)
    jiznesposobna = repl(list2_, jiznesposobna)
    adresovany = repl(list3_, adresovany)
    demonstriruemaya = repl(list4_, demonstriruemaya)
    podkontrolem = repl(list5_, podkontrolem)
    vrazrabotke = repl(list6_, vrazrabotke)
    vispolzovanii = repl(list7_, vispolzovanii)
    rabotaet_horosho = repl(list8_, rabotaet_horosho)


    res = []
    reason = []
    recommend = []
    if vsoglasii == norm_vsoglasii and\
            jiznesposobna == norm_jiznesposobna and adresovany == norm_adresovany\
            and demonstriruemaya == norm_demonstriruemaya and podkontrolem == norm_podkontrolem\
            and vrazrabotke == norm_vrazrabotke and rabotaet_horosho == rabotaet_horosho and \
            vispolzovanii == norm_vispolzovanii:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if vsoglasii != norm_vsoglasii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Причиной такого результата может быть является слабая связь участников проекта с заинтересованными сторонами, заинтересованные стороны не помогают команде, ожидания от работы не удовлетворяет заинтересованные стороны. ")  # Причина
        recommend.append("Организуйте встречу с Заинтересованными сторонами для обсуждения последующих шагов в реализации проекта. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        z = nz

    if jiznesposobna != norm_jiznesposobna:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». При выполнении задач могли возникнуть трудности. Возможно, некоторые члены команды не до конца понимают ценность проекта и конечный результат, некоторые члены команды могут по разному оценивать возможность решения проблем проекта. ")  # Причина
        recommend.append("Обсудите с командой понимание проекта и решение поставленных задач. Если мнение между командой расходиться, прийдите к общему мнение или попросите помощи у Заинтересованных сторон. ")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        v = nv


    if adresovany != norm_adresovany:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможной причиной может быть неудовлетворенность Заинтересованных сторон в получающемся результате, требования, которые применялись для решения задач, не соответсвуют требованиям Заказчика. ")  # Причина
        recommend.append("Возьмите пауза и уточните требования Заказчика, проверьте, где требования расходятся и исправьте данных ошибки перед переходом на следующий этап. ")  # Рекомендация
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        t = nt

    if demonstriruemaya != norm_demonstriruemaya:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха могут служить: ключевые архитектурные характеристики не продемонстрированы, конфигурации и интерфейсы не были продемонстрированы. ")  # Причина
        recommend.append("Предоставьте команде немного больше времени для того, чтобы найти ошибки и исправить их. Если есть трудности, которые команда не может решить сама, стоит обратить к заинтересованным сторонам для помощи или совета. ")  # Рекомендация
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    else:
        p = np

    if podkontrolem != norm_podkontrolem:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы».Причинами неуспеха могут служить: задачи не выполняются, отставание по срокам, простои в проекте, команда не справляется с задачами. ")  # Причина
        recommend.append("Перераспределите задачи между членами команды, найдите кого-то нового в команду с большей квалификацией для помощи, приостановите работу, разберитесь с незакрытыми задачами, перераспределите ресурсы и сроки выполнения и продолжите работу, исключая возникшие риски. ")  # Рекомендация
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        r = nr

    if vrazrabotke != norm_vrazrabotke:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Возможно отставание по срокам и Заинтересованные стороны не довольны достигаемым результатом. ")  # Причина
        recommend.append("Изучите выполнямые задачи,посмотрите в каком состоянии задачи каждого из членов команды. Помогите или перераспределите задачи у тех, кто не может решить поставленные задачи. Уточните у Заинетресованных сторон, какой результат они ожадают на следующем цикле. ")  # Рекомендация
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        k = nk

    if rabotaet_horosho == norm_rabotaet_horosho and vispolzovanii == norm_vispolzovanii:
        tr = ntr
    elif rabotaet_horosho != norm_rabotaet_horosho and vispolzovanii != norm_vispolzovanii:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Работа с использованием выбранных инструментов началась, но возникли трудности.Возможно, выбранные методы не подходят для реализации поставленных задач, предложенные Заказчиками инструменты команде незнакомы или неудобны.  ")  # Причина
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды новые инструменты и предложите их на встрече. ")  # Рекомендация
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    else:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны».Причинами неуспеха могут служить: практики и инструменты не используются, команда отстает по срокам, инструменты не подходят для разработки, в команде есть недопонимание и разногласия по поводу выбранных средств.  ")
        recommend.append("Проанализируйте существующие методы и инструменты и выберите те, которые больше всего подходят для проекта вашего типа. Проконсультируйте с заинтересованными сторонами, обсудите внутри команды сложные моменты и уточните при встрече. ")
        tr = ntr - 1


    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})


# РЕЗУЛЬТАТЫ ПО СЕДЬМОМУ ЦИКЛУ
@login_required
def results_7(request):
    cycle_ = 7
    author = request.user
    nz, nv, nt, np, nr, nk, ntr = 5, 5, 6, 3, 5, 4, 5
    # Заинтересованные стороны (удовлетворены для разворачивания)
    udovletvoreny_dlya_razvorachivaniya = [0, 0]
    norm_udovletvoreny_dlya_razvorachivaniya = ["1", "1"]
    # Возможность (адресована)
    adresovana = [0, 0, 0]
    norm_adresovana = ["1", "1", "1"]
    # Требования (адресованы, удовлетворены)
    adresovany = [0, 0, 0, 0]
    udovletvoreny = [0, 0, 0]
    norm_adresovany = ["1", "1", "1", "1"]
    norm_udovletvoreny = ["1", "1", "1"]
    # Программная система (демонстрируемая, пригодна для использования)
    demonstriruemaya = [0, 0, 0, 0, 0, 0]
    prigodna = [0, 0, 0, 0, 0, 0, 0]
    norm_demonstriruemaya = ["1", "1", "1", "1", "1", "1"]
    norm_prigodna= ["1", "1", "1", "1", "1", "1", "1"]
    # Работа (закончена)
    zakonchena = [0, 0, 0]
    norm_zakonchena = ["1", "1", "1"]
    # Команда (в разработке)
    vrazrabotke = [0, 0, 0, 0, 0]
    norm_vrazrabotke = ["1", "1", "1", "1", "1"]
    # Технология работы (работает хорошо, в использовании)
    rabotaet_horosho = [0, 0, 0, 0]
    norm_rabotaet_horosho = ["1", "1", "1", "1"]
    vispolzovanii = [0, 0, 0]
    norm_vispolzovanii = ["1", "1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('Удовлетворены для разворачивания')
        list2_ = request.POST.getlist('Адресована')
        list3_ = request.POST.getlist('Адресованы')
        list4_ = request.POST.getlist('Удовлетворены')
        list5_ = request.POST.getlist('Демонстрируемая')
        list6_ = request.POST.getlist('Пригодна для использования')
        list7_ = request.POST.getlist('Закончена')
        list8_ = request.POST.getlist('В разработке')
        list9_ = request.POST.getlist('В использовании')
        list10_ = request.POST.getlist('Работает хорошо')
        projectname = request.POST.get('Проект')



    udovletvoreny_dlya_razvorachivaniya = repl(list_, udovletvoreny_dlya_razvorachivaniya)
    adresovana = repl(list2_, adresovana)
    adresovany = repl(list3_, adresovany)
    udovletvoreny = repl(list4_, udovletvoreny)
    demonstriruemaya = repl(list5_, demonstriruemaya)
    prigodna = repl(list6_, prigodna)
    zakonchena = repl(list7_, zakonchena)
    vrazrabotke = repl(list8_, vrazrabotke)
    vispolzovanii = repl(list9_, vispolzovanii)
    rabotaet_horosho = repl(list10_, rabotaet_horosho)

    res = []
    reason = []
    recommend = []
    if udovletvoreny_dlya_razvorachivaniya == norm_udovletvoreny_dlya_razvorachivaniya and\
            adresovana == norm_adresovana and adresovany == norm_adresovany and\
            udovletvoreny == norm_udovletvoreny and demonstriruemaya == norm_demonstriruemaya and\
            prigodna == norm_prigodna and zakonchena == norm_zakonchena and\
            vrazrabotke == norm_vrazrabotke and rabotaet_horosho == rabotaet_horosho and \
            vispolzovanii == norm_vispolzovanii:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if udovletvoreny_dlya_razvorachivaniya != norm_udovletvoreny_dlya_razvorachivaniya:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Заинтересованные стороны до конца не удовлетворены получившимся результатом. ")  # Причина
        recommend.append("Обсудите неполучившиеся моменты и исправьте их в ближайщие сроки. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        z = nz

    if adresovana != norm_adresovana:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Возможно, получившийся результат неудобен или не до конца соответсвует обсуждаемым итогам. ")  # Причина
        recommend.append("Соберитесь командой для исправления недочетов перед завершающим этапом проектной работы. Уточните у Заказчика, какие места требуют исправлений. ")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        v = nv

    if adresovany == norm_adresovany and udovletvoreny == norm_udovletvoreny:
        t = nt
    elif adresovany != norm_adresovany and udovletvoreny != norm_udovletvoreny:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможной причиной может быть неудовлетворенность Заинтересованных сторон в получающемся результате, требования, которые применялись для решения задач, не соответсвуют требованиям Заказчика. ")  # Причина
        recommend.append("Возьмите пауза и уточните требования Заказчика, проверьте, где требования расходятся и исправьте данных ошибки перед переходом на следующий этап. ")  # Рекомендация
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможно, остались невыполненные требования или Заказчик не до конца доволен получившимся результатом. ")
        recommend.append("Обсудите с Заказчиком требования, которые остались невыполненными и завершите их перед финальным этапом проектной работы. ")
        t = nt - 1

    if demonstriruemaya == norm_demonstriruemaya and prigodna == norm_prigodna:
        p = np
    elif demonstriruemaya != norm_demonstriruemaya and prigodna != norm_prigodna:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха могут служить: ключевые архитектурные характеристики не продемонстрированы, конфигурации и интерфейсы не были продемонстрированы. ")  # Причина
        recommend.append("Предоставьте команде немного больше времени для того, чтобы найти ошибки и исправить их. Если есть трудности, которые команда не может решить сама, стоит обратить к заинтересованным сторонам для помощи или совета. ")  # Рекомендация
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    else:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». На данном этапе может быть еще не готова документация, остались незаконченные задачи после тестирования, небольшие оставания по срокам.")
        recommend.append("Предоставьте команде немного времени для закрытия оставшихся задач и исправления ошибок. Написание и проверка документации важна после готовой разрабатываемой системы. ")
        p = np - 1

    if zakonchena != norm_zakonchena:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». На данном этапе могут остаться небольшие незавершенные задачи, причинами неуспеха может быть неудовлетворенность заинтересованных сторон в получившемся результате или отставани по срокам. ")  # Причина
        recommend.append("Не заполняйте итоговую документацию, если работа не закончена до конца. Предупретите Заказчика, что будут небольшие простои и завершите рабоут корректно. ")  # Рекомендация
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        r = nr

    if vrazrabotke != norm_vrazrabotke:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причиной неуспеха данной альфы может быть неслаженная командая работа, отставание по срокам и неудовлетворенность Заинтересованных сторон получившимся результатом. ")  # Причина
        recommend.append("Пристановите работу и перераспределите ресурсы. Закончите работу до конца и приступите к заполнению итоговой документации.")  # Рекомендация
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        k = nk

    if rabotaet_horosho == norm_rabotaet_horosho and vispolzovanii == norm_vispolzovanii:
        tr = ntr
    elif rabotaet_horosho != norm_rabotaet_horosho and vispolzovanii != norm_vispolzovanii:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». На данном этапе возможной причиной может быть неполный доступ членов команды к ресурсам. Возможно, некоторые члены команды отстают по срокам по сдаче индивидуальных задач. ")  # Причина
        recommend.append("Обсудите с членами команды сложности, которые могли у них возникнуть. Решите проблему, обратившись за помощью к Заинтересованным сторонам, и закройте оставшиеся задачи. ")  # Рекомендация
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    else:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология работы' влияние оказывают альфы «Команда» и «Заинтересованные стороны». На данном этапе возможной причиной может быть неполный доступ членов команды к ресурсам. Возможно, некоторые члены команды отстают по срокам по сдаче индивидуальных задач. ")  # Причина
        recommend.append("Обсудите с членами команды сложности, которые могли у них возникнуть. Решите проблему, обратившись за помощью к Заинтересованным сторонам, и закройте оставшиеся задачи. ")  # Рекомендация
        tr = ntr - 1

    # Работа с базой
    author = request.user
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)
    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})


# РЕЗУЛЬТАТЫ ПО ВОСЬМОМУ ЦИКЛУ
@login_required
def results_8(request):
    cycle_ = 8
    author = request.user
    nz, nv, nt, np, nr, nk, ntr = 5, 6, 6, 6, 6, 5, 6
    # Заинтересованные стороны (удовлетворены для разворачивания, удовлетворены в использовании)
    udovletvoreny_dlya_razvorachivaniya = [0, 0]
    norm_udovletvoreny_dlya_razvorachivaniya = ["1", "1"]
    udovletvoreny_v_ispolzovanii = [0, 0]
    norm_udovletvoreny_v_ispolzovanii = ["1", "1"]
    # Возможность (адресована, выгода извлечена)
    adresovana = [0, 0, 0]
    norm_adresovana = ["1", "1", "1"]
    vygoda_izvlechena = [0, 0]
    norm_vygoda_izvlechena = ["1", "1"]
    # Требования (удовлетворены)
    udovletvoreny = [0, 0, 0]
    norm_udovletvoreny = ["1", "1", "1"]
    # Программная система (готова, эксплуатируется, выведена из эксплуатации )
    gotova = [0, 0, 0, 0]
    ekspluatirueca = [0, 0, 0]
    vyvedena_iz_ekspluatacii = [0, 0, 0, 0]
    norm_gotova = ["1", "1", "1", "1"]
    norm_ekspluatirueca = ["1", "1", "1"]
    norm_vyvedena_iz_ekspluatacii = ["1", "1", "1", "1"]
    # Работа (закончена, полностью закрыта)
    zakonchena = [0, 0, 0]
    polnostu_zakryta = [0, 0, 0, 0, 0, 0]
    norm_zakonchena = ["1", "1", "1"]
    norm_polnostu_zakryta = ["1", "1", "1", "1", "1", "1"]
    # Команда (в разработке, расформирована)
    vrazrabotke = [0, 0, 0, 0, 0]
    rasformirovana = [0, 0, 0]
    norm_vrazrabotke = ["1", "1", "1", "1", "1"]
    norm_rasformirovana = ["1", "1", "1"]
    # Технология работы (работает хорошо, в использовании, не используется)
    rabotaet_horosho = [0, 0, 0, 0]
    norm_rabotaet_horosho = ["1", "1", "1", "1"]
    vispolzovanii = [0, 0, 0]
    norm_vispolzovanii = ["1", "1", "1"]
    ne_ispolzueca = [0, 0]
    norm_ne_ispolzueca = ["1", "1"]

    if request.method == 'POST':
        list_ = request.POST.getlist('Удовлетворены для разворачивания')
        list2_ = request.POST.getlist('Удовлетворены в использовании')
        list3_ = request.POST.getlist('Адресована')
        list4_ = request.POST.getlist('Выгода извлечена')
        list5_ = request.POST.getlist('Удовлетворены')
        list6_ = request.POST.getlist('Готова')
        list7_ = request.POST.getlist('Эксплуатируется')
        list8_ = request.POST.getlist('Выведена из эксплуатации')
        list9_ = request.POST.getlist('Работа закончена')
        list10_ = request.POST.getlist('Полностью закрыта')
        list11_ = request.POST.getlist('В разработке')
        list12_ = request.POST.getlist('Расформирована')
        list13_ = request.POST.getlist('В использовании')
        list14_ = request.POST.getlist('Работает хорошо')
        list15_ = request.POST.getlist('Не используется')
        projectname = request.POST.get('Проект')


    udovletvoreny_dlya_razvorachivaniya = repl(list_, udovletvoreny_dlya_razvorachivaniya)
    udovletvoreny_v_ispolzovanii = repl(list2_, udovletvoreny_v_ispolzovanii)
    adresovana = repl(list3_, adresovana)
    vygoda_izvlechena = repl(list4_, vygoda_izvlechena)
    udovletvoreny = repl(list5_, udovletvoreny)
    gotova = repl(list6_, gotova)
    ekspluatirueca = repl(list7_, ekspluatirueca)
    vyvedena_iz_ekspluatacii = repl(list8_, vyvedena_iz_ekspluatacii)
    zakonchena = repl(list9_, zakonchena)
    polnostu_zakryta = repl(list10_, polnostu_zakryta)
    vrazrabotke = repl(list11_, vrazrabotke)
    rasformirovana = repl(list12_, rasformirovana)
    vispolzovanii = repl(list13_, vispolzovanii)
    rabotaet_horosho = repl(list14_, rabotaet_horosho)
    ne_ispolzueca = repl(list15_, ne_ispolzueca)

    res = []
    reason = []
    recommend = []
    if udovletvoreny_dlya_razvorachivaniya == norm_udovletvoreny_dlya_razvorachivaniya and\
            udovletvoreny_v_ispolzovanii == norm_udovletvoreny_v_ispolzovanii and\
            adresovana == norm_adresovana and vygoda_izvlechena == norm_vygoda_izvlechena and\
            udovletvoreny == norm_udovletvoreny and gotova == norm_gotova and\
            ekspluatirueca == norm_ekspluatirueca and\
            vyvedena_iz_ekspluatacii == norm_vyvedena_iz_ekspluatacii and\
            zakonchena == norm_zakonchena and polnostu_zakryta == norm_polnostu_zakryta and\
            vrazrabotke == norm_vrazrabotke and rasformirovana == norm_rasformirovana and\
            vispolzovanii == norm_vispolzovanii and  rabotaet_horosho == norm_rabotaet_horosho and\
            ne_ispolzueca == norm_ne_ispolzueca:
        res.append("Все сущности достигли нормального состояния.")
        z, v, t, p, r, k, tr = nz, nv, nt, np, nr, nk, ntr

    if udovletvoreny_dlya_razvorachivaniya == norm_udovletvoreny_dlya_razvorachivaniya and udovletvoreny_v_ispolzovanii == norm_udovletvoreny_v_ispolzovanii:
        z = nz
    elif udovletvoreny_dlya_razvorachivaniya != norm_udovletvoreny_dlya_razvorachivaniya and udovletvoreny_v_ispolzovanii != norm_udovletvoreny_v_ispolzovanii:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Заинтересованные стороны до конца не удовлетворены получившимся результатом. ")  # Причина
        recommend.append("Рассмотрите проблемные места и неполучившиемя задачи, исправьте их в ближайщие сроки. ")  # Рекомендация
        z = get_value_for_graph(cycle_, "zainteresovannye_storony", author, projectname)
    else:
        res.append("Сущность Заинтересованные стороны не достигла нормального состояния.")
        reason.append("Заинтересованные стороны до конца не удовлетворены получившимся результатом. ")  # Причина
        recommend.append("Изучите проблемные моменты, если есть время исправьте в кратчайщие сроки, если времени нет, закрывайте проект с недочетами. ")  # Рекомендация
        z = nz - 1

    if adresovana == norm_adresovana and vygoda_izvlechena == norm_vygoda_izvlechena:
        v = nv
    elif adresovana != norm_adresovana and vygoda_izvlechena != norm_vygoda_izvlechena:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Возможно, получившийся результат неудобен или не до конца соответсвует обсуждаемым итогам. ")  # Причина
        recommend.append("Соберитесь командой для обсуждения получившихся результатов, если есть возможность для исправления недочетов, воспользуйтесь ею. Сделайте выводы для дальнейших проектных работ.")  # Рекомендация
        v = get_value_for_graph(cycle_, "vosmojnost", author, projectname)
    else:
        res.append("Сущность Возможность не достигла нормального состояния.")
        reason.append("На альфу 'Возможность' прямое влияние оказывает альфа «Заинтересованные стороны». Причиной неудачи данной альфы может быть то, что система не приносит выгоды или дохода, возможно, в рамках вашего проекта данные пункты необязательны. ")# Причина
        recommend.append(" Соберитесь командой для обсуждения получившихся результатов, если есть возможность для исправления недочетов, воспользуйтесь ею. Сделайте выводы для дальнейших проектных работ.")  # Рекомендация
        v = nv - 1

    if udovletvoreny != norm_udovletvoreny:
        res.append("Сущность Требования не достигла нормального состояния.")
        reason.append("На альфу 'Требования' влияют альфы «Возможность» и «Заинтересованные стороны». Возможно, остались невыполненные требования или Заказчик не до конца доволен получившимся результатом. ")
        recommend.append("Обсудите с Заказчиком требования, которые остались невыполненными. Сделайте выводы для работы в следующих проектах.  ")
        t = get_value_for_graph(cycle_, "trebovaniya", author, projectname)
    else:
        t = nt

    if gotova == norm_gotova and ekspluatirueca == norm_ekspluatirueca and vyvedena_iz_ekspluatacii == norm_vyvedena_iz_ekspluatacii:
        p = np
    elif gotova != norm_gotova and ekspluatirueca != norm_ekspluatirueca and vyvedena_iz_ekspluatacii != norm_vyvedena_iz_ekspluatacii:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха на данном этапе может служить неудовлетворенность Заинтересованных сторон в итоговом решении.  ")  # Причина
        recommend.append("Оцените проделанную работу и найдите слабые места. Обсудите их с Заинтересованными сторонами и полученные навыки применяйте в следующих проектах. ")  # Рекомендация
        p = get_value_for_graph(cycle_, "programmnaya_sistema", author, projectname)
    elif gotova != norm_gotova and ekspluatirueca != norm_ekspluatirueca or gotova != norm_gotova and vyvedena_iz_ekspluatacii != norm_vyvedena_iz_ekspluatacii or ekspluatirueca != norm_ekspluatirueca and vyvedena_iz_ekspluatacii != norm_vyvedena_iz_ekspluatacii:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха на данном этапе может служить неудовлетворенность Заинтересованных сторон в итоговом решении.  ")  # Причина
        recommend.append("Оцените проделанную работу и найдите слабые места. Обсудите их с Заинтересованными сторонами и полученные навыки применяйте в следующих проектах. ")  # Рекомендация
        p = np - 2
    else:
        res.append("Сущность Программная система не достигла нормального состояния.")
        reason.append("На альфу 'Программная система' влияние оказывает альфа «Работа». Причинами неуспеха на данном этапе может служить неудовлетворенность Заинтересованных сторон в итоговом решении.  ")  # Причина
        recommend.append("Оцените проделанную работу и найдите слабые места. Обсудите их с Заинтересованными сторонами и полученные навыки применяйте в следующих проектах. ")  # Рекомендация
        p = np - 1

    if zakonchena == norm_zakonchena and polnostu_zakryta == norm_polnostu_zakryta:
        r = nr
    elif zakonchena != norm_zakonchena and polnostu_zakryta != norm_polnostu_zakryta:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». На данном этапе могут остаться небольшие незавершенные задачи, причинами неуспеха может быть неудовлетворенность заинтересованных сторон в получившемся результате или отставани по срокам. ")  # Причина
        recommend.append("Проверьте поставленные в начале проекта и проанализируйте завершение рабочего проекта. Поговорите с Заинтересованными стороными, прислушайтесь к советами и применяйте их в дальнейших проектах. ")  # Рекомендация
        r = get_value_for_graph(cycle_, "rabota", author, projectname)
    else:
        res.append("Сущность Работа не достигла нормального состояния.")
        reason.append("На альфу 'Работа' влияние оказывают альфы «Требования», «Возможность», «Технология работы». На данном этапе могут остаться небольшие незавершенные задачи, причинами неуспеха может быть неудовлетворенность заинтересованных сторон в получившемся результате или отставани по срокам. ")  # Причина
        recommend.append("Проверьте поставленные в начале проекта и проанализируйте завершение рабочего проекта. Поговорите с Заинтересованными стороными, прислушайтесь к советами и применяйте их в дальнейших проектах. ")  # Рекомендация
        r = nr - 1

    if vrazrabotke == norm_vrazrabotke and rasformirovana == norm_rasformirovana:
        k = nk
    elif vrazrabotke != norm_vrazrabotke and rasformirovana != norm_rasformirovana:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причиной неуспеха данной альфы может быть неслаженная командая работа, отставание по срокам и неудовлетворенность Заинтересованных сторон получившимся результатом. ")  # Причина
        recommend.append("Определите с командой все трудные моменты в работе на протяжении хода проекта, сделайте выводы и применяйте полученные навыки для участия в следующих проектах.")  # Рекомендация
        k = get_value_for_graph(cycle_, "komanda", author, projectname)
    else:
        res.append("Сущность Команда не достигла нормального состояния.")
        reason.append("На альфу 'Команда' влияние оказывает альфа «Заинтересованные стороны». Причиной неуспеха данной альфы может быть неслаженная командая работа, отставание по срокам и неудовлетворенность Заинтересованных сторон получившимся результатом. ")  # Причина
        recommend.append("Определите с командой все трудные моменты в работе на протяжении хода проекта, сделайте выводы и применяйте полученные навыки для участия в следующих проектах.")  # Рекомендация
        k = nk - 1


    if rabotaet_horosho == norm_rabotaet_horosho and vispolzovanii == norm_vispolzovanii and ne_ispolzueca == norm_ne_ispolzueca:
        tr = ntr
    elif rabotaet_horosho != norm_rabotaet_horosho and vispolzovanii != norm_vispolzovanii and ne_ispolzueca != norm_ne_ispolzueca:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Причиной неуспеха может служить неполное использование запланированных методов и инструментов при разработке, выбранные методики отличались от заявленных. ")  # Причина
        recommend.append("Проанализируйте с командой конечный выбор инструментальных средст для разработки и обоснуйте. Сделайте выводы для участия в  следующих проектах. ")  # Рекомендация
        tr = get_value_for_graph(cycle_, "tehnologiya_raboty", author, projectname)
    elif rabotaet_horosho != norm_rabotaet_horosho and vispolzovanii != norm_vispolzovanii or vispolzovanii != norm_vispolzovanii and ne_ispolzueca != norm_ne_ispolzueca or rabotaet_horosho != norm_rabotaet_horosho and ne_ispolzueca != norm_ne_ispolzueca:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Причиной неуспеха может служить неполное использование запланированных методов и инструментов при разработке, выбранные методики отличались от заявленных. ")  # Причина
        recommend.append( "Проанализируйте с командой конечный выбор инструментальных средст для разработки и обоснуйте. Сделайте выводы для участия в  следующих проектах. ")  # Рекомендация
        tr = ntr - 2
    else:
        res.append("Сущность Технология работы не достигла нормального состояния.")
        reason.append("На альфу 'Технология' влияние оказывают альфы «Команда» и «Заинтересованные стороны». Причиной неуспеха может служить неполное использование запланированных методов и инструментов при разработке, выбранные методики отличались от заявленных. ")  # Причина
        recommend.append("Проанализируйте с командой конечный выбор инструментальных средст для разработки и обоснуйте. Сделайте выводы для участия в  следующих проектах. ")  # Рекомендация
        tr = ntr - 1

    # Работа с базой
    z, v, t, p, r, k, tr = get_val(cycle_, z, v, t, p, r, k, tr, author, projectname)

    graph_div = plotly.offline.plot(graph(nz, nv, nt, np, nr, nk, ntr, z, v, t, p, r, k, tr), auto_open=False, output_type="div")
    return render(request, 'main/results.html', {'res': res, "reason": reason, "recommend": recommend, "graph_div": graph_div})

