from django.shortcuts import render


def custom_not_found_page(request, exception):
    return render(request, 'custom_404.html', status=404)