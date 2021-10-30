# from utils.excel_utils import *
# from data.data import *
import ast
import pandas as pd
from pathlib import Path

wa_file = Path(__file__).parent.parent / 'data/phone_data/20k.xlsx'

# Gchat
# maxRow = getRowCount(user_data, gchat)
# email_sending = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 1), None)
# userName = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 2), None)
# seenOldBound = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 4), None)
# seenOldBound = [i.strip('][').split(', ') for i in seenOldBound]
# seenOldBound = [ast.literal_eval(i) for i in seenOldBound]
# room = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 5), None)
#
# # sheet two
# maxRow = getRowCount(user_data, time_message)
# time = remove_items(readsinglecol(user_data, time_message, 2, maxRow, 1), None)
# message = remove_items(readsinglecol(user_data, time_message, 2, maxRow, 2), None)
# print(email_sending)
# print(userName)
# print(room)
# print(time)
# print(message)


# whats app
# maxRow = getRowCount(user_data, whats_app_sheet)
# phone = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 1), None)
# whatsAppGroup = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 3), None)
# whatsAppGroupMessage = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 2), None)


# print(phone)
# print(len(phone))
# # print(whatsAppGroup)
# print(whatsAppGroupMessage)
print(wa_file)


def get_active_numbers(messenger, file):
    dataframe = pd.read_excel(file)
    # print(dataframe)
    numbers = dataframe.loc[dataframe["Whatsapp"] == 1, ["Mobile_Numbers"]]["Mobile_Numbers"].to_list()
    return [int(number[2:]) for number in numbers]


#
get_active_numbers("Whatsapp", wa_file)
phone = get_active_numbers("Whatsapp", wa_file)
print(phone)
# skype
# maxRow = getRowCount(user_data, skype_sheet)
# people = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 1), None)
# skypeName = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 2), None)
# skypeGroup = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 3), None)
# skypeMessage = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 5), None)
# print(people)
# print(skypeGroup)
# print(skypeMessage)

# GoogleMessages
# maxRow = getRowCount(user_data, google_messages_sheet)
# phoneNumber = remove_items(readsinglecol(user_data, google_messages_sheet, 2, maxRow, 1), None)
# messages = remove_items(readsinglecol(user_data, google_messages_sheet, 2, maxRow, 3), None)

# convert string formatted list to actual list
# b = "[1, 2, 3, 4, 5]"
# res = b.strip('][').split(', ')
# print("final list", res)
# res = ast.literal_eval(b)
# print("final list", res)
