from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
from .models import BookSend
from .forms import BookSendForm
import csv

@login_required
def booksend_list(request):
    q = request.GET.get('q','').strip()
    items = BookSend.objects.all()
    if q:
        items = items.filter(
            Q(ref_no__icontains=q) |
            Q(sender__icontains=q) |
            Q(receiver__icontains=q) |
            Q(subject__icontains=q) |
            Q(action__icontains=q) |
            Q(remark__icontains=q) |
            Q(reg_no__icontains=q)
        )
    paginator = Paginator(items, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'booksend_list.html', {'page_obj': page_obj, 'q': q})

@login_required
def booksend_create(request):
    if request.method == 'POST':
        form = BookSendForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect('booksend_list')
    else:
        form = BookSendForm()
    return render(request, 'booksend_form.html', {'form': form, 'title': 'เพิ่มรายการ'})

@login_required
def booksend_update(request, pk):
    obj = get_object_or_404(BookSend, pk=pk)
    if request.method == 'POST':
        form = BookSendForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('booksend_list')
    else:
        form = BookSendForm(instance=obj)
    return render(request, 'booksend_form.html', {'form': form, 'title': f'แก้ไขรายการ #{pk}'})

@login_required
def booksend_delete(request, pk):
    obj = get_object_or_404(BookSend, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('booksend_list')
    return render(request, 'booksend_confirm_delete.html', {'obj': obj})

@login_required
def booksend_export_csv(request):
    # ส่งออก CSV ตามคอลัมน์แบบทะเบียน
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="booksend.csv"'
    writer = csv.writer(response)
    writer.writerow(['เลขทะเบียนส่ง','ที่','ลงวันที่','จาก','ถึง','เรื่อง','การปฏิบัติ','หมายเหตุ','ผู้บันทึก','บันทึกเมื่อ'])
    for i in BookSend.objects.all().order_by('reg_no'):
        writer.writerow([i.reg_no, i.ref_no or '', i.date, i.sender, i.receiver, i.subject, i.action or '', i.remark or '', i.created_by.username, i.created_at])
    return response