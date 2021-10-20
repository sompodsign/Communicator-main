from pathlib import Path
import os

# User file

user_data = Path(__file__).parent / "userdata.xlsx"

gchat = 'GChat'
time_message = 'TimeMessage'
# whats_app_sheet = 'Whatsapp'
whats_app_sheet = 'WA'
skype_sheet = 'Skype'
google_messages_sheet = 'GoogleMessages'

# WA availability
user_data_whatsapp = Path(__file__).parent / "data.xlsx"
whats_app_sheet_name = 'S1'


class Whatsapp(object):
    gsheet_name = 'airtel 0168...'
    gsheet_worksheet = 'Sheet1'
    gsheet_worksheet_result = 'Sheet2'

    # file_for_availability = Path(__file__).parent / 'Book1000.xlsx'
    # file_for_availability = Path(__file__).parent / '2000data.xlsx'
    # file_for_availability = Path(__file__).parent / 'phone_data/onelakh.xlsx'
    file_for_availability = Path(__file__).parent / 'phone_data/20k.xlsx'
    sheet_for_availability = 'S1'
    # sheet_for_availability = 'Sheet1'
    country_code_BD = '+880'

    message = 'Good evening'
    # message = 'ঘরে বসেই ডাক্তারি পরামর্শ '
    # message = 'সর্বোচ্চ মানের চিকিৎসা সেবা পেতে  ihealthcare bd আপনার পাশে। \n\n ৭০% ছাড়, \n পেতে নিচের লিঙ্কটি ক্লিক করুন। \n\n https://forms.gle/MkSBEHBEANpTqR1h8 \n\n বিস্তারিত জানতে - আজই যোগাযোগ করুন \n ihealthcare bd তে \n\n মোবাইলঃ০১৭১০৬৫১২৮৯ \n 📧hello@ihealthcare.com \n'
    # message = 'সর্বোচ্চ মানের চিকিৎসা সেবা পেতে  ihealthcare আপনার পাশে। \n\n৫০% ছাড়ে,\nআপনি ও আপনার পরিবার পেতে পারেন,\nপুরো ৩০দিনের চিকিৎসা সেবা।\n\nঅফারটি পেতে নিচের লিঙ্কটি ক্লিক করুন। \n\n🔗 https://forms.gle/MkSBEHBEANpTqR1h8\n\n\n📲 https://www.facebook.com/ihealthcare.global\n\nবিস্তারিত জানতে - আজই যোগাযোগ করুন\nihealthcare তে \n\nমোবাইলঃ ০১৭১০৬৫১২৮৯ \n📧ihealthcare.bd@gmail.com\n'


class Imo(object):
    gsheet_name = 'airtel 0168...'
    gsheet_worksheet = 'Sheet1'
    country_code_BD = '0'
    message = 'Good evening'


class Viber(object):
    gsheet_name = 'airtel 0168...'
    gsheet_worksheet = 'Sheet1'
    country_code_BD = '0'
    message = 'Good evening'


class Data(object):
    # Apk path
    google_chat = os.path.abspath(Path(__file__).parent.parent / 'apk/GoogleChat.apk')
    skype = os.path.abspath(Path(__file__).parent.parent / 'apk/Skype.apk')
    viber = os.path.abspath(Path(__file__).parent.parent / 'apk/Viber.apk')
    gmessages = os.path.abspath(Path(__file__).parent.parent / 'apk/GoogleMessages.apk')
    whatsapp = os.path.abspath(Path(__file__).parent.parent / 'apk/WhatsApp.apk.')
    imo = os.path.abspath(Path(__file__).parent.parent / 'apk/Imo.apk.')

    # App package and App activity

    gchat_app_package = 'com.google.android.apps.dynamite'
    gchat_app_activity = 'com.google.android.apps.dynamite.startup.StartUpActivity'
    skype_app_package = 'com.skype.raider'
    skype_app_activity = 'com.skype4life.MainActivity'
    viber_app_package = 'com.viber.voip'
    viber_app_activity = 'com.viber.voip.WelcomeActivity'
    gmessages_app_package = 'com.google.android.apps.messaging'
    gmessages_app_activity = 'com.google.android.apps.messaging.ui.ConversationListActivity'
    whatsapp_app_package = 'com.whatsapp'
    whatsapp_app_activity = 'com.whatsapp.HomeActivity'
    whatsapp_app_activity_main = 'com.whatsapp.Main'
    whatsapp_app_activity_reg = 'com.whatsapp.registration.EULA'
    imo_app_package = 'com.imo.android.imoim'
    imo_app_activity = 'com.imo.android.imoim.activities.Home'

    # Current apk
    current_apk_path = whatsapp
    current_app_package = whatsapp_app_package
    current_app_activity = whatsapp_app_activity

    # Credentials

    # Element properties
    element_id_attribute = 'elementId'
    index_attribute = 'index'
    package_attribute = 'package'
    class_attribute = 'class'
    text_attribute = 'text'
    content_desc_attribute = 'content-desc'
    resource_id_attribute = 'resource-id'
    checkable_attribute = 'checkable'
    checked_attribute = 'checked'
    clickable_attribute = 'clickable'
    enabled_attribute = 'enabled'
    focusable_attribute = 'focusable'
    focused_attribute = 'focused'
    long_clickable_attribute = 'long-clickable'
    password_attribute = 'password'
    scrollable_attribute = 'scrollable'
    selected_attribute = 'selected'
    bounds_attribute = 'bounds'
    displayed_attribute = 'displayed'

    # Whatsapp
    phone_number = ''
    username = ''

    # Skype
    group_name = 'QUPS-IR2'

    # Timeout
    point_five = 0.5
    one_second = 1
    two_seconds = 2
    three_seconds = 3
    four_seconds = 4
    five_seconds = 5
    six_seconds = 6
    seven_seconds = 7
    eight_seconds = 8
    nine_seconds = 9
    ten_seconds = 10
    fifteen_seconds = 15
    twenty_seconds = 20
    twenty_five_seconds = 25
    thirty_seconds = 30
    thirty_five_seconds = 35
    forty_seconds = 40
    forty_five_seconds = 45
    one_minute = 60
    two_minutes = 120
    three_minutes = 180
    four_minutes = 2400
    five_minutes = 3000
