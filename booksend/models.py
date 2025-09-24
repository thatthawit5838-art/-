from django.db import models
from django.contrib.auth.models import User

class BookSend(models.Model):
    # เลขทะเบียนส่ง (AutoField เริ่มจาก 1 และเพิ่มอัตโนมัติ)
    reg_no = models.AutoField(primary_key=True, verbose_name='เลขทะเบียนส่ง')
    ref_no = models.CharField('ที่', max_length=50, blank=True, null=True)
    date = models.DateField('ลงวันที่')
    sender = models.CharField('จาก', max_length=200)
    receiver = models.CharField('ถึง', max_length=200)
    subject = models.CharField('เรื่อง', max_length=300)
    action = models.CharField('การปฏิบัติ', max_length=200, blank=True, null=True)
    remark = models.TextField('หมายเหตุ', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ผู้บันทึก')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-reg_no']
        verbose_name = 'ทะเบียนหนังสือส่ง'
        verbose_name_plural = 'ทะเบียนหนังสือส่ง'

    def __str__(self):
        return f"{self.reg_no} - {self.subject}"