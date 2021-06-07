from django.http import HttpResponse
def showIndex(http_request):
    message='''<html>
<h1>heloooo</h1>
</html>'''

    return HttpResponse(message)


