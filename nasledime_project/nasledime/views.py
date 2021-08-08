from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, \
    DetailView, UpdateView, DeleteView

from nasledime_project.nasledime.models import Will


class IndexView(TemplateView):
    template_name = 'index.html'


class HowWillsWorkView(TemplateView):
    template_name = 'nasledime/how-wills-work.html'


class CreateWill(LoginRequiredMixin, CreateView):
    model = Will
    fields = ('first_name', 'last_name', 'uic', 'address', 'text')
    success_url = reverse_lazy('wills list')
    login_url = '/profile/login/'
    template_name = 'nasledime/create-will.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CreateWill, self).get_form(form_class)
        '''
        Adds placeholder text, modifies the fields' scale.
        '''
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'Име на завещателя'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Фамилно име'})
        form.fields['uic'].widget = forms.TextInput(attrs={'placeholder': 'ЕГН на завещателя'})
        form.fields['address'].widget = forms.TextInput(attrs={'placeholder': 'Адрес на завещателя'})
        form.fields['text'].widget = forms.Textarea(attrs={'cols': 50, 'rows': 10,
                                                           'placeholder': 'Текстът на завещанието.\n'
                                                                           'Напр.:\nЗавещавам цялото си имущество на '
                                                                           'своя син Ангел;\nили\n'
                                                                           'Завещавам апартамента, находящ се на адрес: '
                                                                           '(...) на дъщеря си Ивана и лекия си автомобил'
                                                                           '(...) с номер (...) на своя внук Петър.'})
        return form

    def form_valid(self, form):
        will = form.save(commit=False)
        will.user = self.request.user
        will.save()
        return super().form_valid(form)

    # def add_prefix(self, field_name):
    #     # look up field name; return original if not found
    #     field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
    #     return super(CreateWill, self).get_form_class().add_prefix(field_name)


class EditWillView(LoginRequiredMixin, UpdateView):
    model = Will
    fields = ('first_name', 'last_name', 'uic', 'address', 'text')
    template_name = 'nasledime/update-will.html'
    success_url = reverse_lazy('wills list')
    login_url = '/profile/login/'


class DeleteWillView(LoginRequiredMixin, DeleteView):
    model = Will
    template_name = 'nasledime/delete-will.html'
    success_url = reverse_lazy('wills list')
    login_url = '/profile/login/'


class ListAllWillsView(LoginRequiredMixin, ListView):
    template_name = 'nasledime/wills_list.html'
    context_object_name = 'wills'
    model = Will
    paginate_by = 3

    # def get_context_data(self, **kwargs):
    #     context = super(ListAllWillsView, self).get_context_data(**kwargs)
    #     context['wills'] = Will.objects.filter(user_id=self.request.user.id)
    #     return context

    '''
    Returns a queryset of all Will objects that belong to current user.
    To be preferred instead of get_context_data, as the latter returns
    a context object which requires more manual input and can mess up 
    things like pagination.
    '''
    def get_queryset(self):
        return Will.objects.filter(user_id=self.request.user.id)


class WillDetailView(LoginRequiredMixin, DetailView):
    template_name = 'nasledime/will-details.html'
    context_object_name = 'will'
    model = Will

