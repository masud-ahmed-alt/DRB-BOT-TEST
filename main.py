import telegram.ext

Token = "6126659784:AAHA5Ex1VUtK93crcr9ig7KI_J7l2-AgwDE"

updater = telegram.ext.Updater("6126659784:AAHA5Ex1VUtK93crcr9ig7KI_J7l2-AgwDE",use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Welcome to DRB! type /menu")


def menu(update, context):
    update.message.reply_text(

                """
                /start-> Welcome to DRB
                /content->All Brochers
                /sales->Sales info
                /finance-> Available Finance 
                /offers-> Offers

                """
    )

def content(update, context):
    update.message.reply_text("""
    /brocher->All Brochers
    /scheme->All Schemes
    /exchange-> Exchange Benfits

    /menu-> Menu
    """)

def sales(update, context):
    update.message.reply_text("""
    LCV Sales contacts

    i. Banajit Kalita(TL)
        M- +918723926533

    ii. Rakib Rahman(TL)
        M- +918638081684

    iii. Satyajeet Kakoti
        M- +919287958348

    iv. Aditi Das (CRM DBM)
        M- +918404007706
    
    Please Contact!


    /menu-> Menu
    """)


def finance(update, context):
    update.message.reply_text(
        """
        Financer Contacts:

        1. Kotak Mahindra : +919864633020


        /menu-> Menu
        """
    )


# All offers content --start

def offers(update, context):
    update.message.reply_text("""
    Our All Offers
    /menu-> Menu
    """)

    
    file = update.message.photo[0].file_id
    obj = context.bot.get_file(file)
    obj.download()
    

# All offers content --start


# All vehicle brochurs details --start
def brocher(update, context):
    update.message.reply_text("""
    Dost Lite
    Payload : 1250 Kg
    Dimenstions: 8.2ft x 5.4ft 1.2 ft
       """)
    
    
    update.message.reply_text("""
    Dost Strong
    Payload : 1350 Kg
    Dimenstions: 8.2ft x 5.4ft 1.3 ft
    """)
    
    update.message.reply_text("""
    Dost Plus
    Payload : 1500 Kg
    Dimenstions: 8.8ft x 5.4ft 1.3 ft  
    """)
    
    update.message.reply_text("""
    Bada Dost I2
    Payload : 1425 Kg 
    Dimenstions: 9ft x 5.9ft 1.5ft 
    """)

    update.message.reply_text("""
    Bada Dost I4
    Payload : 1825 Kg
    Dimenstions: 9.8ft x 5.9ft 1.7ft 
    """)

    update.message.reply_text("""
    Partner 4Tyre 10 ft
    Payload : 3765 Kg 
    """)
    update.message.reply_text("""
    Partner 4Tyre 14 ft
    Payload : 4565 Kg 

    /menu-> Menu
    """)

    

    # All vehicle brochurs details --end




    # All vehicle schemes details --start
def scheme(update, context):
    update.message.reply_text("""
    i. All commercial vehicle exchage benefits 75%.
    ii. Customer scheme upto 9 lakhs funding.
    iii. OE warranty upto 5 Years.
    /menu-> Menu
    """)
    # All vehicle schemes details --end


        # All vehicle exchange details --start
def exchange(update, context):
    update.message.reply_text("""
    Exchange on every old vehicle benefits upto Rs. 70000.00/-
    /menu-> Menu
    """)
    # All vehicle exchange details --end
    



dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('menu',menu))
dispatcher.add_handler(telegram.ext.CommandHandler('content',content))
dispatcher.add_handler(telegram.ext.CommandHandler('sales',sales))
dispatcher.add_handler(telegram.ext.CommandHandler('brocher',brocher))
dispatcher.add_handler(telegram.ext.CommandHandler('scheme',scheme))
dispatcher.add_handler(telegram.ext.CommandHandler('exchange',exchange))
dispatcher.add_handler(telegram.ext.CommandHandler('finance',finance))
dispatcher.add_handler(telegram.ext.CommandHandler('offers',offers))




updater.start_polling()
updater.idle()