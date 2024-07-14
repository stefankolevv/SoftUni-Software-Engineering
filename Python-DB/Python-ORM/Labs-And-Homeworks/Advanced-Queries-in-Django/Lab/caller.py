import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Order
from django.db.models import Sum, Q, F


# Create and run queries
def product_quantity_ordered():
    result = []
    orders = Product.objects.annotate(
        total=Sum('orderproduct__quantity')
    ).values('name', 'total').order_by('-total')

    for order in orders:
        result.append(f"Quantity ordered of {order['name']}: {order['total']}")
    return '\n'.join(result)

def ordered_products_per_customer():
    result = []
    orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')

    for order in orders:
        result.append(f'Order ID: {order.id}, Customer: {order.customer.username}')

        for ordered_product in order.orderproduct_set.all():
            result.append(f'- Product: {ordered_product.product.name}, Category: {ordered_product.product.category.name}')

    return '\n'.join(result)

def filter_products():
    products = Product.objects.filter(Q(is_available=True) & Q(price__gt=3.00)).order_by(
        '-price',
        'name'
    )

    result = []
    for p in products:
        result.append(f'{p.name}: {p.price}lv.')

    return '\n'.join(result)

def give_discount():
    query = Q(is_available=True) & Q(price__gt=3.00)
    product_to_be_discounted = Product.objects.filter(query).order_by('-price', 'name')
    product_to_be_discounted.update(price=F('price') * 0.7)
    available_products = Product.objects.filter(is_available=True).order_by('-price', 'name')
    result = []
    for p in available_products:
        result.append(f'{p.name}: {p.price}lv.')

    return '\n'.join(result)

# Run and print your queries