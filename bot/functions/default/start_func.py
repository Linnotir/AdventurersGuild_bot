from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from datetime import datetime, timedelta
import re

from bin.config import CW_chat_id

from bot.content.texts.start_text import start_menu_text, start_welcome_text, alpha_text, start_welcome2_text
from bot.keyboards.reply_keyboard import start_menu
from bot.states.default_states import start_states
from bot.content.parse.default_parse import hero_parse


async def start_func(mes: Message):
    if mes.chat.type != 'private':
        return

    if mes.db.check('SELECT * FROM users WHERE id = ?', [mes.from_user.id]):
        await mes.answer(start_menu_text, start_menu)
    else:
        await mes.answer(alpha_text)
        await mes.answer(start_welcome_text)
        await start_states.Q1.set()


async def start_q1_func(mes: Message, state: FSMContext):
    if mes.forward_from is None or mes.forward_from.id != CW_chat_id or "🎉Достижения: /ach" not in mes.text:
        await mes.answer('Требуется переслать /hero из @ChatWarsBot!')
        return
    if not datetime.now() - mes.forward_date < timedelta(seconds=30):
        await mes.answer('Этому /hero больше 30 секунд. Пришли новый!')
        return

    await hero_input(mes)
    await mes.answer(start_welcome2_text)
    await mes.answer(start_menu_text, start_menu)
    await state.finish()


async def hero_input(mes: Message):
    parse = re.search(hero_parse, mes.text)
    if mes.db.check('SELECT * FROM users WHERE id = ?', [mes.from_user.id]):
        mes.db.query('update users set guild_tag = ?, nickname = ?, lvl = ?, class = ?',
                     [parse.group('guild_tag'), parse.group('nickname'), int(parse.group('lvl')), parse.group('class')])
    else:
        mes.db.query('insert into users (id, guild_tag, nickname, lvl, class)',
                     [mes.from_user.id, parse.group('guild_tag'), parse.group('nickname'), int(parse.group('lvl')),
                      parse.group('class')])