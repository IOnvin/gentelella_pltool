from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, View
from main.forms import QuoteForm, SubscriptionAddProductForm, Test1Form, Test2Form, PerpetualAddProductForm, SchedulePerpetualForm
from main.models import AddQuote, AddSubscriptionProduct, TestModel1, TestModel2, AddPerpetualModel, SchedulePerpetualModel
from django.db.models import Sum


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


class AddQuoteCreateView(CreateView):  # Create View 1
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


class AddQuoteCreate2View(CreateView):  # Create View 2
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


class AddQuoteDetailView(QuoteObjectMixin, View):  # Detail View
    template_name = "detail_quote.html"  # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)


class AddQuoteListView(ListView):  # List View
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


class AddQuoteUpdateView(UpdateView):  # Update View
    template_name = 'demo_quote.html'
    form_class = QuoteForm
    queryset = AddQuote.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddQuote, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddQuoteDeleteView(DeleteView):  # Delete View
    template_name = 'delete_quote.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddQuote, id=id_)

    def get_success_url(self):
        return reverse('list_quote')


# Production views

class SubscriptionProductCreateView(CreateView):  # Products
    template_name = 'production/subscription_extract.html'
    form_class = SubscriptionAddProductForm
    queryset = AddSubscriptionProduct.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class SubscriptionSW(ListView):  # Calculation View
    template_name = 'production/subscription_calc.html'
    queryset = AddSubscriptionProduct.objects.all()
    form = AddSubscriptionProduct.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


class AddProductListView(ListView):  # List View
    template_name = 'production/list_prod.html'
    queryset = AddSubscriptionProduct.objects.all()
    form = AddSubscriptionProduct.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


class AddProductUpdateView(UpdateView):  # Update View
    template_name = 'production/subscription_extract.html'
    form_class = SubscriptionAddProductForm
    queryset = AddSubscriptionProduct.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddSubscriptionProduct, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddProductDeleteView(DeleteView):  # Delete View
    template_name = 'production/sub_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddSubscriptionProduct, id=id_)

    def get_success_url(self):
        return reverse('sub_list')


# Test Models


class Mod1View(View):  # Create Test Model 1
    template_name = 'test_models/mod1view.html'

    def get(self, request, *args, **kwargs):
        test1Form = Test1Form(request.POST or None)
        test2Form = Test2Form(request.POST or None)

        if request.method == 'POST':
            form = Test1Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

        '''val1 = int(request.POST.get('mod1Num1', False))
        val2 = int(request.POST.get('mod2Num1', False))
        res = val1 + val2'''
        context = {
            'form': test1Form,
            'form2': test2Form,
        }
        return render(request, self.template_name, context)


def Mod2View(request):
    return render(request, 'test_models/mod2view.html')


# Schedule Products

def list_and_create(request):                                   # Schedule Products
    form = SchedulePerpetualForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    # notice this comes after saving the form to pick up new objects
    objects = SchedulePerpetualModel.objects.all()
    return render(request, 'products/schedule_perp.html', {'objects': objects, 'form': form})


# Products

class PerpetualProductCreateView(CreateView):  # Products
    template_name = 'products/add_perpetual.html'
    form_class = PerpetualAddProductForm
    queryset = AddPerpetualModel.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PerpetualProductListView(ListView):  # List View
    template_name = 'products/list_perpetual.html'
    queryset = AddPerpetualModel.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


class PerpetualProductUpdateView(UpdateView):  # Update View
    template_name = 'products/add_perpetual.html'
    form_class = PerpetualAddProductForm
    queryset = AddPerpetualModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddPerpetualModel, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('perpetual_list')


class PerpetualProductDeleteView(DeleteView):   # Delete View
    template_name = 'products/delete_perpetual.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(AddPerpetualModel, id=id_)


class PerpetualSW(ListView):        # Detail View 7. Perpetual sw
    template_name = 'products/sw_perpetual.html'
    queryset = AddPerpetualModel.objects.all()
    total_volDiscPrice_p = AddPerpetualModel.objects.aggregate(Sum('volDiscPrice_p'))['volDiscPrice_p__sum'] or 0.00

    '''def get_total(self):
        total = 0
        for instance in AddPerpetualModel.volDiscPrice_p.all():
            total += instance
        return total'''

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form_perp': self.queryset}

        return render(request, self.template_name, context)