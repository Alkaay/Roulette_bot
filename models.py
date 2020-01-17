from mongoengine import *


class User(Document):
    user_id = IntField()
    name = StringField()
    surname = StringField()
    nickname = StringField()
    count = IntField()

    @classmethod
    def get_or_create_user(cls, message):
        user = cls.objects.filter(user_id=message.from_user.id).first()
        if user:
            return user
        else:
            print("message.from_user.id" ,message.from_user.id)
            print('message.chat.id', message.chat.id)
            return cls(user_id=message.from_user.id,
                       name=message.from_user.first_name,
                       surname=message.from_user.last_name,
                       nickname=message.from_user.username,
                       count=100,).save()

    @classmethod
    def get_user(cls, id):
        return cls.objects.filter(user_id=id).first()

class Text(Document):
    title = StringField(max_length=128)
    type = StringField(max_length=64)
    text = StringField(max_length=4096)
    date = StringField(max_length=36)

class Bet(Document):
    user = ReferenceField(User)
    bet_size = IntField()
    bet_type = StringField(max_length=64)
    bet_numbers = ListField()
    date = StringField(max_length=36)
    result = IntField(default=0) #'0'-wating, '-1'-lose, '1'-win

    @classmethod
    def check_last_bet(cls, id):
        bes = cls.objects.filter(user_id=id)


