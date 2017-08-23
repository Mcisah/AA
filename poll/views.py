from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from poll.models import Category, Contestant, Vote, Sum
from django.db.models import Q


def oldindex(request):
    if request.GET.get('board') and request.GET.get('category'):
        board = request.GET.get('board')
        category = request.GET.get('category')
    else:
        board = ''
        category = ''

    if request.GET.get('response'):
        response = request.GET.get('response')
    else:
        response = ''

    student_category = Category.objects.get(id=1)
    couple_category = Category.objects.get(id=2)
    face_category = Category.objects.get(id=3)
    entrepreneur_category = Category.objects.get(id=4)
    popular_category = Category.objects.get(id=5)
    fashionable_male_category = Category.objects.get(id=6)
    fashionable_female_category = Category.objects.get(id=7)
    personality_category = Category.objects.get(id=8)
    other_category = Category.objects.get(id=9)

    student_year = Contestant.objects.filter(category=1).order_by('id')
    couple_year = Contestant.objects.filter(category=2).order_by('id')
    face_year = Contestant.objects.filter(category=3).order_by('id')
    entrepreneur_year = Contestant.objects.filter(category=4).order_by('id')
    popular_year = Contestant.objects.filter(category=5).order_by('id')
    fashionable_male_year = Contestant.objects.filter(category=6).order_by('id')
    fashionable_female_year = Contestant.objects.filter(category=7).order_by('id')
    personality_year = Contestant.objects.filter(category=8).order_by('id')
    other_year = Contestant.objects.filter(category=9).order_by('id')



    return render(request, "poll/index.html", {
        'response': response,
        'category': category,
        'board': board,
        'student_category': student_category,
        'couple_category': couple_category,
        'face_category': face_category,
        'entrepreneur_category': entrepreneur_category,
        'popular_category': popular_category,
        'fashionable_male_category': fashionable_male_category,
        'fashionable_female_category': fashionable_female_category,
        'personality_category': personality_category,
        'other_category': other_category,
        'student_year': student_year,
        'couple_year': couple_year,
        'face_year': face_year,
        'entrepreneur_year': entrepreneur_year,
        'popular_year': popular_year,
        'fashionable_male_year': fashionable_male_year,
        'fashionable_female_year': fashionable_female_year,
        'personality_year': personality_year,
        'other_year': other_year,
    })


def index(request):

    student_category = Category.objects.get(id=1)
    couple_category = Category.objects.get(id=2)
    face_category = Category.objects.get(id=3)
    entrepreneur_category = Category.objects.get(id=4)
    popular_category = Category.objects.get(id=5)
    fashionable_male_category = Category.objects.get(id=6)
    fashionable_female_category = Category.objects.get(id=7)
    personality_category = Category.objects.get(id=8)
    other_category = Category.objects.get(id=9)

    student_year = Contestant.objects.filter(category=1).order_by('id')
    couple_year = Contestant.objects.filter(category=2).order_by('id')
    face_year = Contestant.objects.filter(category=3).order_by('id')
    entrepreneur_year = Contestant.objects.filter(category=4).order_by('id')
    popular_year = Contestant.objects.filter(category=5).order_by('id')
    fashionable_male_year = Contestant.objects.filter(category=6).order_by('id')
    fashionable_female_year = Contestant.objects.filter(category=7).order_by('id')
    personality_year = Contestant.objects.filter(category=8).order_by('id')
    other_year = Contestant.objects.filter(category=9).order_by('id')

    return render(request, "poll/results.html", {
        'student_category': student_category,
        'couple_category': couple_category,
        'face_category': face_category,
        'entrepreneur_category': entrepreneur_category,
        'popular_category': popular_category,
        'fashionable_male_category': fashionable_male_category,
        'fashionable_female_category': fashionable_female_category,
        'personality_category': personality_category,
        'other_category': other_category,
        'student_year': student_year,
        'couple_year': couple_year,
        'face_year': face_year,
        'entrepreneur_year': entrepreneur_year,
        'popular_year': popular_year,
        'fashionable_male_year': fashionable_male_year,
        'fashionable_female_year': fashionable_female_year,
        'personality_year': personality_year,
        'other_year': other_year,
    })


def about(request):
    return render(request, "poll/about.html")
