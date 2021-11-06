from .models import *
from .views import *


def count(request):

    items_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            if request.user.is_authenticated:
                ct = CartList.objects.filter(user=request.user)
                cti = Items.objects.all().filter(cart=ct[:1])
                for c in cti:
                    items_count += c.iquan
        except CartList.DoesNotExist:
            items_count = 0
        return dict(itc=items_count)
