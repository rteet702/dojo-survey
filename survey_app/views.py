from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    if 'submission_data' in request.session:
        request.session.pop('submission_data')
    return render(request, 'index.html')


def submit(request):
    request.session['submission_data'] = request.POST
    return redirect('/success')


def success(request):
    context = {
        'name' : request.session['submission_data'].get('name'),
        'location' : request.session['submission_data'].get('location'),
        'language' : request.session['submission_data'].get('language'),
        'comment' : request.session['submission_data'].get('comment')
    }
    # Since we don't want that data stuck in session, clear it.
    return render(request, 'success.html', context)