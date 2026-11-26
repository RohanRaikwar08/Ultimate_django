from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Online_Shopping
from ..service.online_shopping_service import Online_ShoppingService
from ..utility.data_validator import DataValidator


class Online_ShoppingCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['product_id'] = request.POST.get('product_id')
        self.form['name'] = request.POST.get('name')
        self.form['price'] = request.POST.get('price')
        self.form['category'] = request.POST.get('category')
        self.form['stock'] = request.POST.get('stock')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.product_id = self.form['product_id']
        obj.name = self.form['name']
        obj.price = self.form['price']
        obj.category = self.form['category']
        obj.stock = self.form['stock']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['product_id'] = obj.product_id
        self.form['name'] = obj.name
        self.form['price'] = obj.price
        self.form['category'] = obj.category
        self.form['stock'] = obj.stock

    def input_validation(self, request):
        input_error = self.form['input_error']
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("product_id", ''))):
            input_error['product_id'] = 'Product_Id is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Shopping Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("price", ''))):
            input_error['price'] = 'Price is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("category", ''))):
            input_error['category'] = 'Category is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("stock", ''))):
            input_error['stock'] = 'Stock is required'
            input_error['error'] = True
        return input_error['error']

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):

        try:
            online_shopping = self.form_to_model(Online_Shopping())
            self.get_service().save(online_shopping)
            if self.form['id'] > 0:
                self.form['message'] = 'Shopping List Updated Successfully...!!!'
                self.form['error'] = False
            else:
                self.form['message'] = 'Shopping List Added Successfully...!!!'
                self.form['error'] = False
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return Online_ShoppingService()

    def get_template(self):
        return 'online_shopping.html'
