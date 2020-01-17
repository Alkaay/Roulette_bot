bet_type = call.data.split('_')[1]
bet = call.data.split('_')[2]
bet_size_kb = InlineKeyboardMarkup(row_width=4)
buttons_list = []
sizes = (1, 5, 10, 15)

for bet_size in sizes:
    buttons_list.append(InlineKeyboardButton(
        text=f'{bet_size}$', callback_data='bet_' + str(bet_size) + '_' + bet_type + '_' + bet))
bet_size_kb.add(*buttons_list)
bot.send_message(call.message.chat.id, text='Выберите размер ставки:',
                 reply_markup=bet_size_kb)
a = ' '
if a!= '':
    print('asd')
else:
    print('asddeqw')

{'game_short_name': None, 'chat_instance': '9099133411301525339', 'id': '776773420301522318', 'from_user': {'id': 180856655, 'is_bot': False, 'first_name': 'Alex', 'username': 'alkaay', 'last_name': None, 'language_code': 'ru'}, 'message': {'content_type': 'text', 'message_id': 829, 'from_user': <telebot.types.User object at 0x044A7310>, 'date': 1579028149, 'chat': <telebot.types.Chat object at 0x04E3FDD0>, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Выберите тип ставки:', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 829, 'from': {'id': 1042149198, 'is_bot': True, 'first_name': 'Roulette', 'username': 'try_topora_bot'}, 'chat': {'id': 180856655, 'first_name': 'Alex', 'username': 'alkaay', 'type': 'private'}, 'date': 1579028149, 'text': 'Выберите тип ставки:', 'reply_markup': {'inline_keyboard': [[{'text': 'Число', 'callback_data': 'bet type change_1'}, {'text': 'Красн/черн', 'callback_data': 'bet type change_2'}]]}}}, 'data': 'bet type change_2', 'inline_message_id': None}
{'content_type': 'text', 'message_id': 831, 'from_user': {'id': 180856655, 'is_bot': False, 'first_name': 'Alex', 'username': 'alkaay', 'last_name': None, 'language_code': 'ru'}, 'date': 1579028173, 'chat': {'type': 'private', 'last_name': None, 'first_name': 'Alex', 'username': 'alkaay', 'id': 180856655, 'title': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Изменить сумму ставки', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 831, 'from': {'id': 180856655, 'is_bot': False, 'first_name': 'Alex', 'username': 'alkaay', 'language_code': 'ru'}, 'chat': {'id': 180856655, 'first_name': 'Alex', 'username': 'alkaay', 'type': 'private'}, 'date': 1579028173, 'text': 'Изменить сумму ставки'}}
