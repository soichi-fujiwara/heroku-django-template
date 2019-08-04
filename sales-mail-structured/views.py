from django.shortcuts import render
from django.http.response import HttpResponse
from forms import MyForm

def index_template(request):

  if request.method == "POST":
    form = MyForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
    if form.is_valid():  # ← 受け取ったデータの正当性確認
      pass  # ← 正しいデータを受け取った場合の処理
  else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
    #フォーム表示
    form = MyForm()
  
  myapp_data = {
    'app': 'Django',
    'form': form,
  }
  return render(request, 'index.html',myapp_data)