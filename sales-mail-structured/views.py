from django.shortcuts import render
from django.http.response import HttpResponse
 
def index_template(request):

  #ƒtƒH[ƒ€ì¬
  form = MyForm()
  
  myapp_data = {
    'app': 'Django',
    'form': form,
  }
  return render(request, 'index.html',myapp_data)