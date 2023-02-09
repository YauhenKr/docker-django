from cart.models import Cart


def create_cart_for_new_user(sender, instance, created, **kwargs):
    if not instance.created:
        Cart.objects.create(user=instance)
        instance.created = True
        instance.save()
