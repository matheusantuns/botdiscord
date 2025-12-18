"""
BOT DE ORGANIZAÇÃO PROFISSIONAL DISCORD
Arquivo principal: main.py
"""

import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio
from datetime import datetime, timedelta
import json
import re

# ========== CONFIGURAÇÃO ==========
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    print("❌ ERRO: Token não encontrado no arquivo .env")
    print("👉 Certifique-se de que o arquivo .env existe e tem:")
    print('DISCORD_TOKEN=seu_token_aqui')
    exit()

# Configurar intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.presences = True

# Criar bot
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None
)

# Sistema de dados dos usuários
user_data = {}
DATA_FILE = "user_data.json"

def load_user_data():
    global user_data
    try:
        with open(DATA_FILE, 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}

def save_user_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(user_data, f, indent=4)

load_user_data()

# ========== TEMPLATES COMPLETOS ==========
TEMPLATES = {
    # ========== TEMPLATE GAMING ULTRA ==========
    "gaming": {
        "name": "🎮 Gaming Universe",
        "emoji": "🎮",
        "description": "Servidor premium para gamers competitivos e casuais com organização profissional",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios oficiais", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Leia as regras", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Apresente-se!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos membros", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│geral", "topic": "💭 Conversas gerais", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│games-discussão", "topic": "🕹️ Discussão geral sobre jogos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│fps", "topic": "🔫 Valorant, CS2, COD", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "⚔️│moba", "topic": "🏰 League of Legends, Dota 2", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎲│casual", "topic": "🎪 Stardew Valley, Minecraft", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎪│rpg", "topic": "🐉 D&D, Genshin Impact", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎵│musica", "topic": "🎧 Recomendações musicais", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎥│clips", "topic": "📹 Compartilhe seus melhores momentos!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🤣│memes", "topic": "😂 Memes e humor", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎨│artes", "topic": "🖌️ Arte, designs e criatividade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🍿│filmes-series", "topic": "🎬 Recomendações de filmes e séries", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💡│sugestões", "topic": "💭 Sugira melhorias para o servidor", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "❓│ajuda", "topic": "🆘 Precisa de ajuda? Pergunte aqui!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│conquistas", "topic": "⭐ Compartilhe suas conquistas!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📱│offtopic", "topic": "💬 Conversas fora do tema gaming", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "🎮│Lobby Principal", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎯│FPS Squad", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "⚔️│MOBA Team", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎲│Casual Chat", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎪│RPG Session", "user_limit": 6, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎵│Ouvindo Música", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎤│Karaokê", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎧│Foco Total", "user_limit": 1, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "💤│AFK Zone", "user_limit": 0, "permissions": {"everyone": ["connect"]}},
                {"name": "🎮│Torneio 1", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎮│Torneio 2", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}}
            ],
            "category": [
                {"name": "📢│INFORMAÇÕES", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "💬│COMUNIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│JOGOS", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎤│VOICE CHAT", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "🏆│TORNEIOS", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "🎨│CRIATIVIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "👑│Dono", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "⚡│Co-Fundador", "color": "purple", "permissions": ["manage_guild", "manage_channels"], "hoist": True, "mentionable": True},
                {"name": "🛡️│Administrador", "color": "red", "permissions": ["manage_guild", "manage_channels", "manage_roles", "kick_members", "ban_members"], "hoist": True, "mentionable": True},
                {"name": "⭐│Moderador", "color": "blue", "permissions": ["manage_messages", "kick_members", "mute_members", "deafen_members"], "hoist": True, "mentionable": True}
            ],
            "community": [
                {"name": "🎮│Pro Player", "color": "green", "permissions": ["priority_speaker"], "hoist": True, "mentionable": True},
                {"name": "🌟│VIP", "color": "orange", "permissions": ["priority_speaker", "stream"], "hoist": True, "mentionable": True},
                {"name": "🏆│Campeão", "color": "yellow", "permissions": [], "hoist": True, "mentionable": False},
                {"name": "🎯│Competitivo", "color": "dark_red", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎲│Casual", "color": "dark_green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎥│Streamer", "color": "pink", "permissions": ["stream"], "hoist": True, "mentionable": False},
                {"name": "🎨│Artista", "color": "magenta", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎵│DJ", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False}
            ],
            "special": [
                {"name": "🤖│Bot", "color": "teal", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🔔│Notificado", "color": "light_blue", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎪│Membro", "color": "default", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "👀│Spectator", "color": "grey", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": True,
            "music_bot": True,
            "moderation_bot": True
        }
    },
    
    # ========== TEMPLATE ESTUDO PRO ==========
    "estudo": {
        "name": "📚 Academia Pro",
        "emoji": "📚",
        "description": "Plataforma educacional completa com recursos para aprendizado colaborativo",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes e avisos", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Regras da comunidade de estudos", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Boas-vindas! Conte-nos sobre você", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos alunos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│geral", "topic": "💭 Conversas gerais sobre estudos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📚│material", "topic": "📖 Compartilhe materiais de estudo", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "❓│dúvidas", "topic": "🤔 Tire suas dúvidas aqui", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📅│calendário", "topic": "🗓️ Datas importantes e prazos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📝│anotações", "topic": "✏️ Anotações compartilhadas e resumos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🔬│ciências", "topic": "🧪 Biologia, Química, Física", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🧮│matemática", "topic": "📐 Cálculo, Álgebra, Geometria", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💻│programação", "topic": "👨‍💻 Python, JavaScript, Java, C++", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🌍│humanas", "topic": "📖 História, Geografia, Filosofia", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💼│administração", "topic": "📊 Negócios, Economia, Marketing", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎨│artes", "topic": "🖌️ Arte, Design, Música", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│conquistas", "topic": "⭐ Compartilhe suas conquistas!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💡│dicas", "topic": "💭 Técnicas de estudo e produtividade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📖│recomendações", "topic": "📚 Livros, cursos e recursos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "☕│descontração", "topic": "🎮 Hora do café e descanso", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "📚│Sala de Estudos 1", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "📚│Sala de Estudos 2", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "📚│Sala de Estudos 3", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "💭│Sala de Discussão", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎤│Aula Online", "user_limit": 50, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎧│Foco Total", "user_limit": 1, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "👥│Grupo de Estudo", "user_limit": 8, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "☕│Pausa Café", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎵│Ambiente Calmo", "user_limit": 3, "permissions": {"everyone": ["connect", "speak"]}}
            ],
            "category": [
                {"name": "📢│INFORMAÇÕES", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "📚│ÁREAS DE ESTUDO", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎤│SALAS DE ESTUDO", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "💬│COMUNIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│PROGRESSO", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "👑│Coordenador", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "👨‍🏫│Professor", "color": "blue", "permissions": ["manage_channels", "manage_messages"], "hoist": True, "mentionable": True},
                {"name": "📚│Monitor", "color": "green", "permissions": ["manage_messages"], "hoist": True, "mentionable": True}
            ],
            "community": [
                {"name": "🎓│Aluno Avançado", "color": "purple", "permissions": ["priority_speaker"], "hoist": True, "mentionable": False},
                {"name": "💻│Programador", "color": "orange", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🔬│Cientista", "color": "teal", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎨│Artista", "color": "pink", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "📖│Leitor", "color": "dark_blue", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎯│Focado", "color": "dark_green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "⭐│Destaque", "color": "yellow", "permissions": [], "hoist": True, "mentionable": False}
            ],
            "special": [
                {"name": "🤖│Bot", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🤝│Voluntário", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎁│Convidado", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "👨‍🎓│Aluno", "color": "default", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": True,
            "music_bot": False,
            "moderation_bot": True
        }
    },
    
    # ========== TEMPLATE STREAMER PRO ==========
    "streamer": {
        "name": "🎥 Streamer Pro",
        "emoji": "🎥",
        "description": "Servidor profissional para streamers com ferramentas para crescimento e engajamento",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios das lives e novidades", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Regras da comunidade do streamer", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Bem-vindo à comunidade!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos viewers", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│chat-geral", "topic": "💭 Conversas da comunidade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│games", "topic": "🕹️ Discussão sobre jogos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎥│clips", "topic": "📹 Compartilhe seus melhores clips", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🤣│memes", "topic": "😂 Memes da comunidade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│sugestões", "topic": "💭 Sugira jogos e ideias para lives", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎵│playlist", "topic": "🎧 Sugestões musicais", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📊│metas", "topic": "📈 Metas do canal e conquistas", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💻│setup", "topic": "🖥️ Equipamentos e configurações", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎨│artes", "topic": "🖌️ Artes, overlays e designs", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🤝│colabs", "topic": "👥 Propostas de colaborações", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│highlights", "topic": "⭐ Melhores momentos da semana", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💰│doações", "topic": "💸 Informações sobre doações", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "❓│ajuda", "topic": "🆘 Precisa de ajuda? Pergunte aqui!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "☕│offstream", "topic": "💬 Conversas fora das lives", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "🎤│Sala do Streamer", "user_limit": 1, "permissions": {"everyone": ["view_channel"], "streamer": ["connect", "speak"]}},
                {"name": "🎮│Gaming com Subs", "user_limit": 5, "permissions": {"everyone": ["view_channel"], "subscriber": ["connect", "speak"]}},
                {"name": "💬│Call da Comunidade", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎵│Ouvindo Música", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎤│Karaokê", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎧│Edição", "user_limit": 3, "permissions": {"everyone": ["view_channel"], "staff": ["connect", "speak"]}},
                {"name": "👥│Colaboração", "user_limit": 4, "permissions": {"everyone": ["view_channel"], "vip": ["connect", "speak"]}},
                {"name": "💤│AFK", "user_limit": 0, "permissions": {"everyone": ["connect"]}},
                {"name": "🎮│Torneio 1", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎮│Torneio 2", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}}
            ],
            "category": [
                {"name": "📢│INFORMAÇÕES", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "🎥│COMUNIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│CONTEÚDO", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎤│VOICE", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "💼│NEGÓCIOS", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "🎥│Streamer", "color": "purple", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "👑│Dono", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "⭐│Moderador", "color": "blue", "permissions": ["manage_messages", "kick_members"], "hoist": True, "mentionable": True}
            ],
            "community": [
                {"name": "👑│Subscriber", "color": "red", "permissions": ["priority_speaker"], "hoist": True, "mentionable": True},
                {"name": "🌟│VIP", "color": "orange", "permissions": ["priority_speaker", "stream"], "hoist": True, "mentionable": True},
                {"name": "🎮│Gamer", "color": "green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎨│Designer", "color": "pink", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "💻│Tech", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "💰│Doador", "color": "yellow", "permissions": [], "hoist": True, "mentionable": False},
                {"name": "🏆│Campeão", "color": "magenta", "permissions": [], "hoist": True, "mentionable": False}
            ],
            "special": [
                {"name": "🤖│Bot", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🔔│Notificado", "color": "green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "👥│Comunidade", "color": "default", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": True,
            "music_bot": True,
            "moderation_bot": True
        }
    },
    
    # ========== TEMPLATE EMPRESA CORPORATIVO ==========
    "empresa": {
        "name": "💼 Nexus Corporativo",
        "emoji": "💼",
        "description": "Ambiente profissional para empresas com estrutura para departamentos e comunicação eficiente",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Comunicados corporativos oficiais", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Políticas e normas da empresa", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Boas-vindas à equipe!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│onboarding", "topic": "✨ Guia de integração de novos colaboradores", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│geral", "topic": "💭 Comunicação geral da empresa", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💼│rh", "topic": "👥 Recursos Humanos e administrativo", "permissions": {"everyone": ["view_channel"], "hr": ["send_messages"]}},
                {"name": "📊│financeiro", "topic": "💰 Finanças e contabilidade", "permissions": {"everyone": ["view_channel"], "finance": ["send_messages"]}},
                {"name": "🛠️│ti", "topic": "💻 Tecnologia da Informação", "permissions": {"everyone": ["view_channel"], "it": ["send_messages"]}},
                {"name": "📈│vendas", "topic": "🛒 Vendas e comercial", "permissions": {"everyone": ["view_channel"], "sales": ["send_messages"]}},
                {"name": "🎯│marketing", "topic": "📣 Marketing e publicidade", "permissions": {"everyone": ["view_channel"], "marketing": ["send_messages"]}},
                {"name": "⚙️│ops", "topic": "🚚 Operações e logística", "permissions": {"everyone": ["view_channel"], "operations": ["send_messages"]}},
                {"name": "💡│projetos", "topic": "📋 Gerenciamento de projetos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📝│relatórios", "topic": "📄 Relatórios e métricas", "permissions": {"everyone": ["view_channel"], "manager": ["send_messages"]}},
                {"name": "🎯│metas", "topic": "⭐ Metas e objetivos trimestrais", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "🤝│clientes", "topic": "👨‍💼 Atendimento ao cliente", "permissions": {"everyone": ["view_channel"], "customer_service": ["send_messages"]}},
                {"name": "💡│ideias", "topic": "💭 Sugestões e melhorias", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│conquistas", "topic": "🎉 Celebrando conquistas da equipe", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "☕│break", "topic": "🎮 Momento descontração e café", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "💼│Reunião Geral", "user_limit": 50, "permissions": {"everyone": ["view_channel", "connect", "speak"]}},
                {"name": "💼│Reunião Diretoria", "user_limit": 10, "permissions": {"everyone": ["view_channel"], "director": ["connect", "speak"]}},
                {"name": "💼│Reunião de Equipe", "user_limit": 15, "permissions": {"everyone": ["view_channel"], "team_lead": ["connect", "speak"]}},
                {"name": "💬│Call Rápida", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎤│Apresentações", "user_limit": 100, "permissions": {"everyone": ["view_channel", "connect", "speak"]}},
                {"name": "🤝│Sala de Clientes", "user_limit": 10, "permissions": {"everyone": ["view_channel"], "sales": ["connect", "speak"]}},
                {"name": "☕│Cafeteria Virtual", "user_limit": 20, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎧│Foco Individual", "user_limit": 1, "permissions": {"everyone": ["connect", "speak"]}}
            ],
            "category": [
                {"name": "📢│CORPORATIVO", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "💼│DEPARTAMENTOS", "permissions": {"everyone": ["view_channel"], "department_head": ["send_messages"]}},
                {"name": "🎤│REUNIÕES", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "💬│COMUNICAÇÃO", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│DESENVOLVIMENTO", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "👑│CEO", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "👔│Diretor", "color": "purple", "permissions": ["manage_guild", "manage_channels"], "hoist": True, "mentionable": True},
                {"name": "👨‍💼│Gerente", "color": "blue", "permissions": ["manage_channels", "manage_messages"], "hoist": True, "mentionable": True},
                {"name": "💼│Líder", "color": "green", "permissions": ["manage_messages"], "hoist": True, "mentionable": True}
            ],
            "department": [
                {"name": "💻│TI", "color": "red", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "📊│Financeiro", "color": "dark_green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "📈│Vendas", "color": "yellow", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎯│Marketing", "color": "magenta", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "⚙️│Operações", "color": "orange", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "👥│RH", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False}
            ],
            "special": [
                {"name": "👨‍💻│Sênior", "color": "orange", "permissions": ["priority_speaker"], "hoist": False, "mentionable": False},
                {"name": "💼│Pleno", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎯│Júnior", "color": "teal", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🤝│Estagiário", "color": "pink", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🤖│Bot", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "👥│Colaborador", "color": "default", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": False,
            "music_bot": False,
            "moderation_bot": True
        }
    },
    
    # ========== TEMPLATE ARTES CRIATIVAS ==========
    "artes": {
        "name": "🎨 Creative Hub",
        "emoji": "🎨",
        "description": "Comunidade para artistas, designers e criativos de todas as áreas",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes da comunidade", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Regras para compartilhamento de arte", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Apresente-se e mostre seu trabalho!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│introdução", "topic": "✨ Guia para novos artistas", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│geral", "topic": "💭 Conversas gerais sobre arte", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎨│arte-digital", "topic": "🖥️ Photoshop, Illustrator, Procreate", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🖌️│tradicional", "topic": "✏️ Pintura, desenho, escultura", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎭│conceito", "topic": "💡 Character design, concept art", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📷│fotografia", "topic": "📸 Fotografia e edição", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎬│animação", "topic": "🎞️ Animação 2D/3D e motion graphics", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎵│musica", "topic": "🎧 Produção musical e composição", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "✍️│escrita", "topic": "📝 Poesia, contos, roteiros", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💻│design", "topic": "🖋️ Design gráfico e UI/UX", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏗️│3d", "topic": "🔄 Modelagem 3D e renderização", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💡│feedback", "topic": "👁️‍🗨️ Peça e dê feedback construtivo", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🤝│colabs", "topic": "👥 Projetos colaborativos", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💰│comissions", "topic": "💸 Informações sobre comissions", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📚│recursos", "topic": "📖 Tutoriais, brushes, referências", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│portfólio", "topic": "⭐ Mostre seu melhor trabalho!", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "☕│descontração", "topic": "🎮 Hora do café e inspiração", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "🎨│Sala de Arte", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎧│Foco Criativo", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "💭│Brainstorm", "user_limit": 8, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "👁️│Feedback Live", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎵│Ouvindo Música", "user_limit": 5, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "☕│Café Virtual", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "💤│AFK", "user_limit": 0, "permissions": {"everyone": ["connect"]}}
            ],
            "category": [
                {"name": "📢│INFORMAÇÕES", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "🎨│ÁREAS CRIATIVAS", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│COMUNIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎤│VOICE CHAT", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "🏆│PORTFÓLIO", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "👑│Fundador", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "🎨│Artista Sênior", "color": "purple", "permissions": ["manage_channels"], "hoist": True, "mentionable": True},
                {"name": "🛡️│Moderador", "color": "blue", "permissions": ["manage_messages"], "hoist": True, "mentionable": True}
            ],
            "community": [
                {"name": "🎭│Character Designer", "color": "pink", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🖥️│Digital Artist", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🖌️│Traditional Artist", "color": "orange", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "📷│Fotógrafo", "color": "teal", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎬│Animador", "color": "magenta", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎵│Músico", "color": "green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "✍️│Escritor", "color": "yellow", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "💻│Designer", "color": "red", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🏗️│3D Artist", "color": "dark_blue", "permissions": [], "hoist": False, "mentionable": False}
            ],
            "special": [
                {"name": "🤖│Bot", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎨│Artista", "color": "default", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": True,
            "music_bot": True,
            "moderation_bot": True
        }
    },
    
    # ========== TEMPLATE COMUNIDADE INTERNACIONAL ==========
    "comunidade": {
        "name": "🌍 Comunidade Global",
        "emoji": "🌍",
        "description": "Servidor para comunidades diversas com espaço para todos os interesses e culturas",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes da comunidade", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "📜│regras", "topic": "⚖️ Regras gerais da comunidade", "permissions": {"everyone": ["view_channel"], "staff": ["send_messages"]}},
                {"name": "👋│boas-vindas", "topic": "🎉 Seja bem-vindo! Conte sobre você", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos membros", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💬│geral", "topic": "💭 Conversas gerais", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│games", "topic": "🕹️ Jogos e entretenimento", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎬│filmes-series", "topic": "🎬 Filmes, séries e animes", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎵│musica", "topic": "🎧 Música e artistas", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "📚│livros", "topic": "📖 Livros e literatura", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💻│tecnologia", "topic": "🖥️ Tecnologia e inovação", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏃│esportes", "topic": "⚽ Esportes e atividades físicas", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🍳│culinária", "topic": "🍰 Receitas e culinária", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "✈️│viagens", "topic": "🗺️ Viagens e culturas", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎨│artes", "topic": "🖌️ Arte e criatividade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🤣│memes", "topic": "😂 Memes e humor", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "❓│ajuda", "topic": "🆘 Ajuda e suporte", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "💡│sugestões", "topic": "💭 Sugestões para a comunidade", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🏆│eventos", "topic": "🎉 Eventos e atividades", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ],
            "voice": [
                {"name": "💬│Sala Geral", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎮│Gaming Lounge", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎵│Music Room", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎬│Watch Party", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "☕│Café Virtual", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🎤│Karaokê", "user_limit": 10, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "🌍│Internacional", "user_limit": 0, "permissions": {"everyone": ["connect", "speak"]}},
                {"name": "💤│AFK", "user_limit": 0, "permissions": {"everyone": ["connect"]}}
            ],
            "category": [
                {"name": "📢│INFORMAÇÕES", "permissions": {"everyone": ["view_channel"], "staff": ["manage_channels"]}},
                {"name": "💬│COMUNIDADE", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎮│ENTRETENIMENTO", "permissions": {"everyone": ["view_channel", "send_messages"]}},
                {"name": "🎤│VOICE CHAT", "permissions": {"everyone": ["view_channel", "connect"]}},
                {"name": "🌍│INTERNACIONAL", "permissions": {"everyone": ["view_channel", "send_messages"]}}
            ]
        },
        "roles": {
            "staff": [
                {"name": "👑│Fundador", "color": "gold", "permissions": ["administrator"], "hoist": True, "mentionable": True},
                {"name": "⚡│Co-Fundador", "color": "purple", "permissions": ["manage_guild", "manage_channels"], "hoist": True, "mentionable": True},
                {"name": "🛡️│Administrador", "color": "red", "permissions": ["manage_guild", "manage_channels", "manage_roles"], "hoist": True, "mentionable": True},
                {"name": "⭐│Moderador", "color": "blue", "permissions": ["manage_messages", "kick_members"], "hoist": True, "mentionable": True}
            ],
            "community": [
                {"name": "🌟│VIP", "color": "orange", "permissions": ["priority_speaker"], "hoist": True, "mentionable": True},
                {"name": "🎮│Gamer", "color": "green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎨│Artista", "color": "pink", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "💻│Tech", "color": "cyan", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "📚│Leitor", "color": "teal", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🎵│Músico", "color": "magenta", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🏃│Esportista", "color": "dark_green", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🍳│Chef", "color": "yellow", "permissions": [], "hoist": False, "mentionable": False}
            ],
            "special": [
                {"name": "🤖│Bot", "color": "grey", "permissions": [], "hoist": False, "mentionable": False},
                {"name": "🌍│Membro", "color": "default", "permissions": [], "hoist": False, "mentionable": False}
            ]
        },
        "setup_options": {
            "verification": True,
            "welcome_channel": True,
            "ticket_system": True,
            "level_system": True,
            "music_bot": True,
            "moderation_bot": True
        }
    }
}

# Mapeamento de permissões Discord
PERMISSIONS_MAP = {
    "administrator": discord.Permissions.administrator,
    "manage_guild": discord.Permissions.manage_guild,
    "manage_channels": discord.Permissions.manage_channels,
    "manage_roles": discord.Permissions.manage_roles,
    "manage_messages": discord.Permissions.manage_messages,
    "kick_members": discord.Permissions.kick_members,
    "ban_members": discord.Permissions.ban_members,
    "mute_members": discord.Permissions.mute_members,
    "deafen_members": discord.Permissions.deafen_members,
    "priority_speaker": discord.Permissions.priority_speaker,
    "stream": discord.Permissions.stream,
    "view_channel": discord.Permissions.view_channel,
    "send_messages": discord.Permissions.send_messages,
    "connect": discord.Permissions.connect,
    "speak": discord.Permissions.speak,
}

# CORRIGIDO: Usar discord.Color (com C maiúsculo)
COLOR_MAP = {
    "gold": discord.Color.gold(),
    "red": discord.Color.red(),
    "blue": discord.Color.blue(),
    "green": discord.Color.green(),
    "purple": discord.Color.purple(),
    "orange": discord.Color.orange(),
    "pink": discord.Color.from_rgb(255, 182, 193),
    "teal": discord.Color.teal(),
    
    "magenta": discord.Color.from_rgb(255, 0, 255),
    "yellow": discord.Color.yellow(),
    "dark_red": discord.Color.from_rgb(139, 0, 0),
    "dark_green": discord.Color.from_rgb(0, 100, 0),
    "dark_blue": discord.Color.from_rgb(0, 0, 139),
    "light_blue": discord.Color.from_rgb(173, 216, 230),
    "grey": discord.Color.from_rgb(128, 128, 128),
    "default": discord.Color.default()
}

# ========== SISTEMA DE VERIFICAÇÃO ==========
class VerificationView(discord.ui.View):
    def __init__(self, bot, guild_id):
        super().__init__(timeout=None)
        self.bot = bot
        self.guild_id = guild_id

    @discord.ui.button(label="🔓 Verificar-se", style=discord.ButtonStyle.green, custom_id="verify_button")
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Verifica se o usuário já está verificado
        if str(interaction.user.id) in user_data.get(str(self.guild_id), {}):
            await interaction.response.send_message("✅ Você já está verificado!", ephemeral=True)
            return
        
        # Envia modal para verificação
        modal = VerificationModal(self.bot, self.guild_id)
        await interaction.response.send_modal(modal)

class VerificationModal(discord.ui.Modal, title="🔐 Verificação do Servidor"):
    def __init__(self, bot, guild_id):
        super().__init__()
        self.bot = bot
        self.guild_id = guild_id
    
    nome = discord.ui.TextInput(
        label="Seu Nome",
        placeholder="Digite seu nome ou apelido",
        max_length=30
    )
    
    idade = discord.ui.TextInput(
        label="Sua Idade",
        placeholder="Digite sua idade",
        max_length=2
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        # Valida a idade
        try:
            idade_int = int(self.idade.value)
            if idade_int < 13:
                await interaction.response.send_message(
                    "❌ Você precisa ter pelo menos 13 anos para usar o Discord.",
                    ephemeral=True
                )
                return
        except ValueError:
            await interaction.response.send_message(
                "❌ Por favor, digite uma idade válida.",
                ephemeral=True
            )
            return
        
        # Salva os dados do usuário
        guild_data = user_data.setdefault(str(self.guild_id), {})
        guild_data[str(interaction.user.id)] = {
            "nome": self.nome.value,
            "idade": idade_int,
            "verificado": True,
            "verificado_em": datetime.now().isoformat()
        }
        save_user_data()
        
        # Adiciona cargo de verificado se existir
        guild = self.bot.get_guild(self.guild_id)
        if guild:
            verified_role = discord.utils.get(guild.roles, name="✅│Verificado")
            if verified_role:
                try:
                    await interaction.user.add_roles(verified_role)
                except:
                    pass
        
        await interaction.response.send_message(
            f"✅ **Verificação concluída!**\n\n"
            f"**Nome:** {self.nome.value}\n"
            f"**Idade:** {idade_int} anos\n\n"
            f"Bem-vindo(a) ao servidor! 🎉",
            ephemeral=True
        )

# ========== COMANDO !template ==========
@bot.command(name="template")
async def mostrar_templates(ctx):
    """Mostra todos os templates disponíveis"""
    
    embed = discord.Embed(
        title="🎨 **TEMPLATES DISPONÍVEIS**",
        description="Escolha um template para configurar seu servidor:",
        color=0x5865F2
    )
    
    # Adicionar cada template
    for template_key, template_data in TEMPLATES.items():
        embed.add_field(
            name=f"{template_data['emoji']} **{template_data['name']}**",
            value=f"**ID:** `{template_key}`\n"
                  f"{template_data['description']}\n"
                  f"📊 **Canais:** {len(template_data['channels']['text'])} texto + {len(template_data['channels']['voice'])} voz\n"
                  f"👥 **Cargos:** {sum(len(roles) for roles in template_data['roles'].values())}\n"
                  f"📂 **Categorias:** {len(template_data['channels']['category'])}",
            inline=False
        )
    
    embed.add_field(
        name="🎯 **COMO USAR:**",
        value="Use `!setup [id_do_template]` para configurar\n"
              "Exemplo: `!setup gaming` para o template Gaming Universe",
        inline=False
    )
    
    await ctx.send(embed=embed)

# ========== SISTEMA DE SETUP PERSONALIZADO ==========
class SetupView(discord.ui.View):
    def __init__(self, bot, template_name, author_id):
        super().__init__(timeout=300)
        self.bot = bot
        self.template_name = template_name
        self.author_id = author_id
        self.selected_options = TEMPLATES[template_name]["setup_options"].copy()
    
    @discord.ui.button(label="✅ Sistema de Verificação", style=discord.ButtonStyle.secondary, row=0)
    async def toggle_verification(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.selected_options["verification"] = not self.selected_options["verification"]
        button.style = discord.ButtonStyle.green if self.selected_options["verification"] else discord.ButtonStyle.secondary
        await self.update_message(interaction)
    
    @discord.ui.button(label="👋 Canal de Boas-vindas", style=discord.ButtonStyle.green, row=0)
    async def toggle_welcome(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.selected_options["welcome_channel"] = not self.selected_options["welcome_channel"]
        button.style = discord.ButtonStyle.green if self.selected_options["welcome_channel"] else discord.ButtonStyle.secondary
        await self.update_message(interaction)
    
    @discord.ui.button(label="🎫 Sistema de Tickets", style=discord.ButtonStyle.secondary, row=1)
    async def toggle_tickets(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.selected_options["ticket_system"] = not self.selected_options["ticket_system"]
        button.style = discord.ButtonStyle.green if self.selected_options["ticket_system"] else discord.ButtonStyle.secondary
        await self.update_message(interaction)
    
    @discord.ui.button(label="📈 Sistema de Níveis", style=discord.ButtonStyle.secondary, row=1)
    async def toggle_levels(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.selected_options["level_system"] = not self.selected_options["level_system"]
        button.style = discord.ButtonStyle.green if self.selected_options["level_system"] else discord.ButtonStyle.secondary
        await self.update_message(interaction)
    
    @discord.ui.button(label="🔒 Canais Privados", style=discord.ButtonStyle.secondary, row=2)
    async def toggle_private(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.selected_options["private_channels"] = not self.selected_options["private_channels"]
        button.style = discord.ButtonStyle.green if self.selected_options["private_channels"] else discord.ButtonStyle.secondary
        await self.update_message(interaction)
    
    @discord.ui.button(label="🚀 Iniciar Setup", style=discord.ButtonStyle.primary, row=3)
    async def start_setup(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.author_id:
            await interaction.response.send_message("❌ Apenas quem iniciou o setup pode confirmar!", ephemeral=True)
            return
        
        await interaction.response.defer()
        await self.execute_setup(interaction)
    
    @discord.ui.button(label="❌ Cancelar", style=discord.ButtonStyle.danger, row=3)
    async def cancel_setup(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.author_id:
            await interaction.response.send_message("❌ Apenas quem iniciou o setup pode cancelar!", ephemeral=True)
            return
        
        await interaction.response.edit_message(
            content="❌ Setup cancelado!",
            embed=None,
            view=None
        )
        self.stop()
    
    async def update_message(self, interaction: discord.Interaction):
        template = TEMPLATES[self.template_name]
        
        embed = discord.Embed(
            title="⚙️ **CONFIGURAÇÃO PERSONALIZADA**",
            description=f"Template: **{template['name']}**\n\n"
                       "**Opções selecionadas:**\n",
            color=0x5865F2
        )
        
        options_text = ""
        for option, enabled in self.selected_options.items():
            emoji = "✅" if enabled else "❌"
            name = option.replace("_", " ").title()
            options_text += f"{emoji} **{name}**\n"
        
        embed.add_field(name="Configurações", value=options_text, inline=False)
        
        embed.add_field(
            name="📋 **O que será criado:**",
            value=f"• Categorias organizadas\n"
                  f"• Canais de texto e voz\n"
                  f"• Cargos com permissões\n"
                  f"• Sistema de verificação\n"
                  f"• Canais privados (se selecionado)",
            inline=False
        )
        
        await interaction.response.edit_message(embed=embed, view=self)
    
    async def execute_setup(self, interaction: discord.Interaction):
        template = TEMPLATES[self.template_name]
        guild = interaction.guild
        
        # Progress embed
        progress_embed = discord.Embed(
            title=f"⚙️ CONFIGURANDO: {template['name']}",
            description="⏳ Iniciando configuração...",
            color=0x5865F2
        )
        progress_msg = await interaction.followup.send(embed=progress_embed, wait=True)
        
        try:
            created_roles = {}
            created_categories = {}
            
            # 1. Criar cargos
            progress_embed.description += "\n\n🔧 **Criando cargos...**"
            await progress_msg.edit(embed=progress_embed)
            
            for role_type, roles_list in template["roles"].items():
                for role_data in roles_list:
                    # Calcular permissões
                    permissions = discord.Permissions()
                    for perm in role_data.get("permissions", []):
                        if perm in PERMISSIONS_MAP:
                            permissions.update(**{perm: True})
                    
                    # Criar cargo
                    role = await guild.create_role(
                        name=role_data["name"],
                        color=COLOR_MAP.get(role_data["color"], discord.Color.default()),
                        permissions=permissions,
                        hoist=role_data.get("hoist", False),
                        mentionable=role_data.get("mentionable", False)
                    )
                    created_roles[role_data["name"]] = role
                    await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ **Cargos criados!**"
            progress_embed.description += "\n\n🔧 **Criando categorias...**"
            await progress_msg.edit(embed=progress_embed)
            
            # 2. Criar categorias
            for i, category_data in enumerate(template["channels"]["category"]):
                # Configurar permissões da categoria
                overwrites = {}
                
                # Permissões para everyone
                if "everyone" in category_data["permissions"]:
                    everyone_perms = discord.Permissions()
                    for perm in category_data["permissions"]["everyone"]:
                        if perm in PERMISSIONS_MAP:
                            everyone_perms.update(**{perm: True})
                    overwrites[guild.default_role] = discord.PermissionOverwrite.from_pair(
                        everyone_perms, discord.Permissions.none()
                    )
                
                # Permissões para staff
                if "staff" in category_data["permissions"]:
                    staff_roles = [r for name, r in created_roles.items() if any(keyword in name.lower() for keyword in ["admin", "mod", "dono", "staff"])]
                    for staff_role in staff_roles:
                        staff_perms = discord.Permissions()
                        for perm in category_data["permissions"]["staff"]:
                            if perm in PERMISSIONS_MAP:
                                staff_perms.update(**{perm: True})
                        overwrites[staff_role] = discord.PermissionOverwrite.from_pair(
                            staff_perms, discord.Permissions.none()
                        )
                
                category = await guild.create_category(
                    name=category_data["name"],
                    overwrites=overwrites if overwrites else None,
                    position=i
                )
                created_categories[category_data["name"]] = category
                await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ **Categorias criadas!**"
            progress_embed.description += "\n\n🔧 **Criando canais de texto...**"
            await progress_msg.edit(embed=progress_embed)
            
            # 3. Criar canais de texto
            for channel_data in template["channels"]["text"]:
                # Determinar categoria
                category_name = "📢│INFORMAÇÕES"  # padrão
                if "geral" in channel_data["name"] or "chat" in channel_data["name"]:
                    category_name = "💬│COMUNIDADE"
                elif "games" in channel_data["name"] or "jogos" in channel_data["name"]:
                    category_name = "🎮│JOGOS"
                elif "estudo" in channel_data["name"] or "sala" in channel_data["name"]:
                    category_name = "📚│ÁREAS DE ESTUDO"
                elif "arte" in channel_data["name"] or "design" in channel_data["name"]:
                    category_name = "🎨│ÁREAS CRIATIVAS"
                
                category = created_categories.get(category_name, list(created_categories.values())[0])
                
                # Configurar permissões
                overwrites = {}
                
                if "permissions" in channel_data:
                    for role_type, perms in channel_data["permissions"].items():
                        if role_type == "everyone":
                            perms_obj = discord.Permissions()
                            for perm in perms:
                                if perm in PERMISSIONS_MAP:
                                    perms_obj.update(**{perm: True})
                            overwrites[guild.default_role] = discord.PermissionOverwrite.from_pair(
                                perms_obj, discord.Permissions.none()
                            )
                        elif role_type == "staff":
                            staff_roles = [r for name, r in created_roles.items() if any(keyword in name.lower() for keyword in ["admin", "mod", "staff"])]
                            for staff_role in staff_roles:
                                perms_obj = discord.Permissions()
                                for perm in perms:
                                    if perm in PERMISSIONS_MAP:
                                        perms_obj.update(**{perm: True})
                                overwrites[staff_role] = discord.PermissionOverwrite.from_pair(
                                    perms_obj, discord.Permissions.none()
                                )
                
                channel = await category.create_text_channel(
                    name=channel_data["name"],
                    topic=channel_data.get("topic", ""),
                    overwrites=overwrites if overwrites else None
                )
                await asyncio.sleep(0.3)
            
            progress_embed.description += "\n✅ **Canais de texto criados!**"
            progress_embed.description += "\n\n🔧 **Criando canais de voz...**"
            await progress_msg.edit(embed=progress_embed)
            
            # 4. Criar canais de voz
            for channel_data in template["channels"]["voice"]:
                # Determinar categoria
                category = created_categories.get("🎤│VOICE CHAT", list(created_categories.values())[-1])
                
                # Configurar permissões
                overwrites = {}
                
                if "permissions" in channel_data:
                    for role_type, perms in channel_data["permissions"].items():
                        if role_type == "everyone":
                            perms_obj = discord.Permissions()
                            for perm in perms:
                                if perm in PERMISSIONS_MAP:
                                    perms_obj.update(**{perm: True})
                            overwrites[guild.default_role] = discord.PermissionOverwrite.from_pair(
                                perms_obj, discord.Permissions.none()
                            )
                        elif role_type in ["vip", "staff", "competitive"]:
                            # Encontrar cargos correspondentes
                            target_roles = []
                            if role_type == "vip":
                                target_roles = [r for name, r in created_roles.items() if "vip" in name.lower()]
                            elif role_type == "staff":
                                target_roles = [r for name, r in created_roles.items() if any(keyword in name.lower() for keyword in ["admin", "mod", "staff"])]
                            elif role_type == "competitive":
                                target_roles = [r for name, r in created_roles.items() if "competitivo" in name.lower()]
                            
                            for target_role in target_roles:
                                perms_obj = discord.Permissions()
                                for perm in perms:
                                    if perm in PERMISSIONS_MAP:
                                        perms_obj.update(**{perm: True})
                                overwrites[target_role] = discord.PermissionOverwrite.from_pair(
                                    perms_obj, discord.Permissions.none()
                                )
                
                channel = await category.create_voice_channel(
                    name=channel_data["name"],
                    user_limit=channel_data.get("user_limit", 0),
                    overwrites=overwrites if overwrites else None
                )
                await asyncio.sleep(0.3)
            
            # 5. Configurar sistema de verificação se selecionado
            if self.selected_options["verification"]:
                progress_embed.description += "\n\n🔧 **Configurando sistema de verificação...**"
                await progress_msg.edit(embed=progress_embed)
                
                # Criar cargo de verificado
                verified_role = await guild.create_role(
                    name="✅│Verificado",
                    color=discord.Color.green(),
                    hoist=False
                )
                
                # Criar canal de verificação
                category = created_categories.get("📢│INFORMAÇÕES", list(created_categories.values())[0])
                verify_channel = await category.create_text_channel(
                    name="🔐│verificação",
                    topic="Verifique-se para acessar o servidor",
                    overwrites={
                        guild.default_role: discord.PermissionOverwrite(
                            view_channel=True,
                            send_messages=False
                        ),
                        verified_role: discord.PermissionOverwrite(
                            view_channel=True,
                            send_messages=True
                        )
                    }
                )
                
                # Enviar mensagem de verificação
                embed = discord.Embed(
                    title="🔐 **VERIFICAÇÃO DO SERVIDOR**",
                    description="Bem-vindo ao servidor! Para acessar todos os canais, "
                               "você precisa se verificar.\n\n"
                               "**Clique no botão abaixo para iniciar a verificação.**\n\n"
                               "📋 **Informações necessárias:**\n"
                               "• Seu nome/apelido\n"
                               "• Sua idade\n\n"
                               "⚠️ **Importante:**\n"
                               "• Você precisa ter pelo menos 13 anos\n"
                               "• Use informações verdadeiras",
                    color=0x5865F2
                )
                
                view = VerificationView(bot, guild.id)
                await verify_channel.send(embed=embed, view=view)
                
                # Salvar view persistentemente
                bot.add_view(view)
            
            # 6. Configurar canal de boas-vindas
            if self.selected_options["welcome_channel"]:
                progress_embed.description += "\n\n🔧 **Configurando canal de boas-vindas...**"
                await progress_msg.edit(embed=progress_embed)
                
                category = created_categories.get("📢│INFORMAÇÕES", list(created_categories.values())[0])
                welcome_channel = await category.create_text_channel(
                    name="👋│boas-vindas",
                    topic="Dê as boas-vindas aos novos membros!"
                )
                
                welcome_embed = discord.Embed(
                    title=f"🎉 **BEM-VINDO AO {guild.name.upper()}!**",
                    description=f"Seja muito bem-vindo ao nosso servidor! 🎊\n\n"
                               f"**Template usado:** {template['name']}\n"
                               f"**Emoji:** {template['emoji']}\n"
                               f"**Descrição:** {template['description']}\n\n"
                               f"📋 **Como começar:**\n"
                               f"1. Leia as regras\n"
                               f"2. Verifique-se no canal de verificação\n"
                               f"3. Apresente-se na comunidade!\n\n"
                               f"🎯 **Comandos úteis:**\n"
                               f"`!ajuda` - Mostra todos os comandos\n"
                               f"`!regras` - Mostra as regras\n"
                               f"`!info` - Informações do servidor",
                    color=discord.Color.green()
                )
                
                await welcome_channel.send(embed=welcome_embed)
            
            # 7. Setup completo
            progress_embed.title = "✅ **SETUP COMPLETO!**"
            progress_embed.description = (
                f"**Servidor configurado com sucesso!** 🎉\n\n"
                f"**Template:** {template['name']}\n"
                f"**Categorias criadas:** {len(created_categories)}\n"
                f"**Cargos criados:** {len(created_roles)}\n"
                f"**Canais criados:** {len(template['channels']['text']) + len(template['channels']['voice'])}\n\n"
                f"✨ **Funcionalidades ativas:**\n"
            )
            
            for option, enabled in self.selected_options.items():
                if enabled:
                    name = option.replace("_", " ").title()
                    progress_embed.description += f"• {name}\n"
            
            progress_embed.description += "\n🎯 **Próximos passos:**\n"
            progress_embed.description += "1. Configure os administradores nos cargos staff\n"
            progress_embed.description += "2. Personalize as permissões conforme necessário\n"
            progress_embed.description += "3. Adicione bots adicionais (música, moderação)\n"
            progress_embed.description += "4. Convide seus amigos!"
            
            progress_embed.color = discord.Color.green()
            
            await progress_msg.edit(embed=progress_embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO NO SETUP**",
                description=f"Ocorreu um erro durante o setup:\n```{str(e)}```\n\n"
                           "Por favor, verifique as permissões do bot e tente novamente.",
                color=discord.Color.red()
            )
            await interaction.followup.send(embed=error_embed)

# ========== EVENTOS ==========
@bot.event
async def on_ready():
    print('=' * 50)
    print(f'✅ BOT ONLINE: {bot.user}')
    print(f'🆔 ID: {bot.user.id}')
    print(f'📊 CONECTADO EM {len(bot.guilds)} SERVIDORES:')
    
    for guild in bot.guilds:
        print(f'   • {guild.name} (ID: {guild.id}, Membros: {guild.member_count})')
    
    print('=' * 50)
    print('🎮 COMANDOS DISPONÍVEIS:')
    print('   !template - Mostra todos os templates disponíveis')
    print('   !setup    - Configuração do servidor')
    print('   !verificar - Sistema de verificação')
    print('   !criarcanal - Cria canais privados')
    print('   !criarcargo - Cria cargos com permissões')
    print('   !ajuda     - Ajuda completa')
    print('=' * 50)
    
    # Status do bot
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servidores | !ajuda"
        ),
        status=discord.Status.online
    )

@bot.event
async def on_member_join(member):
    """Envia mensagem de boas-vindas quando um membro entra"""
    # Verifica se o servidor tem canal de boas-vindas
    welcome_channel = discord.utils.get(member.guild.text_channels, name="👋│boas-vindas")
    
    if welcome_channel:
        embed = discord.Embed(
            title=f"🎉 **BEM-VINDO(A), {member.name}!**",
            description=f"Seja muito bem-vindo(a) ao **{member.guild.name}**! 🎊\n\n"
                       f"👤 **Membro:** {member.mention}\n"
                       f"📅 **Entrou em:** <t:{int(datetime.now().timestamp())}:D>\n"
                       f"👥 **Total de membros:** {member.guild.member_count}\n\n"
                       f"📋 **Para começar:**\n"
                       f"1. Leia as regras\n"
                       f"2. Verifique-se no canal de verificação\n"
                       f"3. Apresente-se para a comunidade!",
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        
        embed.set_footer(text=f"ID: {member.id}")
        
        await welcome_channel.send(embed=embed)

# ========== COMANDOS ==========
@bot.command(name="setup")
@commands.has_permissions(administrator=True)
async def setup_command(ctx, template="gaming"):
    """Configuração completa do servidor com opções personalizadas"""
    
    if template not in TEMPLATES:
        # Mostrar templates disponíveis
        embed = discord.Embed(
            title="❌ Template não encontrado",
            description=f"**Templates disponíveis:**\n" + 
                       "\n".join([f"• **{key}** - {data['name']}" 
                                 for key, data in TEMPLATES.items()]),
            color=discord.Color.red()
        )
        embed.set_footer(text="Use !template para ver todos os templates detalhados")
        await ctx.send(embed=embed)
        return
    
    template_data = TEMPLATES[template]
    
    embed = discord.Embed(
        title="⚙️ **SETUP PERSONALIZADO DO SERVIDOR**",
        description=f"Template: **{template_data['name']}**\n\n"
                   "Configure o servidor selecionando as opções desejadas:\n\n"
                   "✅ **Opções disponíveis:**\n"
                   "• Sistema de verificação\n"
                   "• Canal de boas-vindas\n"
                   "• Sistema de tickets\n"
                   "• Sistema de níveis\n"
                   "• Canais privados\n\n"
                   "🔧 **Clique nos botões para ativar/desativar**\n"
                   "Depois clique em **Iniciar Setup**",
        color=0x5865F2
    )
    
    view = SetupView(bot, template, ctx.author.id)
    await ctx.send(embed=embed, view=view)

@bot.command(name="criarcanal")
@commands.has_permissions(manage_channels=True)
async def criar_canal(ctx, tipo: str, *, nome: str):
    """Cria um canal com permissões personalizadas"""
    
    tipos_validos = ["texto", "voz", "privado", "staff", "vip"]
    tipo = tipo.lower()
    
    if tipo not in tipos_validos:
        embed = discord.Embed(
            title="❌ Tipo inválido",
            description=f"**Tipos disponíveis:**\n" + 
                       "\n".join([f"• **{t}**" for t in tipos_validos]),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return
    
    # Configurar permissões baseadas no tipo
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(
            view_channel=True if tipo == "texto" else False,
            send_messages=True if tipo == "texto" else False,
            connect=True if tipo == "voz" else False,
            speak=True if tipo == "voz" else False
        )
    }
    
    if tipo == "privado":
        overwrites[ctx.guild.default_role] = discord.PermissionOverwrite(view_channel=False)
        # Adicionar permissão para o autor
        overwrites[ctx.author] = discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            manage_channels=True
        )
    
    elif tipo == "staff":
        # Encontrar cargos de staff
        staff_roles = []
        for role in ctx.guild.roles:
            if any(keyword in role.name.lower() for keyword in ["admin", "mod", "staff", "dono"]):
                staff_roles.append(role)
        
        if not staff_roles:
            staff_roles = [ctx.guild.roles[-1]]  # Usar o cargo mais alto
        
        overwrites[ctx.guild.default_role] = discord.PermissionOverwrite(view_channel=False)
        for role in staff_roles:
            overwrites[role] = discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                connect=True,
                speak=True
            )
    
    elif tipo == "vip":
        # Encontrar cargos VIP
        vip_roles = [role for role in ctx.guild.roles if "vip" in role.name.lower()]
        
        if not vip_roles:
            await ctx.send("❌ Nenhum cargo VIP encontrado. Crie um cargo VIP primeiro.")
            return
        
        overwrites[ctx.guild.default_role] = discord.PermissionOverwrite(view_channel=True, connect=False)
        for role in vip_roles:
            overwrites[role] = discord.PermissionOverwrite(
                view_channel=True,
                connect=True,
                speak=True
            )
    
    try:
        if tipo in ["texto", "privado", "staff"]:
            channel = await ctx.guild.create_text_channel(
                name=nome,
                overwrites=overwrites,
                category=ctx.channel.category
            )
            tipo_nome = "📝 Canal de texto"
        
        else:  # voz, vip
            channel = await ctx.guild.create_voice_channel(
                name=nome,
                overwrites=overwrites,
                category=ctx.channel.category,
                user_limit=0
            )
            tipo_nome = "🎤 Canal de voz"
        
        embed = discord.Embed(
            title="✅ **CANAL CRIADO**",
            description=f"Canal **{tipo_nome}** criado com sucesso!",
            color=discord.Color.green()
        )
        
        embed.add_field(name="📝 Nome", value=channel.mention, inline=True)
        embed.add_field(name="🎯 Tipo", value=tipo_nome, inline=True)
        embed.add_field(name="🔐 Acesso", value="Privado" if tipo in ["privado", "staff", "vip"] else "Público", inline=True)
        
        if tipo in ["staff", "vip"]:
            allowed_roles = [role for role in overwrites.keys() if isinstance(role, discord.Role) and role != ctx.guild.default_role]
            if allowed_roles:
                embed.add_field(name="👥 Permitido para", value=", ".join([r.mention for r in allowed_roles]), inline=False)
        
        await ctx.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="❌ **ERRO AO CRIAR CANAL**",
            description=f"```{str(e)}```",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@bot.command(name="criarcargo")
@commands.has_permissions(manage_roles=True)
async def criar_cargo(ctx, tipo: str, *, nome: str):
    """Cria um cargo com permissões específicas"""
    
    tipos_validos = ["admin", "mod", "vip", "membro", "bot", "custom"]
    
    if tipo not in tipos_validos:
        embed = discord.Embed(
            title="❌ Tipo inválido",
            description=f"**Tipos disponíveis:**\n" + 
                       "\n".join([f"• **{t}**" for t in tipos_validos]),
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return
    
    # Configurar permissões baseadas no tipo
    permissions = discord.Permissions()
    
    if tipo == "admin":
        permissions.administrator = True
        color = discord.Color.red()
        hoist = True
        mentionable = True
    
    elif tipo == "mod":
        permissions.update(
            manage_messages=True,
            kick_members=True,
            ban_members=True,
            mute_members=True,
            deafen_members=True,
            manage_channels=True
        )
        color = discord.Color.blue()
        hoist = True
        mentionable = True
    
    elif tipo == "vip":
        permissions.update(
            priority_speaker=True,
            stream=True,
            attach_files=True,
            embed_links=True
        )
        color = discord.Color.gold()
        hoist = True
        mentionable = True
    
    elif tipo == "bot":
        permissions.update(
            send_messages=True,
            embed_links=True,
            attach_files=True,
            read_message_history=True
        )
        color = discord.Color.teal()
        hoist = False
        mentionable = False
    
    else:  # membro ou custom
        color = discord.Color.default()
        hoist = False
        mentionable = False
    
    try:
        role = await ctx.guild.create_role(
            name=nome,
            color=color,
            permissions=permissions,
            hoist=hoist,
            mentionable=mentionable
        )
        
        embed = discord.Embed(
            title="✅ **CARGO CRIADO**",
            description=f"Cargo **{nome}** criado com sucesso!",
            color=color
        )
        
        embed.add_field(name="🆔 ID", value=role.id, inline=True)
        embed.add_field(name="🎯 Tipo", value=tipo.title(), inline=True)
        embed.add_field(name="👑 Posição", value=role.position, inline=True)
        
        # Listar permissões principais
        if permissions.administrator:
            perms_text = "Administrador (Todas as permissões)"
        else:
            perms_list = []
            for perm, value in permissions:
                if value and perm in [
                    'manage_guild', 'manage_channels', 'manage_roles',
                    'manage_messages', 'kick_members', 'ban_members'
                ]:
                    perms_list.append(perm.replace('_', ' ').title())
            
            perms_text = ", ".join(perms_list) if perms_list else "Permissões básicas"
        
        embed.add_field(name="🔐 Permissões", value=perms_text, inline=False)
        embed.set_footer(text=f"Criado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="❌ **ERRO AO CRIAR CARGO**",
            description=f"```{str(e)}```",
            color=discord.Color.red()
        )
        await ctx.send(embed=error_embed)

@bot.command(name="verificar")
@commands.has_permissions(manage_guild=True)
async def setup_verificacao(ctx):
    """Configura o sistema de verificação no servidor"""
    
    # Verificar se já existe cargo de verificado
    verified_role = discord.utils.get(ctx.guild.roles, name="✅│Verificado")
    if not verified_role:
        verified_role = await ctx.guild.create_role(
            name="✅│Verificado",
            color=discord.Color.green(),
            hoist=False
        )
    
    # Criar/Encontrar categoria de informações
    info_category = discord.utils.get(ctx.guild.categories, name="📢│INFORMAÇÕES")
    if not info_category:
        info_category = await ctx.guild.create_category("📢│INFORMAÇÕES")
    
    # Criar canal de verificação
    verify_channel = discord.utils.get(ctx.guild.text_channels, name="🔐│verificação")
    if not verify_channel:
        verify_channel = await info_category.create_text_channel(
            name="🔐│verificação",
            topic="Verifique-se para acessar o servidor",
            overwrites={
                ctx.guild.default_role: discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=False
                ),
                verified_role: discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True
                )
            }
        )
    
    # Enviar mensagem de verificação
    embed = discord.Embed(
        title="🔐 **SISTEMA DE VERIFICAÇÃO**",
        description="Bem-vindo ao sistema de verificação!\n\n"
                   "**Para acessar todos os canais do servidor, você precisa se verificar.**\n\n"
                   "📋 **O que será solicitado:**\n"
                   "• Seu nome ou apelido\n"
                   "• Sua idade\n\n"
                   "⚠️ **Importante:**\n"
                   "• Idade mínima: 13 anos\n"
                   "• Use informações verdadeiras\n"
                   "• Seus dados são armazenados apenas neste servidor\n\n"
                   "🔒 **Privacidade:**\n"
                   "Seus dados são usados apenas para verificação de idade\n"
                   "e não são compartilhados com terceiros.",
        color=0x5865F2
    )
    
    embed.set_footer(text="Clique no botão abaixo para começar")
    
    view = VerificationView(bot, ctx.guild.id)
    await verify_channel.send(embed=embed, view=view)
    
    # Salvar view persistentemente
    bot.add_view(view)
    
    embed_success = discord.Embed(
        title="✅ **SISTEMA DE VERIFICAÇÃO CONFIGURADO**",
        description=f"Sistema de verificação configurado com sucesso!\n\n"
                   f"**Canal:** {verify_channel.mention}\n"
                   f"**Cargo:** {verified_role.mention}\n\n"
                   f"Novos membros precisarão se verificar para acessar o servidor.",
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed_success)

@bot.command(name="verificados")
@commands.has_permissions(manage_guild=True)
async def listar_verificados(ctx):
    """Lista todos os membros verificados"""
    
    verified_role = discord.utils.get(ctx.guild.roles, name="✅│Verificado")
    if not verified_role:
        await ctx.send("❌ Cargo de verificado não encontrado. Use `!verificar` para configurar.")
        return
    
    verified_members = [member for member in ctx.guild.members if verified_role in member.roles]
    
    if not verified_members:
        await ctx.send("ℹ️ Nenhum membro verificado ainda.")
        return
    
    embed = discord.Embed(
        title="📋 **MEMBROS VERIFICADOS**",
        description=f"Total: {len(verified_members)} membros\n\n",
        color=discord.Color.green()
    )
    
    # Paginação se houver muitos membros
    members_text = ""
    for i, member in enumerate(verified_members[:20], 1):
        user_data_entry = user_data.get(str(ctx.guild.id), {}).get(str(member.id), {})
        nome = user_data_entry.get("nome", "Não informado")
        idade = user_data_entry.get("idade", "Não informada")
        
        members_text += f"**{i}. {member.name}**\n"
        members_text += f"   👤 Nome: {nome}\n"
        members_text += f"   🎂 Idade: {idade} anos\n"
        members_text += f"   🆔 ID: {member.id}\n\n"
    
    embed.add_field(name="Lista de Verificados", value=members_text, inline=False)
    
    if len(verified_members) > 20:
        embed.set_footer(text=f"Mostrando 20 de {len(verified_members)} verificados")
    
    await ctx.send(embed=embed)

@bot.command(name="minhainfo")
async def minha_info(ctx):
    """Mostra suas informações de verificação"""
    
    user_id = str(ctx.author.id)
    guild_id = str(ctx.guild.id)
    
    if guild_id in user_data and user_id in user_data[guild_id]:
        data = user_data[guild_id][user_id]
        
        embed = discord.Embed(
            title="📋 **SUAS INFORMAÇÕES**",
            color=discord.Color.blue()
        )
        
        embed.add_field(name="👤 Nome", value=data["nome"], inline=True)
        embed.add_field(name="🎂 Idade", value=f"{data['idade']} anos", inline=True)
        
        verified_date = datetime.fromisoformat(data["verificado_em"])
        embed.add_field(name="📅 Verificado em", value=verified_date.strftime("%d/%m/%Y %H:%M"), inline=True)
        
        verified_role = discord.utils.get(ctx.guild.roles, name="✅│Verificado")
        if verified_role and verified_role in ctx.author.roles:
            status = "✅ Verificado"
        else:
            status = "❌ Não verificado"
        
        embed.add_field(name="🔐 Status", value=status, inline=True)
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Você ainda não se verificou. Use o sistema de verificação do servidor.")

@bot.command(name="configurar")
@commands.has_permissions(administrator=True)
async def configurar_servidor(ctx):
    """Menu de configuração do servidor"""
    
    embed = discord.Embed(
        title="⚙️ **CONFIGURAÇÃO DO SERVIDOR**",
        description="Escolha o que deseja configurar:",
        color=0x5865F2
    )
    
    embed.add_field(
        name="🔐 Sistema de Verificação",
        value="`!verificar` - Configura verificação de membros",
        inline=False
    )
    
    embed.add_field(
        name="🎭 Cargos e Permissões",
        value="`!criarcargo [tipo] [nome]` - Cria cargos com permissões",
        inline=False
    )
    
    embed.add_field(
        name="💬 Canais Especiais",
        value="`!criarcanal [tipo] [nome]` - Cria canais privados/VIP",
        inline=False
    )
    
    embed.add_field(
        name="🚀 Setup Completo",
        value="`!setup [template]` - Configuração automática completa\n"
              "`!template` - Mostra todos os templates disponíveis",
        inline=False
    )
    
    embed.add_field(
        name="📊 Gerenciar Verificados",
        value="`!verificados` - Lista membros verificados",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name="ajuda")
async def ajuda_completa(ctx):
    """Mostra todos os comandos disponíveis"""
    
    embed = discord.Embed(
        title="🤖 **BOT DE ORGANIZAÇÃO COMPLETO**",
        description="**Versão:** 2.0.0 | **Prefixo:** `!`\n\n"
                   "Um bot completo para organização automática de servidores Discord",
        color=0x5865F2
    )
    
    embed.add_field(
        name="🎯 **TEMPLATES & SETUP**",
        value="```"
              "!template        - Mostra todos os templates\n"
              "!setup [template]- Configura servidor completo\n"
              "!configurar      - Menu de configuração\n"
              "```",
        inline=False
    )
    
    embed.add_field(
        name="🔐 **VERIFICAÇÃO**",
        value="```"
              "!verificar       - Sistema de verificação\n"
              "!verificados     - Lista verificados\n"
              "!minhainfo       - Suas informações\n"
              "```",
        inline=True
    )
    
    embed.add_field(
        name="👑 **GERENCIAR**",
        value="```"
              "!criarcargo [tipo] [nome]  - Cria cargos\n"
              "!criarcanal [tipo] [nome]  - Cria canais\n"
              "```",
        inline=True
    )
    
    embed.add_field(
        name="📊 **INFORMAÇÕES**",
        value="```"
              "!serverinfo     - Info do servidor\n"
              "!userinfo       - Info de usuário\n"
              "!ping           - Testa latência\n"
              "```",
        inline=False
    )
    
    embed.add_field(
        name="🎨 **TEMPLATES DISPONÍVEIS**",
        value="• **gaming** - Servidor de jogos 🎮\n"
              "• **estudo** - Academia de estudos 📚\n"
              "• **streamer** - Streamer profissional 🎥\n"
              "• **empresa** - Corporativo 💼\n"
              "• **artes** - Comunidade criativa 🎨\n"
              "• **comunidade** - Comunidade geral 🌍",
        inline=False
    )
    
    embed.set_footer(text="Use !template para ver detalhes de cada template")
    
    await ctx.send(embed=embed)

@bot.command(name="serverinfo")
async def server_info(ctx):
    """Informações detalhadas do servidor"""
    
    guild = ctx.guild
    
    # Contar canais por tipo
    text_channels = len(guild.text_channels)
    voice_channels = len(guild.voice_channels)
    categories = len(guild.categories)
    
    # Verificar sistemas ativos
    verified_role = discord.utils.get(guild.roles, name="✅│Verificado")
    has_verification = verified_role is not None
    
    vip_roles = [role for role in guild.roles if "vip" in role.name.lower()]
    has_vip = len(vip_roles) > 0
    
    staff_roles = [role for role in guild.roles if any(keyword in role.name.lower() for keyword in ["admin", "mod", "staff"])]
    has_staff = len(staff_roles) > 0
    
    embed = discord.Embed(
        title=f"📊 **{guild.name}**",
        description=guild.description or "Sem descrição",
        color=0x5865F2,
        timestamp=datetime.now()
    )
    
    embed.add_field(name="👑 Dono", value=guild.owner.mention, inline=True)
    embed.add_field(name="📅 Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="🌍 Região", value=str(guild.preferred_locale).title(), inline=True)
    
    embed.add_field(name="👥 Membros", value=f"{guild.member_count}", inline=True)
    embed.add_field(name="💬 Canais", value=f"{text_channels} texto + {voice_channels} voz", inline=True)
    embed.add_field(name="📂 Categorias", value=f"{categories}", inline=True)
    
    embed.add_field(name="👑 Cargos", value=f"{len(guild.roles)}", inline=True)
    embed.add_field(name="🎨 Emojis", value=f"{len(guild.emojis)}", inline=True)
    embed.add_field(name="🚀 Boosts", value=f"{guild.premium_subscription_count}", inline=True)
    
    # Sistemas ativos
    systems = []
    if has_verification:
        systems.append("🔐 Verificação")
    if has_vip:
        systems.append("🌟 VIP")
    if has_staff:
        systems.append("🛡️ Staff")
    
    if systems:
        embed.add_field(name="⚙️ Sistemas Ativos", value="\n".join(systems), inline=False)
    
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    
    embed.set_footer(text=f"ID: {guild.id}")
    
    await ctx.send(embed=embed)

@bot.command(name="userinfo")
async def user_info(ctx, member: discord.Member = None):
    """Informações de um usuário"""
    
    member = member or ctx.author
    
    # Verificar se está verificado
    user_id = str(member.id)
    guild_id = str(ctx.guild.id)
    is_verified = False
    user_info = {}
    
    if guild_id in user_data and user_id in user_data[guild_id]:
        is_verified = True
        user_info = user_data[guild_id][user_id]
    
    embed = discord.Embed(
        title=f"👤 **{member.display_name}**",
        color=member.color if member.color.value != 0 else 0x5865F2,
        timestamp=datetime.now()
    )
    
    embed.add_field(name="📝 Nome", value=member.name, inline=True)
    embed.add_field(name="#️⃣ Tag", value=member.discriminator, inline=True)
    embed.add_field(name="🆔 ID", value=member.id, inline=True)
    
    embed.add_field(name="📅 Criado em", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="📅 Entrou em", value=member.joined_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="🤖 Bot", value="Sim" if member.bot else "Não", inline=True)
    
    # Informações de verificação
    if is_verified:
        embed.add_field(name="🔐 Verificado", value="✅ Sim", inline=True)
        embed.add_field(name="👤 Nome registrado", value=user_info.get("nome", "N/A"), inline=True)
        embed.add_field(name="🎂 Idade", value=f"{user_info.get('idade', 'N/A')} anos", inline=True)
    else:
        embed.add_field(name="🔐 Verificado", value="❌ Não", inline=True)
    
    # Cargos (exceto @everyone)
    roles = [role.mention for role in member.roles[1:]]
    if roles:
        roles_text = ", ".join(roles[:5])
        if len(roles) > 5:
            roles_text += f" e mais {len(roles) - 5}"
        embed.add_field(name=f"🎖️ Cargos ({len(roles)})", value=roles_text, inline=False)
    
    if member.avatar:
        embed.set_thumbnail(url=member.avatar.url)
    
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    
    await ctx.send(embed=embed)

@bot.command(name="ping")
async def ping_command(ctx):
    """Testa a latência do bot"""
    latency = round(bot.latency * 1000)
    
    if latency < 100:
        color = discord.Color.green()
        status = "✅ Excelente"
    elif latency < 200:
        color = discord.Color.orange()
        status = "⚠️ Bom"
    else:
        color = discord.Color.red()
        status = "❌ Lento"
    
    embed = discord.Embed(
        title="🏓 **PONG!**",
        description=f"**Status:** {status}",
        color=color
    )
    embed.add_field(name="📡 **Latência**", value=f"`{latency}ms`", inline=True)
    embed.add_field(name="🤖 **Bot**", value=bot.user.name, inline=True)
    embed.set_footer(text=f"Solicitado por {ctx.author.name}")
    
    await ctx.send(embed=embed)

# ========== INICIAR BOT ==========
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 **BOT DE ORGANIZAÇÃO COMPLETO DISCORD**")
    print("=" * 50)
    print("📋 Verificando configurações...")
    
    if TOKEN == "seu_token_aqui" or not TOKEN:
        print("❌ ERRO: Token não configurado!")
        print("👉 Edite o arquivo .env e coloque seu token real")
        print("   Formato: DISCORD_TOKEN=seu_token_aqui")
        exit()
    
    print("✅ Token encontrado")
    print("📂 Carregando dados dos usuários...")
    print(f"📊 {len(user_data)} servidores com dados salvos")
    print("🔗 Conectando ao Discord...")
    print("=" * 50)
    
    try:
        bot.run(TOKEN, reconnect=True)
    except discord.LoginFailure:
        print("❌ ERRO: Token inválido!")
        print("👉 Verifique se o token no arquivo .env está correto")
    except discord.PrivilegedIntentsRequired:
        print("❌ ERRO: Intents privilegiados necessários!")
        print("👉 Ative os intents no portal do desenvolvedor Discord:")
        print("   - Presence Intent")
        print("   - Server Members Intent")
        print("   - Message Content Intent")
    except Exception as e:
        print(f"❌ ERRO: {type(e).__name__}: {e}")
    finally:
        print("=" * 50)
        print("💾 Salvando dados dos usuários...")
        save_user_data()
        print("👋 Bot finalizado")