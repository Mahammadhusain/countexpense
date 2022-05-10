from django.contrib import admin
from .models import * 
# Register your models here.


@admin.register(CreditModel)
class CreditModelAdmin(admin.ModelAdmin):
    list_display = ["add_date", "tag", "amt"][::-1]


@admin.register(DebitModel)
class DebitModelAdmin(admin.ModelAdmin):
    list_display = ["add_date", "tag", "amt"][::-1]


@admin.register(BankTransferModel)
class BankTransferModelAdmin(admin.ModelAdmin):
    list_display = ["add_date", "tag", "amt"][::-1]



@admin.register(CreditDebitTransferButtonModel)
class CreditDebitButtonModelAdmin(admin.ModelAdmin):
    list_display = ["btn_type", "tag", "amt"][::-1]
