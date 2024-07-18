from .models import limage

def liog(request):
    latest_logo = limage.objects.all()
    return {"logo":latest_logo}