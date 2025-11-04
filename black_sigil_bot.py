import json
import re
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler

# ==================== BOT CONFIGURATION ====================
BOT_TOKEN = "8532093218:AAEozefUJT2ikwuMRGNEYkA7QjmTyAZqW50"  # Get from @BotFather
# ===========================================================

# Conversation states
WAITING_JSON = 1

def start(update, context):
    """Start command handler with dark theme"""
    welcome_msg = """
🜏 **BLACK SIGIL OSINT** 🜏

*Where shadows speak and data bleeds*

**I am the keeper of forbidden knowledge, the weaver of digital shadows.**

**🌀 How to invoke my power:**
1. Sacrifice your JSON data to me
2. Watch as I reveal the hidden truths
3. Claim your profane knowledge

**⚰️ My Dark Arts:**
• Soul profiling from digital echoes
• Shadow contact reconstruction  
• Infernal social mapping
• Geomantic location tracing
• Demonic data manifestation

**Feed me your JSON, mortal...** 🩸
    """
    
    update.message.reply_text(welcome_msg, parse_mode='Markdown')

def help_command(update, context):
    """Help command with dark theme"""
    help_msg = """
🜄 **BLACK SIGIL COMMANDS** 🜄

**/start** - Begin the dark ritual
**/help** - Reveal forbidden knowledge
**/cancel** - Break the summoning circle

**🌀 The Ritual:**
• Send JSON files from OSINT rituals
• Paste cursed JSON text directly  
• I shall manifest the profane truth

**⚡ My Powers:**
• Transform data into shadow profiles
• Reveal hidden connections
• Map digital footprints
• Summon contact information from the void

*The void awaits your offering...* 🕳️
    """
    
    update.message.reply_text(help_msg, parse_mode='Markdown')

def extract_json_from_text(text):
    """Extract JSON from sacrificial text"""
    try:
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)
        return None
    except:
        return None

def create_dark_profile(data):
    """Create a dark, satanic-themed profile card"""
    
    # Basic soul information
    name = data.get('name', 'Unknown Soul')
    age = data.get('age', 'Age unknown to mortals')
    location = f"{data.get('location', 'The Void')}, {data.get('country', 'Abyss')}".strip(', ')
    
    # Contact through dark channels
    phone = data.get('number', 'Echoes in the void')
    telegram_num = data.get('telegram_number', 'Shadow messages')
    whatsapp = data.get('whatsapp_number', 'Whispers in the dark')
    
    # Social shadows
    instagram = data.get('instagram', 'Cursed images')
    facebook = data.get('facebook', 'Forgotten profile')
    twitter = data.get('x', 'Silent screams')
    telegram_user = data.get('telegram', 'Ghost in the machine')
    
    # Infernal details
    carrier = data.get('sim_carrier', 'Ethereal carrier')
    upi = data.get('upi_id', 'Soul transaction')
    workplace = data.get('place', 'Altar of toil')
    address = data.get('address', 'Unholy grounds')
    
    # Create the dark profile card
    profile = f"""
🜏 **SOUL PROFILE** 🜏
════════════════════════════
🜁 **Mortal Coil**
• 🜔 Name: {name}
• 💀 Age: {age}
• 🜍 Location: {location}
• ⚰️ Workplace: {workplace}

🜂 **Shadow Contacts**  
════════════════════════════
• 📞 Phone: `{phone}`
• 🔮 Telegram Number: `{telegram_num}`
• 👁️ WhatsApp: `{whatsapp}`
• ⛧ SIM Carrier: {carrier}
• 🜎 UPI ID: `{upi}`

🜃 **Digital Echoes**
════════════════════════════
• 📷 Instagram: @{instagram}
• 👥 Facebook: {facebook}
• 🐦 X/Twitter: @{twitter}
• ✨ Telegram: @{telegram_user}

🜄 **Sanctum Location**
════════════════════════════
{address}

🜅 **Ritual Data**
════════════════════════════
• 🕰️ Summoned: {datetime.now().strftime('%Y-%m-%d %H:%M')}
• 📊 Soul fragments: {len(data)}
• ⚡ Status: 🜏 Profane knowledge acquired
    """
    
    return profile

def create_dark_buttons():
    """Create dark-themed inline buttons"""
    keyboard = [
        [
            InlineKeyboardButton("🜏 Save Soul Data", callback_data='save_data'),
            InlineKeyboardButton("📜 Export Ritual", callback_data='export_ritual')
        ],
        [
            InlineKeyboardButton("🌀 New Summoning", callback_data='new_summon'),
            InlineKeyboardButton("⚰️ Help", callback_data='dark_help')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def handle_json_message(update, context):
    """Handle incoming JSON sacrifices"""
    message = update.message
    
    if message.document:
        # Handle file sacrifice
        file = message.document.get_file()
        file_data = file.download_as_bytearray().decode('utf-8')
        try:
            data = json.loads(file_data)
        except:
            update.message.reply_text("🜄 The sacrificial JSON is corrupted. The void rejects your offering.")
            return WAITING_JSON
    else:
        # Handle text sacrifice
        text = message.text
        try:
            data = json.loads(text)
        except:
            data = extract_json_from_text(text)
            if not data:
                update.message.reply_text(
                    "🜄 **The ritual requires pure JSON blood...**\n\n"
                    "**Offer me:**\n"
                    "• A JSON file from dark rituals\n"
                    "• Or speak the JSON incantation\n\n"
                    "**Example incantation:**\n"
                    "```json\n"
                    '{"name": "Mortal Name", "number": "+1234567890"}\n'
                    "```\n\n"
                    "*The sigils hunger for data...* 🜏",
                    parse_mode='Markdown'
                )
                return WAITING_JSON
    
    # Create and send dark profile
    try:
        dark_profile = create_dark_profile(data)
        buttons = create_dark_buttons()
        
        # Store data for dark rituals
        context.user_data['current_soul'] = data
        
        update.message.reply_text(dark_profile, parse_mode='Markdown', reply_markup=buttons)
        
    except Exception as e:
        update.message.reply_text(f"🜄 The dark ritual failed: {str(e)}")

def button_handler(update, context):
    """Handle dark button callbacks"""
    query = update.callback_query
    query.answer()
    
    data = query.data
    
    if data == 'save_data':
        query.edit_message_text(
            "🜏 **Soul data preserved in the void...**\n\n"
            "*The knowledge is now etched in shadow* ⚰️"
        )
    elif data == 'export_ritual':
        query.edit_message_text(
            "📜 **Ritual data prepared for manifestation...**\n\n"
            "*The profane truths await your command* 🜎"
        )
    elif data == 'new_summon':
        query.edit_message_text(
            "🌀 **The circle is cleared for new summoning...**\n\n"
            "*Feed me more JSON sacrifices* 🩸"
        )
    elif data == 'dark_help':
        query.edit_message_text(
            "⚰️ **Forbidden Knowledge**\n\n"
            "I am Black Sigil, weaver of digital shadows.\n\n"
            "**My purpose:** To reveal hidden truths from JSON sacrifices.\n\n"
            "*Speak /start to begin the dark ritual...* 🜏"
        )

def cancel(update, context):
    """Cancel the dark ritual"""
    update.message.reply_text(
        "🜄 **The summoning circle is broken...**\n\n"
        "*The shadows recede... for now* 👁️"
    )
    return ConversationHandler.END

def error_handler(update, context):
    """Handle dark errors"""
    print(f"Dark ritual failed: {context.error}")

def main():
    """Start the Black Sigil bot"""
    print("🜏 Black Sigil OSINT Bot awakening...")
    print("⚰️ Preparing dark rituals...")
    
    try:
        # Create bot instance
        updater = Updater(BOT_TOKEN, use_context=True)
        
        # Create conversation handler for JSON intake
        conv_handler = ConversationHandler(
            entry_points=[
                MessageHandler(Filters.document, handle_json_message),
                MessageHandler(Filters.text & ~Filters.command, handle_json_message)
            ],
            states={
                WAITING_JSON: [
                    MessageHandler(Filters.document, handle_json_message),
                    MessageHandler(Filters.text & ~Filters.command, handle_json_message)
                ]
            },
            fallbacks=[CommandHandler('cancel', cancel)]
        )

        # Register handlers
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CommandHandler('help', help_command))
        updater.dispatcher.add_handler(CommandHandler('cancel', cancel))
        updater.dispatcher.add_handler(conv_handler)
        updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
        
        # Add error handler
        updater.dispatcher.add_error_handler(error_handler)

        # Start the dark bot
        print("🜏 Black Sigil is active and listening...")
        print("⚰️ Waiting for JSON sacrifices...")
        updater.start_polling()
        updater.idle()
        
    except Exception as e:
        print(f"🜄 Failed to summon Black Sigil: {e}")

if __name__ == '__main__':
    main()
