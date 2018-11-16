from django.shortcuts import render
from formtools.wizard.views import NamedUrlSessionWizardView

class FormWizard(NamedUrlSessionWizardView):
    template_name = 'forms/form_step.html'

    def done(self, form_list, **kwargs):
        form_data = process_forms(form_list)
        return render(self.request, 'forms/done.html',
            {'form_data': form_data})

def process_forms(form_list):
	form_data = [form.cleaned_data for form in form_list]
	return form_data

# Create your views here.
def index(request):
    return render(request, 'forms/index.html', {})