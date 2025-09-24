from django.contrib import admin
from .models import BookSend

@admin.register(BookSend)
class BookSendAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'ref_no', 'date', 'sender', 'receiver', 'subject', 'created_by')
    search_fields = ('reg_no', 'ref_no', 'sender', 'receiver', 'subject')
    list_filter = ('date',)