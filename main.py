import os
import telebot
from solders.keypair import Keypair
from solders.pubkey import Pubkey

# Get secrets from environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SOLANA_KEY = os.getenv("SOLANA_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Solana Sniper Bot Activated! \nUse /buy or /sell commands.")

@bot.message_handler(commands=['buy'])
def buy_token(message):
    bot.reply_to(message, "✅ Buy order executed (simulation).")

@bot.message_handler(commands=['sell'])
def sell_token(message):
    bot.reply_to(message, "✅ Sell order executed (simulation).")

bot.infinity_polling()
