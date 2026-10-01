from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Start
from aiogram_dialog.widgets.style import Style

from aiogram import F
from aiogram.enums import ButtonStyle
from app.domain.user.enums import UserRole
from app.presentation.aiogram.state import (
    AdminRootState,
    InfoState,
    ProfileState,
    RootState,
    ShoppingState,
    WalletState,
)
from app.presentation.aiogram.widget import GetText

from .getter import root_getter

root: Window = Window(
    GetText("root"),
    Start(
        GetText("root.buy-btn"),
        id="to_product",
        state=ShoppingState.select_category,
        style=Style(ButtonStyle.SUCCESS),
    ),
    Group(
        Start(
            GetText(
                "root.profile-btn",
            ),
            id="to_profile",
            state=ProfileState.profile,
            style=Style(ButtonStyle.DANGER),
        ),
        Start(
            GetText("root.info-btn"),
            id="to_info",
            state=InfoState.info,
            style=Style(ButtonStyle.PRIMARY),
        ),
        width=2,
    ),
    Start(
        GetText("root.wallet-btn"),
        id="to_wallet",
        state=WalletState.wallet,
        style=Style(ButtonStyle.SUCCESS),
    ),
    Start(
        GetText("root.admin-panel-btn"),
        when=F["user_role"] >= UserRole.ADMIN,
        id="to_admin_root",
        state=AdminRootState.root,
        style=Style(ButtonStyle.DANGER),
    ),
    getter=root_getter,
    state=RootState.root,
)
