from announcement.models import Announcement

def announce(request):
    msg_text = Announcement.objects.all()
    return {"message":msg_text}