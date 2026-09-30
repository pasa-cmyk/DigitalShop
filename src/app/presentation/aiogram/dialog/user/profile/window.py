from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Group, Start

from app.presentation.aiogram.state import OrdersState, ProfileState, ReferralState
from app.presentation.aiogram.widget import GetText

from .getter import profile_getter

profile = Window(
    GetText("user-profile"),
    Group(
        Start(
            GetText("user-profile.orders-btn"),
            id="to_orders",
            state=OrdersState.orders,
        ),
        Start(
            GetText("user-profile.referral-btn"),
            id="to_referral",
            state=ReferralState.referral,
        ),
        width=2,
    ),
    Cancel(GetText("inl-ui.back")),
    state=ProfileState.profile,
    getter=profile_getter,
)
