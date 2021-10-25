from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import ContactWithUsForm

header_phones = [
    "+375 (17) 111-22-33",
    "+375 (29) 319-01-19",
    "+375 (33) 111-22-33",
]


class AvalonHomeForm(CreateView):
    form_class = ContactWithUsForm
    template_name = 'main/index.html'
    # context_object_name = 'contact_with_us_form'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_phones'] = header_phones
        # context['title'] = 'Главная страница - ООО "Авалон Авто"'
        return context
