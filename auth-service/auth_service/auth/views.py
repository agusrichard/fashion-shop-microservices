from django.http import HttpResponse


def index(request):
    print('I GET THE REQUEST MAN!')
    return HttpResponse('HELLO WORLD')
