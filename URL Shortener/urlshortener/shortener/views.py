from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
from django.views.decorators.csrf import csrf_exempt
from .utils import get_unique_uid


@csrf_exempt
def create(request):
    """
    Creates a random, unique short url from the original url.
    """
    if request.method == 'POST':
        url_decoded = request.body.decode('utf-8')
        url = url_decoded.split('url:')[1][:-2]  # In order to get only the url
        uid = get_unique_uid()
        new_url = Url(original_url=url, short_url=uid, counter=0)
        new_url.save()
        return HttpResponse('http://localhost:8000/s/' + uid)
    return HttpResponse('Only POST request are valid')


def redirect(request, short_url):
    """
    Redirects the short url to the original url.
    """
    obj = Url.objects.filter(short_url=short_url).first()
    if not obj:
        return HttpResponse("This url doesn't exist")

    obj.counter += 1
    obj.save()
    return HttpResponseRedirect(obj.original_url)
