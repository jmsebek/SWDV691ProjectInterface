from django import forms

class ReportForm(forms.Form):
    #report_choice = forms.CharField(label="Select Report:", widget=forms.RadioSelect(choices=(("totalTime", "Total Time"),("progress", "Progress"))), required=True)
    
    report_choice = forms.ChoiceField(choices=(("totalTime", "Total Time"),("progress", "Progress")),widget=forms.RadioSelect(), required=True)
    #report_choice.widget.attrs.update({'class':'form-check-input'})