#from django.shortcuts import render_to_response
from django.http import HttpResponse


def test(request):
    if request.method == 'GET':
        return HttpResponse('test.html')
    elif request.method == 'POST':
        if request.is_ajax():
            message = "Yes, AJAX!"
        else:
            message = "Not Ajax"
        return HttpResponse(message)
    # alternative test: return render_to_response('test_results.html')
