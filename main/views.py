from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, View
from main.forms import QuoteForm, SubscriptionAddProductForm
from main.models import AddQuote, AddSubscriptionProduct

# Create your views here.


def index(request):
    form = AddQuote.objects.all()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def tables_dynamic(request):
    return render(request, 'tables_dynamic.html')


def new_quote(request):
    return render(request, 'new_quote.html')


def errorpage(request):
    return render(request, '404.html')


class AddQuoteCreateView(CreateView):
    template_name = 'new_quote.html'
    form_class = QuoteForm
    queryset = AddQuote.objects.all()
    form = AddQuote.objects.all()
    context = {
        'form': form
    }

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddQuoteCreate2View(CreateView):
    template_name = 'demo_quote.html'
    form_class = QuoteForm
    queryset = AddQuote.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


'''class AddQuoteDetailView(DetailView):
    template_name = 'detail_quote.html'
    queryset = AddQuote.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddQuote, id=id_)'''


class QuoteObjectMixin(object):
    model = AddQuote

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class AddQuoteDetailView(QuoteObjectMixin, View):
    template_name = "detail_quote.html"  # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)


class AddQuoteListView(ListView):
    template_name = 'list_quote.html'
    queryset = AddQuote.objects.all()
    form = AddQuote.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


def pl_details(request):
    return render(request, 'p&l_details.html')


class AddQuoteUpdateView(UpdateView):
    template_name = 'demo_quote.html'
    form_class = QuoteForm
    queryset = AddQuote.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddQuote, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddQuoteDeleteView(DeleteView):
    template_name = 'delete_quote.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddQuote, id=id_)

    def get_success_url(self):
        return reverse('list_quote')


# Production views

class SubscriptionProductCreateView(CreateView):
    template_name = 'production/subscription_extract.html'
    form_class = SubscriptionAddProductForm
    queryset = AddSubscriptionProduct.objects.all()
    form = AddSubscriptionProduct.objects.all()
    context = {
        'form': form
    }

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)



