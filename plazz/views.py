from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from plazz.models import Form, FormField, FieldOption, Location, Neighbourhood, NeighbourhoodCity


def index(request):
    city_form = FieldOption.objects.filter(formfield__form__name="Plaats").filter(
        formfield__form__enabled=True).order_by('index')
    context = {'form': city_form}
    return render(request, 'home.html', context)


def filters(request, city):
    form_fields = FormField.objects.raw(
        'SELECT * FROM "plazz_formfield" INNER JOIN "plazz_form" ON ("plazz_formfield"."form_id" = "plazz_form"."id")INNER JOIN "plazz_fieldtype" ON ("plazz_formfield"."fieldtype_id" = "plazz_fieldtype"."id")WHERE ("plazz_form"."name" = \'Filters\' AND "plazz_form"."enabled" = True)ORDER BY "plazz_formfield"."index" ASC')
    form_option = FieldOption.objects.raw(
        'SELECT * FROM "plazz_fieldoption" INNER JOIN "plazz_formfield" ON ("plazz_fieldoption"."formfield_id" = "plazz_formfield"."id")INNER JOIN "plazz_form" ON ("plazz_formfield"."form_id" = "plazz_form"."id")WHERE ("plazz_form"."name" = \'Filters\' AND "plazz_form"."enabled" = True) ORDER BY plazz_fieldoption."index", "plazz_formfield"."index"  ASC')
    context = {
        'form_fields': form_fields,
        'form_options': form_option
    }
    return render(request, 'filters.html', context)


def results(request):
    pricerent_min = request.POST.get("min-huurprijs", 0)
    pricerent_max = request.POST.get("max-huurprijs", 99999999)
    space_min = request.POST.get("vierkante-meter-min", 0)
    space_max = request.POST.get("vierkante-meter-max", 9999999)

    if pricerent_max == 'Geen maximum':
        pricerent_max = 99999999999
    if space_min == '':
        space_min = 0
    if space_max == '':
        space_max = 99999

    locations = Location.objects\
        .select_related('street')\
        .filter(rent_month__gte=pricerent_min, rent_month__lte=pricerent_max)\
        .filter(square_meter__gte=space_min, square_meter__lte=space_max)
    rentweight = locations.aggregate(Avg('rent_month'))
    spaceweight = locations.aggregate(Avg('square_meter'))


    rentweight = rentweight["rent_month__avg"]
    spaceweight = spaceweight["square_meter__avg"]

    if rentweight is None:
        rentweight = 0

    def calcratingrent(loc):
        ratingrentprice = int(rentweight) / float(loc.rent_month)
        if ratingrentprice > 2:
            ratingrentprice = 2.0
        elif ratingrentprice < 0.5:
            ratingrentprice = 0.5
        return ratingrentprice

    def calculatingspace(loc):
        ratingspace = int(loc.square_meter) / int(spaceweight)
        if ratingspace > 2:
            ratingspace = 2.0
        elif ratingspace < 0.5:
            ratingspace = 0.5
        return ratingspace

    def calculatingage():
        ageweight = 30  # gem van de leeftijd van de doorgegeven locaties
        getage = input("Age?")
        ratingage = int(getage) / ageweight
        if ratingage > 2:
            ratingage = 2.0
        elif ratingage < 0.5:
            ratingage = 0.5
        return ratingage

    def calculatingcompetition(loc):
        competitionweight = Location.objects\
        .get(loc)
        #.values_list('neighbourhood__neighbourhoodcity__Avg_restaurant_amt_3_km', flat=True)[0]
        getage = input("Age?")
        ratingage = int(getage) / competitionweight
        if ratingage > 2:
            ratingage = 2.0
        elif ratingage < 0.5:
            ratingage = 0.5
        return ratingage

    def calculatingeducation():
        eduniveau = 2
        getedu = input("Education?")
        secedu = "secondary"
        secvoc = "secondary vocational"
        higherprof = "higher prof"
        womaster = "wo master"
        if getedu == secedu:
            eduniveau = 1
        elif getedu == secvoc:
            eduniveau = 2
        elif getedu == higherprof:
            eduniveau = 3
        elif getedu == womaster:
            eduniveau = 4
        else:
            eduniveau = 0
        ratingedu = int(eduniveau) / 2
        if ratingedu > 2:
            ratingedu = 2.0
        elif ratingedu < 0.5:
            ratingedu = 0.5
        return ratingedu

    def calculatingrating(loc):
        rent = calcratingrent(loc)
        space = calculatingspace(loc)
        # age = calculatingage()
        # education = calculatingeducation()
        #competition = calculatingcompetition(loc)
        totalrating = rent + space #+ competition # + age + education
        return totalrating

    results = []
    for location in locations:
        results.append([location, calculatingrating(location)])

    context = {
        'results': results
    }

    return render(request, 'results.html', context)

# def vote(request, question_id):
#     #question = get_object_or_404(Question, pk=question_id)
#     try:
#         #selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
