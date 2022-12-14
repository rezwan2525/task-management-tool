from django.urls import path, include
from .views import AddNewBoardMember, AllCardItemOrderUpdate, BoardAllShow, BoardCreate, BoardMembersAll, BoardShow, CardCommentAll, CardCommentCreate, ListItemCreate, ListItemShow, ListItemAll, ListItemOrderUpdate, CardItemCreate, CardItemShow, CardItemAll, CardItemOrderUpdate, UserShow, SharedBoardAll

urlpatterns = [
    path('currentuser/', UserShow.as_view()),

    path('createboard/', BoardCreate.as_view()),
    path('board/<int:pk>/', BoardShow.as_view()),
    path('boards/', BoardAllShow.as_view()),
    path('sharedboards/', SharedBoardAll.as_view()),

    path('createlist/', ListItemCreate.as_view()),
    path('board/<int:board_id>/lists/', ListItemAll.as_view()),
    path('lists/<int:pk>/', ListItemShow.as_view()),
    path('updatelistorder/<int:pk>/', ListItemOrderUpdate.as_view()),

    path('createcard/', CardItemCreate.as_view()),
    path('list/<int:list_id>/cards/', CardItemAll.as_view()),
    path('cards/<int:pk>/', CardItemShow.as_view()),
    path('updatecardorder/<int:pk>/', CardItemOrderUpdate.as_view()),

    path('inccardorder/<int:list_id>/', AllCardItemOrderUpdate.as_view()),

    path('addcomment/', CardCommentCreate.as_view()),
    path('comments/<int:card_id>/', CardCommentAll.as_view()),


    path('addmember/', AddNewBoardMember.as_view()),
    path('members/<int:board_id>/', BoardMembersAll.as_view()),
]
