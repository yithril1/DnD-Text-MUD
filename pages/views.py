from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from game.models import Character
from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.http import Http404

class CharacterDetailView(DetailView):
    model = Character
    template = 'character_detail.html'
    def character_detail_view(request,pk):
        try:
            character_id = Character.objects.get(pk=pk)
        except Character.DoesNotExist:
            raise Http404("Character does not exist.")
        # book_id=get_object_or_404(Book, pk=pk)

        return render(
                request,
                'character_detail.html',
                context={'character': character_id, }
            )

class HomePageView(ListView):
    template_name = 'home.html'
    model = Character
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Character.objects.filter(account = self.request.user).order_by('name')


def get_max_chars(request):
    chars = Character.objects.filter(account=request.user)
    fail=0
    if chars.count() > 9:
        fail = 1
    else:
        fail = 0
    print(fail)
    return JsonResponse({
            'fail': fail,
            'url': reverse('creation'),
        })


