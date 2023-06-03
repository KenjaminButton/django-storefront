@admin.display(ordering='products_count')
def products_count(self, collection):
    # reverse('admin:app_model_page') is the template for below
    url = (
        reverse('admin:store_product_changelist')
        + '?'
        + urlencode({
          'collection__id': str(collection.id)
        })
    )
    return format_html('<a href="{}">{}</a>',
                       url, collection.products_count)


@admin.display(ordering='orders_count')
def orders(self, customer):
    url = (
        reverse('admin:store_order_changelist')
        + '?'
        + urlencode({
            'customer__id': str(customer.id)
        }))
    return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )
