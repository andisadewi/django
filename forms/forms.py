from django import forms

class FirstForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    sender = forms.EmailField(required=False)

    # here we can define our own clean method
    def clean_subject(self):
    	data = self.cleaned_data['subject']
    	# check something bla
    	return data

class SecondForm(forms.Form):
    CHOICES = [('ONE','Choice 1'), ('TWO','Choice 2'), ('THREE','Choice 3'), ('FOUR','Choice 4'),]
    message = forms.CharField(widget=forms.Textarea, required=False)
    radio_choice = forms.ChoiceField(widget=forms.RadioSelect, 
    	label='this is the question?', 
    	choices=CHOICES, 
    	required=False)
    string_input = forms.CharField(widget=forms.TextInput, required=False)

class ThirdForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=False)
    #choice = forms.ChoiceField(widget=forms.Select, 
    #	label='this is the question?', 
    #	choices=['a', 'b', 'c'], 
    #	required=False)


# forms.Select = drop down, forms.RadioSelect = radio buttons

# required: If True, the field may not be left blank or given a None value. Fields are required by default, so you would set required=False to allow blank values in the form.
# label: The label to use when rendering the field in HTML. If a label is not specified, Django will create one from the field name by capitalizing the first letter and replacing underscores with spaces (e.g. Renewal date).
# label_suffix: By default a colon is displayed after the label (e.g. Renewal date:). This argument allows you to specify a different suffix containing other character(s).
# initial: The initial value for the field when the form is displayed.
# widget: The display widget to use.
# help_text (as seen in the example above): Additional text that can be displayed in forms to explain how to use the field.
# error_messages: A list of error messages for the field. You can override these with your own messages if needed.
# validators: A list of functions that will be called on the field when it is validated.
# localize: Enables the localization of form data input (see link for more information).
# disabled: The field is displayed but its value cannot be edited if this is True. The default is False.