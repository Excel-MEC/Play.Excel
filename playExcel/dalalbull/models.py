from __future__ import unicode_literals

from django.db import models

# Create your models here.


from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    image_url = models.URLField()
    def __str__ (self):
    	return self.name

class Portfolio(models.Model):
	user_id = models.CharField(max_length=200,primary_key=True)
	cash_bal = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('100000'))
	net_worth = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'),validators=[MinValueValidator(Decimal('0.00'))])
	margin = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'))
	no_trans = models.DecimalField(max_digits=19, decimal_places=0, default=Decimal('0'))
	def __str__(self):
		return self.user_id
		
	def as_dict(self):
		return {
		'user_id' : self.user_id,
		'cash_bal' : float(self.cash_bal),
		'net_worth' : float(self.net_worth),
		'margin' : float(self.margin),
		'no_trans' : float(self.no_trans),
		}

class Transaction(models.Model):
	user_id=models.CharField(max_length=200)
	symbol=models.CharField(max_length=10)
	buy_ss = models.CharField(max_length=30)
	quantity=models.DecimalField(max_digits=19, decimal_places=0,validators=[MinValueValidator(Decimal('0.00'))])
	value=models.DecimalField(max_digits=19,decimal_places=2)
	time=models.DateTimeField(auto_now_add=True)


	

class Pending(models.Model):
	user_id=models.CharField(max_length=200)
	symbol=models.CharField(max_length=10)
	buy_ss = models.CharField(max_length=30)
	quantity=models.DecimalField(max_digits=19, decimal_places=0,validators=[MinValueValidator(Decimal('0.00'))])
	value=models.DecimalField(max_digits=19,decimal_places=2)
	time=models.DateTimeField(auto_now_add=True)


class History(models.Model):
	user_id=models.CharField(max_length=200)
	time=models.DateTimeField(auto_now_add=True)
	symbol=models.CharField(max_length=10)
	buy_ss=models.CharField(max_length=30)
	quantity=models.DecimalField(max_digits=19, decimal_places=0,validators=[MinValueValidator(Decimal('0.00'))])
	price=models.DecimalField(max_digits=19,decimal_places=2)

	def as_dict(self):
		return {
		'time' : self.time,
		'symbol' : self.symbol,
		'buy_ss' : self.buy_ss,
		'quantity' : float(self.quantity),
		'price' : float(self.price),
		}

class Stock_data(models.Model):
    symbol=models.CharField(max_length=30,primary_key=True)
    current_price=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    high=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    low=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    open_price=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    change=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    change_per=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    trade_Qty=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    trade_Value=models.DecimalField(max_digits=19, decimal_places=2,null=True)

    def __str__(self):
    	return self.symbol

    def as_dict(self):
    	return {
    	'symbol' : self.symbol,
    	'current_price' : float(self.current_price[0]),
    	'high' : float(self.high[0]),
    	'low' : float(self.low[0]),
    	'open_price' : float(self.open_price[0]),
    	'change' : float(self.change[0]),
    	'change_per' : float(self.change_per[0]),
    	'trade_Qty' : float(self.trade_Qty[0]),
    	'trade_Value' : float(self.trade_Value[0]),
    	}

#for graph
class Old_Stock_data(models.Model):
    symbol=models.CharField(max_length=30)
    current_price=models.DecimalField(max_digits=19, decimal_places=2,null=True)
    time=models.DateTimeField(auto_now_add=True)