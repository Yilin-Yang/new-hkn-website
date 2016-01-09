from django import forms

from .models import Member, Social, Service_Hours

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		exclude = ['uniqname', 'status']
		widgets = {
			'expected_grad_date': forms.SelectDateWidget(),
		}

	def clean_resume(self):
		resume = self.cleaned_data.get('resume')
		if resume == None or resume == False:
			return resume
		resume_parts = resume.name.split('.')
		extension = resume_parts[-1]
		if extension != 'pdf' and extension != 'PDF':
			raise forms.ValidationError("Resumes must be a PDF document")
		return resume

# Form to submit a comma separated list of new member to create member objects for
class NewMemberForm(forms.Form):
	new_members = forms.CharField()

	def clean_new_members(self):
		new_members = self.cleaned_data.get('new_members')	

		uniqnames = new_members.split(',')
		for name in uniqnames:
			if len(name) < 3 or len(name) > 8:
				raise forms.ValidationError("A Uniqname is either too long or too short")
			if not str(name).isalpha():
				raise forms.ValidationError("A Uniqname has a non alphabetical character in it")
		return new_members

# Form to submit a social model
class SocialForm(forms.ModelForm):
	class Meta:
		model = Social
		exclude = ['electee', 'approved']

# Form to submit a service hours model
class ServiceHoursForm(forms.ModelForm):
	class Meta:
		model = Service_Hours
		exclude = ['electee', 'approved']
