from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from receipts.models import Receipt, ExpenseCategory, Account

# Create your views here.


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = "receipts/list.html"
    # context_object_name="receipt_list"

    def get_queryset(self):
        return Receipt.objects.filter(purchaser=self.request.user)


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    template_name = "receipts/new.html"
    fields = ["vendor", "total", "tax", "date", "category", "account"]

    def form_valid(self, form):
        new_receipt = form.save(commit=False)
        new_receipt.purchaser = self.request.user
        new_receipt.save()
        return redirect("home")


class ExpenseCategoryListView(LoginRequiredMixin, ListView):
    model = ExpenseCategory
    template_name = "expenses/list.html"
    # context_object_name = "expensecategory_list"

    def get_queryset(self):
        return ExpenseCategory.objects.filter(owner=self.request.user)


class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ExpenseCategory
    template_name = "expenses/new.html"
    fields = ["name"]

    def form_valid(self, form):
        new_category = form.save(commit=False)
        new_category.owner = self.request.user
        new_category.save()
        return redirect("list_categories")


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/list.html"

    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    template_name = "accounts/new.html"
    fields = ["name", "number"]

    def form_valid(self, form):
        new_account = form.save(commit=False)
        new_account.owner = self.request.user
        new_account.save()
        return redirect("list_accounts")
