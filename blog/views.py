from django.shortcuts import render


def index(request):

    context = {
        'judul': 'Home Page | BLOG',
        'subjudul': 'Header BLOG',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }

    return render(request, 'index.html', context)
