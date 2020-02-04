from django.shortcuts import render,HttpResponse

class IndexController():
    def index(request):
        #return HttpResponse('<h1>Miguel Villalba</h1>%s' % year)
        return render(request,'views/index/index.html')