from rest_framework import serializers
from .models import Board, BoardPermission, CardComment, ListItem, CardItem, User

class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'listitem', 'name', 'desc', 'order', 'created_at')
        model = CardItem

    def create(self, validated_data):
        listId = validated_data['listitem']
        cardObj = CardItem.objects.create(**validated_data)
        top = CardItem.objects.filter(listitem=listId).order_by('-order')
        if len(top) > 0:
            topOrder = getattr(top[0], 'order')
            cardObj.order = (topOrder if topOrder is not None else 0) + 4096
            cardObj.save()
        return cardObj

class ListItemSerializer(serializers.ModelSerializer):
    carditems = CardItemSerializer(many=True, read_only=True,)
    class Meta:
        fields = ('id', 'board', 'name', 'order', 'created_at', 'carditems')
        model = ListItem

    def create(self, validated_data):
        boardId = validated_data['board']
        listObj = ListItem.objects.create(**validated_data)
        top = ListItem.objects.filter(board=boardId).order_by('-order')
        if len(top) > 0:
            topOrder = getattr(top[0], 'order')
            listObj.order = (topOrder if topOrder is not None else 0) + 4096
            listObj.save()
        return listObj


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    listitems = ListItemSerializer(many=True)
    class Meta:
        fields = ('id', 'owner', 'name', 'created_at', 'listitems', 'bg')
        model = Board
    
    def create(self, validated_data):
        validated_data.pop('listitems')
        boardObj = Board.objects.create(**validated_data)
        return boardObj

class BoardSummarySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 'owner', 'name', 'created_at', 'updated_at', 'bg')
        model = Board

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 'username', 'email' )
        model = User

class CardCommentSerializer(serializers.ModelSerializer):
    commenter_name = serializers.CharField(source='commenter.username', read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 'comment', 'commenter', 'commenter_name', 'created_at', 'carditem')
        model = CardComment

class BoardMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='member.user.username', read_only=True)
    email = serializers.CharField(source='member.user.email', read_only=True)
    profile_image = serializers.CharField(source='member.profile_image', read_only=True)
    class Meta:
        fields = ('id', 'username', 'profile_image', 'email')
        model = BoardPermission



    
class BoardMemberPerformSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='member.user.username', read_only=True)
    email = serializers.CharField(source='member.user.email', read_only=True)
    profile_image = serializers.CharField(source='member.profile_image', read_only=True)
    class Meta:
        fields = ('id', 'username', 'profile_image', 'email')
        model = BoardPermission
