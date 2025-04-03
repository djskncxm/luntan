from django.http import JsonResponse
from django.views import View


class Index(View):
    def get(self, requests):
        return JsonResponse({'code':"200 OK!!"})

