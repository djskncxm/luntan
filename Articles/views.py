from django.views import View
from django.http import JsonResponse

class Index(View):
    def get(self, requests):
        return JsonResponse({'code':'200 OK'})

