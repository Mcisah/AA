from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from poll.models import Category, Contestant, Vote, Sum
from django.db.models import Q


def vote(request):
    if 'vote_student' in request.POST:
        contestant = request.POST.get('student_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")


        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=1).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="1")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj41&category=student")

    elif 'vote_face' in request.POST:
        contestant = request.POST.get('face_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=3).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="3")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj43&category=face")

    elif 'vote_couple' in request.POST:
        contestant = request.POST.get('couple_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=2).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="2")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj42&category=couple")

    elif 'vote_popular' in request.POST:
        contestant = request.POST.get('popular_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=5).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="5")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj45&category=popular")

    elif 'vote_entrepreneur' in request.POST:
        contestant = request.POST.get('entrepreneur_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=4).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="4")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj44&category=entrepreneur")

    elif 'vote_fashion_male' in request.POST:
        contestant = request.POST.get('fashionable_male_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=6).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="6")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj46&category=f_male")

    elif 'vote_fashion_female' in request.POST:
        contestant = request.POST.get('fashionable_female_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=7).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="7")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj47&category=f_female")

    elif 'vote_personality' in request.POST:
        contestant = request.POST.get('personality_year', '')
        if contestant == '':
            return HttpResponseRedirect("/poll/?response=no_count")

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        vote_count = Vote.objects.filter(ip_ad=ipaddress, category=8).count()
        if vote_count > 0:
            return HttpResponseRedirect("/poll/?response=already")
        else:
            pass

        voted = Vote(ip_ad=ipaddress, contestant=contestant, category="8")
        voted.save()

        contestant_here = Contestant.objects.get(id=contestant)
        contestant_here.votes += 1
        contestant_here.save()

        return HttpResponseRedirect("/poll/?board=rj48&category=personality")

    else:
        return HttpResponseRedirect("/poll/?response=no_count")


def index(request):
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

    student_year = Contestant.objects.filter(category=1)
    couple_year = Contestant.objects.filter(category=2)
    face_year = Contestant.objects.filter(category=3)
    entrepreneur_year = Contestant.objects.filter(category=4)
    popular_year = Contestant.objects.filter(category=5)
    fashionable_male_year = Contestant.objects.filter(category=6)
    fashionable_female_year = Contestant.objects.filter(category=7)
    personality_year = Contestant.objects.filter(category=8)
    other_year = Contestant.objects.filter(category=9)



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


def result(request):

    student_category = Category.objects.get(id=1)
    couple_category = Category.objects.get(id=2)
    face_category = Category.objects.get(id=3)
    entrepreneur_category = Category.objects.get(id=4)
    popular_category = Category.objects.get(id=5)
    fashionable_male_category = Category.objects.get(id=6)
    fashionable_female_category = Category.objects.get(id=7)
    personality_category = Category.objects.get(id=8)
    other_category = Category.objects.get(id=9)

    student_year = Contestant.objects.filter(category=1)
    couple_year = Contestant.objects.filter(category=2)
    face_year = Contestant.objects.filter(category=3)
    entrepreneur_year = Contestant.objects.filter(category=4)
    popular_year = Contestant.objects.filter(category=5)
    fashionable_male_year = Contestant.objects.filter(category=6)
    fashionable_female_year = Contestant.objects.filter(category=7)
    personality_year = Contestant.objects.filter(category=8)
    other_year = Contestant.objects.filter(category=9)

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
