from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from games.models import Game
from django.core.mail import send_mail
from django.conf import settings


@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    # Додаємо лише якщо гри ще немає в кошику
    CartItem.objects.get_or_create(user=request.user, game=game)

    # Повертаємо на головну сторінку
    return redirect('games:catalog')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.game.price for item in items)

    return render(request, 'cart/cart.html', {
        "items": items,
        "total_price": total_price
    })

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:cart')



@login_required
def confirm_page(request):
    return render(request, "cart/confirm.html")



@login_required
def confirm_order(request):
    if request.method == "POST":

        email = request.user.email  # беремо email з акаунту

        items = CartItem.objects.filter(user=request.user)

        if not items.exists():
            return redirect("cart:cart")

        game_list = "\n".join([f"- {item.game.title}" for item in items])
        total = sum([item.game.price for item in items])

        send_mail(
            subject="Підтвердження покупки",
            message=f"Ви придбали:\n\n{game_list}\n\nСума: {total} грн",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        items.delete()

        return render(request, "cart/success.html", {"email": email})

    return redirect("cart:confirm")
