from re import M
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from .models import Hocphan, Taikhoan, Tudien
from .forms import RegistrationForm, DangNhapForm, ThemHocPhanForm, ThemTuDienForm
from django.contrib.sessions.backends.db import SessionStore
s = SessionStore()
# Create your views here.
def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        try:
            taikhoan = Taikhoan.objects.get(username = username)
            return render(request,'pages/register.html',{'form':form,'thongbao':'thongbao'})
        except Taikhoan.DoesNotExist:
            form.save()
            return redirect('../dangnhap')
    return render(request,'pages/register.html',{'form':form})
def gethome(request):
    form = DangNhapForm(request.POST or None)
    if('taikhoan' not in s):
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                taikhoan = Taikhoan.objects.get(username = username,password=password)
                s['taikhoan']=taikhoan
                return render(request,'pages/home.html',{'taikhoan':taikhoan})
            except Taikhoan.DoesNotExist:
                return redirect('dangnhap')
        return render(request,'pages/home.html')
    else:
        taikhoan = s['taikhoan']
        return render(request, 'pages/home.html',{'taikhoan':s['taikhoan']})
def dangnhap(request):
    form = DangNhapForm(request.POST or None)
    if('taikhoan' not in s):
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                taikhoan = Taikhoan.objects.get(username = username,password=password)
                s['taikhoan']=taikhoan
                return render(request,'pages/home.html',{'taikhoan':taikhoan})
            except Taikhoan.DoesNotExist:
                return render(request,'pages/dangnhap.html',{'form':form,'thongbao':'thongbao'})
    else:
        taikhoan = s['taikhoan']
        return render(request, 'pages/home.html',{'taikhoan':s['taikhoan']})
    return render(request,'pages/dangnhap.html',{'form':form})
def dangxuat(request):
    del s['taikhoan']
    return redirect('../dangnhap')
def themhocphan(request):
    if('taikhoan' in s):
        taikhoan = s['taikhoan']
        initial_value = {
                'taikhoan': taikhoan
                }
        form = ThemHocPhanForm(request.POST or None,initial=initial_value)
        if form.is_valid():
            tenhocphan = form.cleaned_data['tenhocphan']
            try:
                Hocphan.objects.get(tenhocphan = tenhocphan)
                return render(request,'pages/themhocphan.html',{'form':form,'thongbao':'hocphandatontai'})
            except Taikhoan.DoesNotExist:
                form.save()
                return redirect('xemdanhsachhocphan')
        return render(request,'pages/themhocphan.html',{'form':form})
    return redirect('dangnhap')
def xemdanhsachhocphan(request):
    if('taikhoan' in s):
        searchtenhocphan = request.GET.get('search')
        if searchtenhocphan:
            taikhoan = s['taikhoan']
            hocphans = Hocphan.objects.filter(tenhocphan=searchtenhocphan)
            return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
        else:
            taikhoan = s['taikhoan']
            hocphans = Hocphan.objects.filter(taikhoan = taikhoan)
            return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
    return redirect('dangnhap')
def timkiemhocphan(request):
    if('taikhoan' in s):
        searchtenhocphan = request.GET.get('search')
        if searchtenhocphan:
            hocphans = Hocphan.objects.filter(tenhocphan=searchtenhocphan)
            return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
        else:
            taikhoan = s['taikhoan']
            hocphans = Hocphan.objects.filter(taikhoan = taikhoan)
            return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
    return redirect('dangnhap')
def chitiet(request,tenhocphan):
    hocphan = Hocphan.objects.filter(tenhocphan = tenhocphan)
    tudiens = Tudien.objects.filter(hocphan = hocphan[0])
    return render(request, 'pages/chitiet.html',{'taikhoan':s['taikhoan'],'tudiens':tudiens,'hocphan':hocphan[0]})
def suahocphan(request,tenhocphan):
    hocphan = get_object_or_404(Hocphan, tenhocphan=tenhocphan)
    form = ThemHocPhanForm(request.POST or None,instance=hocphan)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            taikhoan = s['taikhoan']
            hocphans = Hocphan.objects.filter(taikhoan = taikhoan)
            return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
    context = {'form': form}
    return render(request, 'pages/suahocphan.html',context)
def xoahocphan(request,tenhocphan):
    hocphan = get_object_or_404(Hocphan, tenhocphan=tenhocphan)
    if request.method == 'POST':
        hocphan.delete()
        taikhoan = s['taikhoan']
        hocphans = Hocphan.objects.filter(taikhoan = taikhoan)
        return render(request,'pages/xemdanhsachhocphan.html',{'taikhoan':taikhoan,'hocphans':hocphans})
    context = {'hocphan': hocphan}
    return render(request, 'pages/xoahocphan.html', context)
def themtudien(request,tenhocphan):
    hocphan = Hocphan.objects.filter(tenhocphan = tenhocphan)
    initial_value = {
                'hocphan': hocphan[0]
                }
    form = ThemTuDienForm(request.POST or None,initial=initial_value)
    if form.is_valid():
        form.save()
        hocphan = Hocphan.objects.filter(tenhocphan = tenhocphan)
        tudiens = Tudien.objects.filter(hocphan = hocphan[0])
        return render(request, 'pages/chitiet.html',{'taikhoan':s['taikhoan'],'tudiens':tudiens,'hocphan':hocphan[0]})
    return render(request,'pages/themtudien.html',{'form':form})
def xoatudien(request,id):
    tudien = get_object_or_404(Tudien, id=id)
    if request.method == 'POST':
        hocphan = tudien.hocphan
        tudiens = Tudien.objects.filter(hocphan = hocphan)
        tudien.delete()
        return render(request, 'pages/chitiet.html',{'taikhoan':s['taikhoan'],'tudiens':tudiens,'hocphan':hocphan})
    context = {'tudien': tudien}
    return render(request, 'pages/xoatudien.html', context)

def suatudien(request,id):
    tudien = get_object_or_404(Tudien, id=id)
    form = ThemTuDienForm(request.POST or None,instance=tudien)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            hocphan = tudien.hocphan
            tudiens = Tudien.objects.filter(hocphan = hocphan)
            return render(request, 'pages/chitiet.html',{'taikhoan':s['taikhoan'],'tudiens':tudiens,'hocphan':hocphan})
    context = {'form': form}
    return render(request, 'pages/suatudien.html',context)