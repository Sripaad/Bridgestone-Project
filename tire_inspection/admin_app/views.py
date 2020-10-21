"""Myview"""
from django.shortcuts import render
from admin_app.auto_tire_test import tire_testing
from django.core.files.storage import FileSystemStorage
from django.templatetags.static import static

# Create your views here.
def tire_test_view(request):
	"""
	Home Page Rendering
	"""
	return render(request,"index.html",context={})
def ink_test_view(request):
	"""
	Ink test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_ink_test = test.ink_test(fss.path(name))
		data = {}
		data['result'] = result_of_ink_test
	return render(request,"result.html",context=data)
def twi_test_view(request):
	"""
	TWI test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_twi_test = test.twi_test(fss.path(name),static('images/template_for_TWI.png'))
		data = {}
		data['result'] = result_of_twi_test
	return render(request,"result.html",context=data)
def wobbling_test_view(request):
	"""
	Wobbling test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_wobbling_test = test.wobbling_test(fss.path(name))
		data = {}
		data['result'] = result_of_wobbling_test
	return render(request,"result.html",context=data)
def seperation_test_view(request):
	"""
	Seperations test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_wobbling_test = test.seperation_test(fss.path(name))
		data = {}
		data['result'] = result_of_wobbling_test
	return render(request,"result.html",context=data)