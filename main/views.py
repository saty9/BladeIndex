from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from main.models import Competitor, RatingTable, Rating
from rest_framework import viewsets


def rating_table_list(request):
    tables = RatingTable.objects.values('pk', 'name')
    return JsonResponse({'tables': list(tables)})


def rating_table_participants(request, name):
    table = get_object_or_404(RatingTable, name=name)
    participants = Competitor.objects.filter(rating__rating_table=table)
    return JsonResponse({'table': table.id,
                         'participants': participants})


def ratings(request, table_id, competitor_id):
    ratings = Rating.objects.filter(table_id=table_id, competitor_id=competitor_id) \
        .order_by('-time') \
        .values('value', 'time')
    return JsonResponse(ratings)


def update_rating(request, table_id):
    if request.method != 'POST':
        return JsonResponse("Error")
    winner = get_object_or_404(Competitor, pk=request.POST['winner_id'])
    looser = get_object_or_404(Competitor, pk=request.POST['loser_id'])
    table = get_object_or_404(RatingTable, pk=table_id)
    winner_rating, looser_rating = table.update_ratings(winner,
                                                        looser,
                                                        int(request.POST['w_score']),
                                                        int(request.POST['l_score']))
    return JsonResponse({'w_r': winner_rating,
                         'l_r': looser_rating})


def competitors(request):
    if request.method == 'POST':
        competitor = Competitor.objects.create(name=request.POST['name'])
        return JsonResponse({'id': competitor.id})
    elif request.GET['name']:
        name = request.GET['name']
        if len(name) < 3:
            return JsonResponse({'success': False})
        filtered_competitors = list(Competitor.objects.filter(name__icontains=name)[:10].values('name', 'id'))
        return JsonResponse({'competitors': filtered_competitors})


def table_data(request, name):
    table = get_object_or_404(RatingTable, name=name)
    ratings = Rating.objects.filter(rating_table=table).select_related('competitor').order_by('competitor', '-time')
    out = []
    current = None
    for r in ratings:
        if r.competitor_id != current:
            out.append({'history': [], 'name': r.competitor.name, 'id': r.competitor_id, 'rating': r.value})
            current = r.competitor_id
        out[-1]['history'].append(r.value)

    return JsonResponse({'data': out})



