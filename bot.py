from pyrogram import Client, filters, types, enums, errors
from environs import Env

env = Env()
env.read_env()

app = Client("userbot", api_hash=env.str("API_HASH"), api_id=env.int("API_ID"))

WHITE_LIST = env.list("WHITE_LIST")

CHAT_ID = env.int("CHAT_ID")


@app.on_message(filters.private)
async def hello(client: Client, message: types.Message):
    if not message.from_user.is_bot and message.from_user.id not in WHITE_LIST:
        msg = """"MAXSUS FIZ - MAT" o'quv markazi tashabbusi bilan amalga oshirilayotgan "KUN SAVOLI" loyihasiga 

         X U SH    K E L I B S I Z !!!

Javob yo'llash uchun avval quyidagi kanalga obuna bo'lishingiz zarur!

        @maxsus_fiz_mat"""
        try:
            chat_member = await client.get_chat_member(CHAT_ID, message.from_user.id)
        except (errors.UserNotParticipant, KeyError):
            chat_member = None
        if not chat_member or chat_member.status not in [
            enums.ChatMemberStatus.MEMBER,
            enums.ChatMemberStatus.OWNER,
            enums.ChatMemberStatus.ADMINISTRATOR,
        ]:
            await message.forward("me")
            await message.delete()
            if message.document:
                msg = ("Assalomu alaykum.\n\n"
                       "\"MAXSUS FIZ-MAT\" o'quv markazi tomonidan tashkil etilgan \"KUN SAVOLI\" viktorinasida"
                       " qatnashayotganingiz uchun minnatdormiz.\n\n[Javobni shu profilga ishlanishi bilan yuboringiz"
                       " kerak bo'ladi.](https://t.me/M_Fiz_Mat)\n\n**Natija har kuni kech soat 20:00 da "
                       "t.me/maxsus_fiz_mat telegram kanalida jonli efirda aniqlanadi.**\n\n[Kanalga obuna bo'lishni "
                       "unutmang!](https://t.me/MAXSUS_FIZ_MAT)")
        else:
            msg = """"KUN SAVOLI" loyihasida har kuni yangi savollar joylanadi. Har kuni kech soat 20:00 da @maxsus_fiz_mat kanalida jonli efir bo'ladi. 

**Albatta qatnashing!** 

To'g'ri javob yo'llaganlar o'rtasida "RANDOM" dasturi yordamida OMADLI ISHTIROKCHI aniqlanadi va pul mukofoti taqdim etiladi.

Omadli ishtirokchi SIZ bo'lishingiz mumkin!

Bizni kuzatishda davom eting. Bundan ham yaxshi loyihalarimiz hali oldinda!"""
        await message.reply(
            msg,
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )


app.run()
