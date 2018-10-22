from django.shortcuts import render, get_object_or_404

from main.models import RatingTable


def new_results(request):
    return render(request, 'ui/new_results.html')


def results(request, table_name):
    table = get_object_or_404(RatingTable, name=table_name)
    return render(request, "ui/results.html", context={'table': table})
