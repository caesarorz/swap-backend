from django.contrib import admin

from .models import TransactionStatus, Transaction

admin.site.register(TransactionStatus)
admin.site.register(Transaction)
