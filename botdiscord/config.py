"""
CONFIGURAÇÕES DO BOT
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Configurações principais
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
BOT_NAME = "Organizador Pro"
VERSION = "2.0.0"

# Cores para embeds
COLORS = {
    "primary": 0x5865F2,      # Discord blue
    "success": 0x57F287,      # Discord green
    "warning": 0xFEE75C,      # Discord yellow
    "error": 0xED4245,        # Discord red
    "info": 0xEB459E,         # Discord pink
    "setup": 0x5865F2         # Setup color
}

# Permissões necessárias
REQUIRED_PERMISSIONS = [
    "administrator",
    "manage_channels",
    "manage_roles",
    "manage_messages",
    "view_audit_log"
]

# Limites
MAX_CHANNELS_PER_CATEGORY = 50
MAX_ROLES = 250
MAX_CHANNELS = 500

# Mensagens padrão
WELCOME_MESSAGES = [
    "🎉 Bem-vindo ao servidor!",
    "✨ Esperamos que você se divirta aqui!",
    "👋 Não esqueça de ler as regras!",
    "🎮 Divirta-se e faça novos amigos!"
]

# Logging
LOG_FILE = "bot.log"
LOG_LEVEL = "INFO"