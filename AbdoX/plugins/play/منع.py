from pyrogram import Client
from pyrogram import filters
from AbdoX import app

@app.on_message(filters.text)
async def delete_text(client, message):
    word_list = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
    if message.text in word_list:
        await client.delete_messages(message.chat.id, message.id)
        await client.send_message(message.chat.id, f"عذار ممنوع السب هنا {message.from_user.first_name}")
