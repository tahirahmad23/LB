from .models import Department
from accounts.models import Uploader
def default(request):
    departments = Department.objects.all()
    try:
        is_uploader = Uploader.objects.get(user=request.user)
        is_uploader = True
    except:
        is_uploader = False
    return {
    "departments" : departments,
    "is_uploader" : is_uploader
    }
