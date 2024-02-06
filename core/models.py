from django.db import models

class IncomeCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория дохода'
        verbose_name_plural = 'Категория доходов'
    

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории расхода')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория расхода'
        verbose_name_plural = 'Категории для расхода'


class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, verbose_name='Категория дохода')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма дохода')
    date = models.DateField(verbose_name='Дата получения дохода')
    description = models.TextField(blank=True, null=True, verbose_name='Описание дохода')

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"
    
    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, verbose_name='Категория расхода')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма расхода')
    date = models.DateField(verbose_name='Дата расхода')
    description = models.TextField(blank=True, null=True, verbose_name='Описание расхода')

    def __str__(self):
        return f"{self.category} - {self.amount} ({self.date})"
    
    class Meta:
        verbose_name = 'Разход'
        verbose_name_plural = 'Расходы'
    
