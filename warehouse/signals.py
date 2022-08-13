from django.dispatch import receiver
from django.db.models.signals import post_save
from warehouse.models import Order
import requests


@receiver(post_save, sender=Order)
def order_api_request(sender, instance, **kwargs):
	order = {
		'slug': instance.slug,
		'status': instance.status_id,
		'warehouse': instance.warehouse
	}
	requests.put(f'http://127.0.0.1:8000/api/v1/order/{instance.slug}/', json=order)
