from products.models import ProductAmount


def check_product_amount(pk) -> bool:
    """
        return True/False whether there is product
        or not
    """
    amount = ProductAmount.objects.values('amount').get(product_id=pk)['amount']
    print(amount)
    if amount > 0:
        return True
    else:
        return False
