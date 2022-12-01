from telegram.ext import CommandHandler, CallbackQueryHandler, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
    
################# MENU ####################
def pdf_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=pdf_menu_message(),
                            reply_markup=pdf_menu_keyboard()) 
  
def beeepdf_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=beeepdf_menu_message(),
                            reply_markup=beeepdf_menu_keyboard()) 
  
  
def mathspdf_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=beeepdf_menu_message(),
                            reply_markup=mathspdf_menu_keyboard())  
  
  
def ppspdf_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=beeepdf_menu_message(),
                            reply_markup=ppspdf_menu_keyboard())  
  
######################################### BEEE ##########################################################################
def beeeunit1_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/BEEE/BEEE-UNIT-1.pdf')))
  
def beeeunit2_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/BEEE/BEEE-UNIT-2.pdf')))
  
def beeeunit3_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/BEEE/BEEE-UNIT-3.pdf')))
  
def beeeunit4_menu(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/BEEE/BEEE-UNIT-4.pdf')))  
    
 
######################################### MATHS ##########################################################################

def mathsunit1_menu(update, context):
  context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/MATHS/Unit-1.pdf'))
  
def mathsunit2_menu(update, context):
 context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/MATHS/Unit-2.pdf'))
  
def mathsunit3_menu(update, context):
  context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/MATHS/Unit-3.pdf'))
  
def mathsunit4_menu(update, context):
 context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/BEEE/BEEE-UNIT-4.pdf'))

######################################### PPS ##########################################################################
def ppsc_menu(update, context):
 context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/PPS/C/Introduction-to-C.pdf'))
  
def ppspython_menu(update, context):
 context.bot.send_document(update.effective_chat.id, document=('https://jackwaghan.ml/MATHS/Unit-2.pdf'))



################# MESSAGE ####################  
def pdf_menu_message():
  return 'Hello there , i am here to help you to get your PDF😎... ' 

def beeepdf_menu_message():
  return 'Now select the unit you want to get... ' 


################# INLINE KEYBOARD ##############
def pdf_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('MATHS', callback_data='mathspdf')],
    [InlineKeyboardButton('BEEE', callback_data='eeepdf')],
    [InlineKeyboardButton('SCP', callback_data='scp')],
    [InlineKeyboardButton('PPS', callback_data='ppspdf')],
    [InlineKeyboardButton('Back', callback_data='main')]
  ]
  return InlineKeyboardMarkup(keyboard)

def beeepdf_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Unit 1', callback_data='111')],
    [InlineKeyboardButton('Unit 2', callback_data='112')],
    [InlineKeyboardButton('Unit 3', callback_data='113')],
    [InlineKeyboardButton('Unit 4', callback_data='114')],
    [InlineKeyboardButton('Back', callback_data='pdfmenu')]
  ]
  return InlineKeyboardMarkup(keyboard)

def mathspdf_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Unit 1', callback_data='121')],
    [InlineKeyboardButton('Unit 2', callback_data='122')],
    [InlineKeyboardButton('Unit 3', callback_data='123')],
    [InlineKeyboardButton('Unit 4', callback_data='124')],
    [InlineKeyboardButton('Back', callback_data='pdfmenu')]
  ]
  return InlineKeyboardMarkup(keyboard)


def ppspdf_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('C', callback_data='131')],
    [InlineKeyboardButton('Python', callback_data='132')],
    [InlineKeyboardButton('Back', callback_data='pdfmenu')]
  ]
  return InlineKeyboardMarkup(keyboard)


def unit1_menu_keyboard():
  keyboard = [
    [InlineKeyboardButton('Back', callback_data='main')]
  ]
  return InlineKeyboardMarkup(keyboard)

