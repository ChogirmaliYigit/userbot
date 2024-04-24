from pyrogram import Client, filters, types, enums, errors
from environs import Env

env = Env()
env.read_env()

app = Client("userbot", api_hash=env.str("API_HASH"), api_id=env.int("API_ID"))

WHITE_LIST = env.list("WHITE_LIST")

CHAT_IDS = env.list("CHAT_IDS")


@app.on_message(filters.private)
async def hello(client: Client, message: types.Message):
    if not message.from_user.is_bot and message.from_user.id not in WHITE_LIST:
        msg = "Iltimos, menga yozish uchun avval quyidagi kanallarga/guruhlarga obuna bo'ling/qo'shiling:\n\n"
        count = 0
        for chat_id in CHAT_IDS:
            try:
                chat_member = await client.get_chat_member(chat_id, message.from_user.id)
            except errors.UserNotParticipant:
                chat_member = None
            if not chat_member or chat_member.status not in [
                enums.ChatMemberStatus.MEMBER,
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ]:
                chat = await client.get_chat(chat_id)
                count += 1
                msg += f"[{count}. {chat.title}]({chat.invite_link})\n"
        if count > 0:
            await message.forward("me")
            await message.delete()
            await message.reply(
                msg,
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )


app.run()
