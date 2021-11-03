from cart.cart import Cart
from order.models import Order, OrderItem


def order_checkout(request, first_name, last_name, email, address, zipcode, place, phone, paid_amount):
    """
    This function is used to check out an order.
    """
    order = Order.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        address=address,
        zipcode=zipcode,
        place=place,
        phone=phone,
        paid_amount=paid_amount,
        total_price=Cart(request).get_total_price()
    )

    for item in Cart(request):
        OrderItem.objects.create(
            order=order, product=item['product'], customer=item['product'].customer, price=item['product'].price, quantity=item['quantity'])

        order.customer.add(item['product'].customer)

    return order
