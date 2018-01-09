from django.shortcuts import render,redirect,HttpResponse

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        print(u,p)
        if u == 'root' and p == '123':
            request.session['is_login'] = True
            request.session['username'] = u
            return redirect('/index/')
        else:
            return render(request,'login.html')

def index(request):
    if request.session.get('is_login',None):
        return render(request,'index.html')
    else:
        return HttpResponse('滚')
def logout(request):
    request.session.clear()
    return redirect('/login/')


from django import forms
class FM(forms.Form):
    # user = forms.CharField(error_messages={'required':'必须填'})
    user = forms.CharField()
    # pwd = forms.CharField(error_messages={'required':'必须填2'})
    email = forms.EmailField()

def fm(request):
    if request.method == 'GET':
        obj = FM()
        return render(request,'fm.html',{'obj':obj})
    elif request.method == 'POST':
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            print(obj.cleaned_data)
        else:
            print(obj.errors)
            return render(request,'fm.html',{'obj':obj})
    return render(request,'fm.html')
