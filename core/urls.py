from django.urls import path
from core.views.stk_push import STKPush
from core.views.stk_push_success import STKPushSuccess
from django.views.decorators.csrf import csrf_exempt

app_name = 'core'

urlpatterns = [
    path('', csrf_exempt(STKPush.as_view()), name='stk-push'),
    path('stk-push-success/', STKPushSuccess.as_view(), name='stk-push-success'),
]
