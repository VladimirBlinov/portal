from django.shortcuts import render

# menu = ['Mortgage calculator', 'Stocks price prediction', 'Stocks price patterns']
menu = [{'title': 'Mortgage calculator', 'url_name': 'mortgage'},
        {'title': 'Stocks price prediction', 'url_name': 'stock_price_prediction'},
        {'title': 'Stocks price patterns', 'url_name': 'stock_price_patterns'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'InvPortal Homepage'
    }
    return render(request, "main/index.html", context=context)

