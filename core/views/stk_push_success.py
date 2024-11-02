from django.shortcuts import render
from django.views import View


class STKPushSuccess(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'stk_push_success.html')
