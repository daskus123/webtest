from django.shortcuts import render


def index(request):

    context = {
        'judul': 'Home Page | Website',
        'subjudul': 'Header Homepage',
        'banner': 'img/banner_home.png',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }

    return render(request, 'index.html', context)
