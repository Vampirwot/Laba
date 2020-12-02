from django.shortcuts import render


def handler404(request, *args, **argv):
    response = render(request, '404.html', status=404)
    return response
