# gChat
class GChatPageLocator(object):
    change_profile = '//android.widget.FrameLayout/android.widget.ImageView[2]'
    sh_qups = '//android.view.ViewGroup[@content-desc="Use shahwata halder sh.qups@gmail.com"]'

    ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    navigation = '//android.widget.ImageButton[@content-desc="Navigation menu"]'
    search_btn = '//android.widget.TextView[@resource-id="com.google.android.apps.dynamite:id/open_search_bar_text_view"]'
    search_text = '//android.widget.EditText[@resource-id="com.google.android.apps.dynamite:id/search_term"]'
    search_text1 = '//android.widget.EditText[@resource-id="com.google.android.apps.dynamite:id/open_search_view_edit_text"]'
    select_person = '//android.widget.LinearLayout[@resource-id="com.google.android.apps.dynamite:id/user_name_and_indicators"]'

    chat_persons = '/android.widget.TextView[@resource-id="com.google.android.apps.dynamite:id/open_search_bar_text_view"]//android.widget.LinearLayout'
    chat_message = '//android.widget.EditText[@resource-id="com.google.android.apps.dynamite:id/compose_edit_text"]'
    post_message = '//android.widget.ImageButton[@resource-id="com.google.android.apps.dynamite:id/post_message_button"]'
    back_from_chat = '//android.widget.ImageButton[@content-desc="Navigate Up"]'
    seen_message = '//android.widget.ImageView[@resource-id="com.google.android.apps.dynamite:id/read_receipt_right_avatar_a"]'

    new_chat = '//android.widget.Button[@resource-id="com.google.android.apps.dynamite:id/fab_stub"]'
    chat = '//android.widget.FrameLayout[@content-desc="Chat"]'
    rooms = '//android.widget.FrameLayout[@content-desc="Rooms"]'
    searched_room = '//android.widget.TextView[@resource-id="com.google.android.apps.dynamite:id/group_name"]'


# Whatsapp
class WhatsappPageLocator(object):
    agree_and_continue = '//android.widget.Button[@resource-id="com.whatsapp:id/eula_accept"]'
    phone_number = '//android.widget.EditText[@resource-id="com.whatsapp:id/registration_phone"]'
    next_registration_submit = '//android.widget.Button[@resource-id="com.whatsapp:id/registration_submit"]'
    ok = '//android.widget.Button[@resource-id="android:id/button1"]'
    continue_whatsapp = '//android.widget.Button[@resource-id="com.whatsapp:id/submit"]'
    allow = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
    enter_name = '//android.widget.EditText[@resource-id="com.whatsapp:id/registration_name"]'
    next_register_name_accept = '//android.widget.Button[@resource-id="com.whatsapp:id/register_name_accept"]'
    give_permission = '//android.widget.Button[@resource-id="android:id/button1"]'
    account = '//android.widget.LinearLayout[3]/android.widget.RadioButton[@resource-id="com.whatsapp:id/radio"]'

    skip_permission = '//android.widget.Button[@resource-id="android:id/button"]'

    search = '//android.widget.TextView[@resource-id="com.whatsapp:id/menuitem_search"]'
    search_input = '//android.widget.EditText[@resource-id="com.whatsapp:id/search_input"]'
    # search_input1 = '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/search_input_layout"]'
    # chat_person = '//android.widget.RelativeLayout[@resource-id="com.whatsapp:id/contact_row_container"]'
    chat_person = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout'
    # chat_person = '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/conversations_row_header"]'
    # chat_person = '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/conversations_row_content"]'

    # chat_person = '//androidx.recyclerview.widget.RecyclerView'

    select_multiple_chat_person = '//android.widget.TextView[@resource-id="com.whatsapp:id/conversations_row_contact_name"]'
    select_multiple_chat_person1 = '//android.widget.FrameLayout[@resource-id="com.whatsapp:id/contact_selector"]'
    # chat_message = '//android.widget.EditText[@resource-id="com.whatsapp:id/entry"]'
    chat_message = '//android.widget.EditText[@resource-id="com.whatsapp:id/entry"]'
    # chat_message = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText'
    post_message = '//android.widget.ImageButton[@resource-id="com.whatsapp:id/send"]'
    back = '//android.widget.ImageView[@resource-id="com.whatsapp:id/whatsapp_toolbar_home"]'

    # send image
    forward = '//android.widget.ImageView[@content-desc="Forward to…"]'
    send_image = '//android.widget.ImageButton[@content-desc="Send"]'
    # send image from gallary
    attachment = '//android.widget.ImageButton[@content-desc="Attach"]'
    gallary = '//android.widget.TextView[@resource-id="com.whatsapp:id/pickfiletype_gallery_holder"]//android.widget.ImageButton'
    gallary1 = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.ImageButton'
    image_folder = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.ImageView'
    photo = '//android.widget.ImageView[@content-desc="Photo"]'
    caption = '//android.widget.LinearLayout[@content-desc="Add a caption…"]'
    caption_text = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText'
    # caption_text1 = '//android.widget.ImageButton[@resource-id="com.whatsapp:id/caption"]'
    send_image_from_gallery = '//android.widget.ImageButton[@content-desc="Send"]'

    # extract contacts
    select_group = '//android.widget.RelativeLayout[@resource-id="com.whatsapp:id/contact_row_container"]'
    more_options = '//android.widget.ImageView[@content-desc="More options"]'
    group_info = '//android.widget.TextView[@resource-id="com.whatsapp:id/title"]'
    group_info_direct = '//android.widget.TextView[@resource-id="com.whatsapp:id/conversation_contact_name"]'
    contacts_parent = '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/group_chat_info_layout"]'
    contacts = '//android.widget.ImageView[@resource-id="com.whatsapp:id/avatar"]'

    total_members = '//android.widget.TextView[@resource-id="com.whatsapp:id/participants_title"]'
    show_more = '//android.widget.ImageView[@content-desc="Contact Profile Photo"]'
    # group_member = '//android.widget.TextView[@resource-id="com.whatsapp:id/group_chat_info_layout"]'
    group_member = '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/group_chat_info_layout"]'

    # not_saved_number = '//android.widget.TextView[@resource-id="android:id/title" and contains(@text,"Message ")]'

    add_to_contacts = '//android.widget.TextView[@text="Add to contacts"]'
    message_contact = '//android.widget.TextView[contains(@text,"Message ")]'
    view_contact = '//android.widget.TextView[contains(@text,"View ")]'
    contact_number = '//android.widget.TextView[@resource-id="com.whatsapp:id/title_tv"]'


# Skype
class SkypePageLocator(object):
    lets_go = '//android.widget.Button[@content-desc="Let\'s go"]'
    sign_in_or_create = '//android.widget.Button[@content-desc="Sign in or create"]'

    search = '//android.widget.Button[@content-desc="People, groups & messages"]'
    search_input = '//android.widget.EditText[@content-desc="Search"]'
    clear_search = '//android.widget.Button[@content-desc="Clear search text"]'

    @staticmethod
    def select_chat_person(name):
        chat_person = f'//android.widget.Button[contains(@content-desc,"{name}")]'
        # chat_person = f'//android.widget.TextView[@text="{name}"]/...'
        return chat_person

    chat_message = '//android.widget.EditText[@content-desc="Type a message"]'
    post_message = '//android.widget.Button[@content-desc="Send message"]'
    back_from_chat = '//android.widget.Button[@content-desc="Back"]'
    show_more = '//android.widget.Button[@content-desc="Show more"]'
    # open_gallery = '//android.widget.Button[@content-desc="Open Chat gallery"]'
    # noti_on = '//android.widget.Button[@content-desc="On"]'
    # noti_off = '(//android.widget.Button[@content-desc="Off"])[1]'
    header = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.View'
    group_icon = '//android.view.ViewGroup[@content-desc="QUPS IR2"]/android.view.ViewGroup/android.view.ViewGroup'
    group_creator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    share_link_to_join = '//android.widget.Button[@content-desc="Share link to join group"]/android.widget.TextView[2]'
    send_message = '//android.widget.Button[@content-desc="Send message"]/android.view.ViewGroup'
    schedule_a_call = '//android.widget.Button[@content-desc="Schedule a call"]/android.view.ViewGroup'
    search_in_conversation = '//android.widget.Button[@content-desc="Search in conversation"]/android.view.ViewGroup'

    elele = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]'

    # total_members = '//android.widget.Button[contains(@content-desc,"PARTICIPANTS, header")]'
    # total_members = '//android.widget.Button[contains(text(),"PARTICIPANTS, header")]'
    # total_members = '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]'
    total_members = '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView/android.widget.TextView'
    view_profile = '//android.widget.TextView[@resource-id="android:id/text1"]'
    scrollable_element = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView'
    scrollable_element1 = '//android.view.ViewGroup[@class="android.widget.ScrollView"]'
    scrollable_element2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
    profile_click = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'

    profile1 = f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'

    @staticmethod
    def profile_person(number):
        profile = f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[{number}]'
        return profile

    profile_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
    skype_name = '//android.widget.Button[contains(@content-desc,"Skype Name,")]'


# Google Messages
class GoogleMessagesPageLocator(object):
    start_chat = '//android.widget.Button[@content-desc="Start chat"]'
    to = '//android.widget.MultiAutoCompleteTextView[@resource-id="com.google.android.apps.messaging:id/recipient_text_view"]'
    message_input = '//android.widget.MultiAutoCompleteTextView[@resource-id="com.google.android.apps.messaging:id/compose_message_text"]'
    send_message = '//android.widget.MultiAutoCompleteTextView[@resource-id="com.google.android.apps.messaging:id/send_message_button_icon"]'
    back = '//android.widget.ImageButton[@content-desc="Navigate up"]'


# imo
class ImoPageLocator(object):
    contacts = '(//android.widget.TextView[@resource-id="com.imo.android.imoim:id/tv_tab_text"])[4]'
    single_contacts = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/layout_buddy_info"]'
    # single_contacts = '(//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/layout_buddy_info"])[10]'

    # contacts = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup[4]/android.widget.TextView'
    # single_contacts = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[5]/android.widget.RelativeLayout/android.widget.RelativeLayout'
    # single_contacts1 = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/rl_root"]'
    # single_contacts1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[5]/android.widget.RelativeLayout'

    contact_profile = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'

    contact_profile1 = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/icon_view"]'
    contact_profile1 = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView'

    contact_profile2 = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/text_view"]'
    contact_profile2 = '///hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView'
    contact_number = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView[2]'
    contact_number = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/tv_bio_content"]'

    search = '//android.view.View[@resource-id="com.imo.android.imoim:id/search"]'
    search_input = '//android.widget.EditText[@resource-id="com.imo.android.imoim:id/custom_search_view"]'
    chat_person = '//android.widget.RelativeLayout[@resource-id="com.imo.android.imoim:id/show"]'
    chat_message = '//android.widget.EditText[@resource-id="com.imo.android.imoim:id/chat_input"]'
    post_message = '//android.widget.ImageView[@resource-id="com.imo.android.imoim:id/chat_send"]'

    img_attachment = '//android.widget.ImageView[@resource-id="com.imo.android.imoim:id/chat_gallery"]'


# viber

class ViberPageLocator(object):
    search = '//android.widget.TextView[@resource-id="com.viber.voip:id/menu_search"]'
    search_input = '//android.widget.EditText[@resource-id="com.viber.voip:id/search_src_text"]'
    chat_person = '//android.view.ViewGroup[@resource-id="com.viber.voip:id/root"]'
    chat_message = '//android.widget.EditText[@resource-id="com.viber.voip:id/send_text"]'
    post_message = '//android.widget.FrameLayout[@resource-id="com.viber.voip:id/btn_send"]'

    img_attachment = '//android.widget.ImageView[@resource-id="com.viber.voip:id/options_menu_open_gallery"]'
