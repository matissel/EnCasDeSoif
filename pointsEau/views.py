from django.shortcuts import render
from .forms import PointEauForm

# Create your views here.
def addPE(request):
    if request.method == 'POST':
        form = PointEauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pointsEau')
        else:
            return redirect('/pointsEau/add')
    else:
        form = PointEauForm()
        args = {'form': form}
    return render(request, 'pointsEau/newPE.html', args)