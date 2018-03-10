from django import forms




class AddForm(forms.Form):


	title = forms.CharField(max_length=200)
	desc = forms.CharField(max_length=400)
	location = forms.CharField(max_length = 100)
	pic = forms.ImageField()

	# date_published = forms.DateTimeField(auto_now_add = True)
	# date_modified = forms.DateTimeField(auto_now = True)