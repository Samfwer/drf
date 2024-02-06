from django.contrib import admin

from .models import IncomeCategory, ExpenseCategory, Income, Expense

@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['category', 'amount', 'date', 'description']
    list_filter = ['category', 'date']
    search_fields = ['category__name', 'description']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'amount', 'date', 'description']
    list_filter = ['category', 'date']
    search_fields = ['category__name', 'description']
