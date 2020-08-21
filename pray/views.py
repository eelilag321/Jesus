from django.shortcuts import render
from . models import Prayer
from django.views.generic import CreateView, ListView
from . forms import PrayerCreateForm

def index(request):
    return render(request, 'pray/index.html')

def pray(request):
    return render(request, 'pray/prayer_form.html')

class PrayerCreateView(CreateView):
    form_class = PrayerCreateForm
    template_name = 'pray/prayer_form.html'
    success_url = '/pray'
    pray_success = False

    def form_valid(self, form):
        self.pray_success = True
        super(PrayerCreateView, self).form_valid(form)
        return render(self.request, self.template_name,
                      self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        ctx = super(PrayerCreateView, self).get_context_data(**kwargs)
        ctx['pray_success'] = self.pray_success
        return ctx

class PrayerListView(ListView) :
    model = Prayer
    prayerCount = model.objects.all().count()
    template_name = 'pray/prayer_list.html'
    context_object_name = 'prayers'
    ordering = ['-date']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        ctx = super(PrayerListView, self).get_context_data(**kwargs)
        ctx['prayerCount'] = self.prayerCount
        return ctx


def about(request):
    return render(request, 'pray/about.html')
