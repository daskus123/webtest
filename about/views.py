from django.shortcuts import render


def index(request):

    context = {
        'judul': 'Home Page | About',
        'subjudul': 'Header About',
        'banner': 'about/img/banner_about.png',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }

    return render(request, 'index.html', context)
