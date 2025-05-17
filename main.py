from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في PromptsDealer_bot! أرسل /prompt للحصول على جملة إبداعية.")

async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompts = [
        "Imagine you are a detective in a city of robots. What mystery are you solving?",
        "Write a dialogue between the moon and a lost astronaut.",
        "Explain quantum computing to a 5-year-old using a bedtime story.",
        "You wake up in a world where everyone can read thoughts. What do you do?",
        "Describe a futuristic café run entirely by AI, including the menu.",
        "Generate startup ideas combining agriculture and AI.",
        "Create a fantasy world where magic is powered by emotions.",
        "What would happen if humans could only speak using song lyrics?"
    ]
    await update.message.reply_text("🧠 Prompt:\n" + random.choice(prompts))

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اكتب /prompt وسأعطيك فكرة مذهلة 👇")

app = ApplicationBuilder().token("7015363345:AAEj0HPuYzXPLZ-oO7M5RUlbuYMqAHXgROo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("prompt", prompt))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
