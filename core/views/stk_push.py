from django.shortcuts import render, redirect
from django.views import View

from core.forms.fields import STKPushForm
from core.utils.initiate import InitiateStkPush
from core.utils.token import AccessToken

access = AccessToken().get_token()

initiate = InitiateStkPush()


class STKPush(View):
    def get(self, *args, **kwargs):
        form = STKPushForm()
        context = {'form': form}
        return render(self.request, 'stk_push.html', context)

    def post(self, request, *args, **kwargs):
        form = STKPushForm(self.request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            reference = 'MURSTECH'  # form.cleaned_data['reference']
            description = 'MURSTECH'  # form.cleaned_data['description']
            print(phone_number)
            print(amount)
            response = initiate.stk_push(int(phone_number), int(amount), reference, description)
            print(response)
            #return JsonResponse(response)
            return redirect('core:stk-push-success')