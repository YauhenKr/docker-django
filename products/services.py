def get_sales_percent(product) -> int:
    """
        calculate summary percent of sales for
        current product
    """
    return sum([sale.percent for sale in product.sales.all()])


def calculate_price_with_sales(product) -> float:
    """
        calculate price with sales for
        current product
    """
    sales_percent = get_sales_percent(product=product)
    return float(product.price) - (float(product.price) * (0.01 * sales_percent))
