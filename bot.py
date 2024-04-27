from pyrogram import Client, filters, types, enums, errors
from environs import Env

env = Env()
env.read_env()

app = Client("userbot", api_hash=env.str("API_HASH"), api_id=env.int("API_ID"))

WHITE_LIST = env.list("WHITE_LIST")

CHAT_IDS = env.list("CHAT_IDS")


@app.on_message(filters.private)
async def hello(client: Client, message: types.Message):
    print(message)
    if not message.from_user.is_bot and message.from_user.id not in WHITE_LIST:
        msg = "Iltimos, menga yozish uchun avval quyidagi kanallarga/guruhlarga obuna bo'ling/qo'shiling:\n\n"
        count = 0
        for chat_id in CHAT_IDS:
            chat_id = int(chat_id)
            try:
                chat_member = await client.get_chat_member(chat_id, message.from_user.id)
            except (errors.UserNotParticipant, KeyError):
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
            if message.document:
                msg = ("Assalomu alaykum.\n\n"
                       "\"MAXSUS FIZ-MAT\" o'quv markazi tomonidan tashkil etilgan \"KUN SAVOLI\" viktorinasida"
                       " qatnashayotganingiz uchun minnatdormiz.\n\n[Javobni shu profilga ishlanishi bilan yuboringiz"
                       " kerak bo'ladi.](https://t.me/M_Fiz_Mat)\n\n**Natija har kuni kech soat 20:00 da "
                       "t.me/maxsus_fiz_mat telegram kanalida jonli efirda aniqlanadi.**\n\n[Kanalga obuna bo'lishni "
                       "unutmang!](https://t.me/MAXSUS_FIZ_MAT)")
            await message.reply(
                msg,
                parse_mode=enums.ParseMode.MARKDOWN,
                disable_web_page_preview=True,
            )


app.run()
