from rest_framework import viewsets
from .serializers import IncomeCategorySerializer,ExpenseCategorySerializer,IncomeSerializer,ExpenseSerializer
from .models import IncomeCategory, ExpenseCategory, Income, Expense


class IncomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    # def get_serializer_class(self):
    #     if self.action in ['create', 'receive', 'update', 'delete']:
    #         return IncomeCategorySerializer
    #     return MovieDetailSerializer