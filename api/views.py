from django.db.models import Sum
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from .forms import PeerUserForm
from .models import PeerUser, RewardHistory
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def new_user_page(request):
    return render(request, "create_new_user.html")


@csrf_exempt
def create_new_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        PeerUser.objects.create(name=name)
        return redirect("get_all_users")


@csrf_exempt
def get_all_users(request):
    table_data = []
    peer_users = PeerUser.objects.all()
    for user in peer_users:
        p5_balance = 100 - (RewardHistory.objects.filter(given_by_id=user.id).aggregate(total_given=Sum('points'))['total_given'] or 0)
        reward_balance = RewardHistory.objects.filter(given_to_id=user.id).aggregate(total_received=Sum('points'))['total_received'] or 0

        user_data = {}
        user_data["user_id"] = user.id
        user_data["user_name"] = user.name
        user_data["p5_balance"] = p5_balance
        user_data["reward_balance"] = reward_balance
        table_data.append(user_data)

    return render(request, "home.html", {"table_data": table_data})


@csrf_exempt
def user_info_page(request, id=None):
    p5_balance = None
    reward_balance = None
    if id:
        user = get_object_or_404(PeerUser, pk=id)
        form = PeerUserForm(instance=user)
        p5_balance = 100 - (RewardHistory.objects.filter(given_by_id=user.id).aggregate(total_given=Sum('points'))[
                                'total_given'] or 0)
        reward_balance = RewardHistory.objects.filter(given_to_id=user.id).aggregate(total_received=Sum('points'))[
                             'total_received'] or 0
    else:
        form = PeerUserForm()

    if request.method == "POST":
        if id:
            form = PeerUserForm(request.POST, instance=user)
        else:
            form = PeerUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("get_all_users")

    return render(request, "user_info.html", {"form": form, "user": user if id else None, "p5_balance": p5_balance, "reward_balance": reward_balance})


def p5_balance_page(request, id=None):
    if id:
        user = get_object_or_404(PeerUser, pk=id)
        p5_balance = 100 - (RewardHistory.objects.filter(given_by_id=user.id).aggregate(total_given=Sum('points'))[
                                'total_given'] or 0)

        p5_given_list = list(RewardHistory.objects.filter(given_by_id=user.id))

        return render(request, "p5_balance_page.html", {"user": user, "p5_balance": p5_balance, "p5_given_list": p5_given_list})


def new_reward_page(request, id=None):
    if id:
        user = get_object_or_404(PeerUser, pk=id)
        users_list = PeerUser.objects.exclude(pk=id)
        p5_balance = 100 - (RewardHistory.objects.filter(given_by_id=user.id).aggregate(total_given=Sum('points'))[
                                'total_given'] or 0)
        return render(request, "create_new_reward.html", {"user": user, "users_list": users_list, "p5_balance": p5_balance})


def create_reward(request, id=None):
    if request.method == "POST" and id:
        recipient_id = request.POST.get('recipient')
        points = float(request.POST.get('points'))

        reward = RewardHistory.objects.create(given_by_id=id, given_to_id=recipient_id, points=points)

        return redirect("p5_balance_page", id=id)


def reward_balance_page(request, id=None):
    if id:
        user = get_object_or_404(PeerUser, pk=id)
        reward_balance = RewardHistory.objects.filter(given_to_id=user.id).aggregate(total_received=Sum('points'))[
                             'total_received'] or 0

        reward_received_list = list(RewardHistory.objects.filter(given_to_id=user.id))

        return render(request, "reward_balance_page.html", {"user": user, "reward_balance": reward_balance, "reward_received_list": reward_received_list})

