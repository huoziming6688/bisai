from django.shortcuts import render
from django.views.generic import View
from .models import House, HouseDetail
# Create your views here.


class indexrecommend(View):
    def get(self, request):
        all_houses = House.objects.all()[:6]
        all_details = HouseDetail.objects.all()[:6]

        return render(request, 'index.html', {
            'all_houses': all_houses
        })




