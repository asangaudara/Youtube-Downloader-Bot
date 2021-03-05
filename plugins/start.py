from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Group", url="https://t.me/seesan_ticket")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Asanga_Udara")],
          [InlineKeyboardButton(
            "Website", url="https://asangabro.ga")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/My Master And Creater Asanga Udara By Sri Lanka"
    first = f"Hey <b>{message.from_user.first_name}</b>\n/My Master And Creater Asanga Udara By Sri Lankaaaaaa"
    await message.reply_text(welcomed ,first, reply_markup=joinButton)
    raise StopPropagation
