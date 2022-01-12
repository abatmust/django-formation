from .models import Profile
from blog.models import Tag
from django.db.models import Q


def search_profiles(request):

    keyword = ""
    if request.GET.get('search'):
        keyword = request.GET.get("search")

    # tags = Tag.objects.filter(name__icontains=keyword)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=keyword) |
        Q(username__icontains=keyword) |
        Q(email__icontains=keyword)  # |
        # Q(tags__in=tags)
    )

    return profiles, keyword
