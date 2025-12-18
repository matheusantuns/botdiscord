"""
COMANDOS UTILITÁRIOS COMPLETOS
"""

import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import platform
import psutil
import time

class UtilCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()
    
    @commands.command(name="ajuda", aliases=["help", "comandos"])
    async def mostrar_ajuda(self, ctx, categoria=None):
        """
        Mostra todos os comandos disponíveis
        Uso: !ajuda [categoria]
        Categorias: setup, admin, util, todos
        """
        
        if categoria and categoria.lower() == "setup":
            embed = self._criar_embed_setup()
        elif categoria and categoria.lower() == "admin":
            embed = self._criar_embed_admin()
        elif categoria and categoria.lower() == "util":
            embed = self._criar_embed_util()
        else:
            embed = self._criar_embed_principal()
        
        embed.set_footer(text=f"Solicitado por {ctx.author.name} • Digite !ajuda [categoria] para mais detalhes")
        
        await ctx.send(embed=embed)
    
    def _criar_embed_principal(self):
        embed = discord.Embed(
            title="🤖 **BOT DE ORGANIZAÇÃO PROFISSIONAL**",
            description="Um bot completo para organização automática de servidores Discord\n"
                       "**Versão:** 2.0.0 • **Prefixo:** `!`",
            color=0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(
            name="🎯 **SETUP & TEMPLATES**",
            value="```"
                  "!setup       - Configura servidor com template\n"
                  "!templates   - Mostra todos templates\n"
                  "!organizar   - Organiza canais automaticamente\n"
                  "!preview     - Prévia de um template\n"
                  "```",
            inline=False
        )
        
        embed.add_field(
            name="🛠️ **ADMINISTRAÇÃO**",
            value="```"
                  "!limpar      - Limpa mensagens\n"
                  "!criarcanal  - Cria novo canal\n"
                  "!criarcargo  - Cria novo cargo\n"
                  "!ban         - Bane um membro\n"
                  "!kick        - Expulsa um membro\n"
                  "!mute        - Silencia um membro\n"
                  "```",
            inline=True
        )
        
        embed.add_field(
            name="📊 **UTILITÁRIOS**",
            value="```"
                  "!serverinfo  - Info do servidor\n"
                  "!userinfo    - Info do usuário\n"
                  "!ping        - Testa latência\n"
                  "!botinfo     - Info do bot\n"
                  "!convite     - Link para convidar\n"
                  "!avatar      - Avatar do usuário\n"
                  "```",
            inline=True
        )
        
        embed.add_field(
            name="📁 **TEMPLATES DISPONÍVEIS**",
            value="• **gaming** - Servidor de jogos\n"
                  "• **estudo** - Servidor de estudos\n"
                  "• **streamer** - Para streamers\n"
                  "• **empresa** - Corporativo\n"
                  "• **comunidade** - Comunidade geral\n"
                  "• **artes** - Para criativos",
            inline=False
        )
        
        return embed
    
    def _criar_embed_setup(self):
        embed = discord.Embed(
            title="🎯 **COMANDOS DE SETUP**",
            description="Comandos para configuração automática do servidor",
            color=0x5865F2
        )
        
        embed.add_field(
            name="!setup [template]",
            value="**Descrição:** Configura o servidor com um template específico\n"
                  "**Uso:** `!setup gaming` ou `!setup estudo`\n"
                  "**Permissão:** Administrador\n"
                  "**Templates:** gaming, estudo, streamer, empresa, comunidade, artes",
            inline=False
        )
        
        embed.add_field(
            name="!templates",
            value="**Descrição:** Mostra todos os templates disponíveis com detalhes\n"
                  "**Uso:** `!templates`",
            inline=False
        )
        
        embed.add_field(
            name="!organizar",
            value="**Descrição:** Organiza canais em categorias automaticamente\n"
                  "**Uso:** `!organizar`\n"
                  "**Permissão:** Administrador",
            inline=False
        )
        
        embed.add_field(
            name="!preview [template]",
            value="**Descrição:** Mostra uma prévia do template antes de aplicar\n"
                  "**Uso:** `!preview gaming`",
            inline=False
        )
        
        return embed
    
    def _criar_embed_admin(self):
        embed = discord.Embed(
            title="🛠️ **COMANDOS ADMINISTRATIVOS**",
            description="Comandos para administração do servidor",
            color=0xED4245
        )
        
        embed.add_field(
            name="!limpar [quantidade]",
            value="**Descrição:** Limpa mensagens do canal\n"
                  "**Uso:** `!limpar 10` (padrão: 10, máximo: 100)\n"
                  "**Permissão:** Gerenciar Mensagens",
            inline=False
        )
        
        embed.add_field(
            name="!criarcanal [tipo] [nome]",
            value="**Descrição:** Cria um novo canal\n"
                  "**Uso:** `!criarcanal texto geral` ou `!criarcanal voz chat`\n"
                  "**Tipos:** texto, voz, anuncios\n"
                  "**Permissão:** Gerenciar Canais",
            inline=False
        )
        
        embed.add_field(
            name="!criarcargo [nome]",
            value="**Descrição:** Cria um novo cargo\n"
                  "**Uso:** `!criarcargo Moderador`\n"
                  "**Permissão:** Gerenciar Cargos",
            inline=False
        )
        
        embed.add_field(
            name="!ban [@membro] [motivo]",
            value="**Descrição:** Bane um membro do servidor\n"
                  "**Uso:** `!ban @usuário Spam`\n"
                  "**Permissão:** Banir Membros",
            inline=False
        )
        
        embed.add_field(
            name="!kick [@membro] [motivo]",
            value="**Descrição:** Expulsa um membro do servidor\n"
                  "**Uso:** `!kick @usuário Comportamento`\n"
                  "**Permissão:** Expulsar Membros",
            inline=False
        )
        
        embed.add_field(
            name="!mute [@membro] [minutos] [motivo]",
            value="**Descrição:** Silencia um membro por um período\n"
                  "**Uso:** `!mute @usuário 60 Spam` (60 minutos)\n"
                  "**Permissão:** Moderar Membros",
            inline=False
        )
        
        return embed
    
    def _criar_embed_util(self):
        embed = discord.Embed(
            title="📊 **COMANDOS UTILITÁRIOS**",
            description="Comandos de informação e utilidade",
            color=0x57F287
        )
        
        embed.add_field(
            name="!serverinfo",
            value="**Descrição:** Mostra informações detalhadas do servidor\n"
                  "**Uso:** `!serverinfo`",
            inline=False
        )
        
        embed.add_field(
            name="!userinfo [@usuário]",
            value="**Descrição:** Mostra informações de um usuário\n"
                  "**Uso:** `!userinfo` ou `!userinfo @usuário`",
            inline=False
        )
        
        embed.add_field(
            name="!ping",
            value="**Descrição:** Mostra a latência do bot\n"
                  "**Uso:** `!ping`",
            inline=False
        )
        
        embed.add_field(
            name="!botinfo",
            value="**Descrição:** Mostra informações sobre o bot\n"
                  "**Uso:** `!botinfo`",
            inline=False
        )
        
        embed.add_field(
            name="!convite",
            value="**Descrição:** Mostra o link para convidar o bot\n"
                  "**Uso:** `!convite`",
            inline=False
        )
        
        embed.add_field(
            name="!avatar [@usuário]",
            value="**Descrição:** Mostra o avatar de um usuário\n"
                  "**Uso:** `!avatar` ou `!avatar @usuário`",
            inline=False
        )
        
        return embed
    
    @commands.command(name="ping", aliases=["latencia", "latency"])
    async def testar_ping(self, ctx):
        """
        Testa a latência do bot
        Uso: !ping
        """
        
        # Latência da API
        api_latency = round(self.bot.latency * 1000)
        
        # Medição de tempo de resposta
        start_time = time.time()
        message = await ctx.send("🏓 **Calculando ping...**")
        end_time = time.time()
        
        response_time = round((end_time - start_time) * 1000)
        
        # Cores baseadas na latência
        if api_latency < 100:
            color = 0x57F287  # Verde
            status = "✅ Excelente"
        elif api_latency < 200:
            color = 0xFEE75C  # Amarelo
            status = "⚠️ Bom"
        elif api_latency < 400:
            color = 0xFEE75C  # Amarelo
            status = "⚠️ Aceitável"
        else:
            color = 0xED4245  # Vermelho
            status = "❌ Lento"
        
        embed = discord.Embed(
            title="🏓 **PONG!**",
            description=f"**Status:** {status}",
            color=color,
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="📡 **Latência da API**", value=f"`{api_latency}ms`", inline=True)
        embed.add_field(name="⚡ **Tempo de Resposta**", value=f"`{response_time}ms`", inline=True)
        embed.add_field(name="🤖 **Shard ID**", value=f"`{ctx.guild.shard_id if ctx.guild.shard_id else 0}`", inline=True)
        
        embed.set_footer(text=f"Solicitado por {ctx.author.name}")
        
        await message.edit(content="", embed=embed)
    
    @commands.command(name="serverinfo", aliases=["server", "sinfo"])
    async def informacoes_servidor(self, ctx):
        """
        Mostra informações detalhadas do servidor
        Uso: !serverinfo
        """
        
        guild = ctx.guild
        
        # Contagens
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        roles = len(guild.roles)
        emojis = len(guild.emojis)
        stickers = len(guild.stickers)
        
        # Níveis de verificação
        verification_levels = {
            discord.VerificationLevel.none: "Nenhuma",
            discord.VerificationLevel.low: "Baixo",
            discord.VerificationLevel.medium: "Médio",
            discord.VerificationLevel.high: "Alto",
            discord.VerificationLevel.highest: "Muito Alto"
        }
        
        # Filtro de conteúdo
        content_filters = {
            discord.ContentFilter.disabled: "Desativado",
            discord.ContentFilter.no_role: "Sem cargo",
            discord.ContentFilter.all_members: "Todos os membros"
        }
        
        embed = discord.Embed(
            title=f"📊 **{guild.name}**",
            description=guild.description or "Sem descrição",
            color=0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        # Informações básicas
        embed.add_field(
            name="👑 **DONO**",
            value=f"{guild.owner.mention}\n`{guild.owner}`",
            inline=True
        )
        
        embed.add_field(
            name="📅 **CRIADO EM**",
            value=f"<t:{int(guild.created_at.timestamp())}:D>\n(<t:{int(guild.created_at.timestamp())}:R>)",
            inline=True
        )
        
        embed.add_field(
            name="🌍 **REGIÃO**",
            value=str(guild.preferred_locale).title(),
            inline=True
        )
        
        # Estatísticas
        embed.add_field(
            name="👥 **MEMBROS**",
            value=f"**Total:** {guild.member_count}\n"
                  f"**Online:** {sum(1 for m in guild.members if m.status != discord.Status.offline)}",
            inline=True
        )
        
        embed.add_field(
            name="💬 **CANAIS**",
            value=f"**Categorias:** {categories}\n"
                  f"**Texto:** {text_channels}\n"
                  f"**Voz:** {voice_channels}",
            inline=True
        )
        
        embed.add_field(
            name="🎨 **RECURSOS**",
            value=f"**Cargos:** {roles}/250\n"
                  f"**Emojis:** {emojis}/50\n"
                  f"**Stickers:** {stickers}/15",
            inline=True
        )
        
        # Boost
        if guild.premium_subscription_count > 0:
            embed.add_field(
                name="🚀 **BOOSTS**",
                value=f"**Nível:** {guild.premium_tier}\n"
                      f"**Quantidade:** {guild.premium_subscription_count}",
                inline=True
            )
        
        # Configurações
        embed.add_field(
            name="⚙️ **CONFIGURAÇÕES**",
            value=f"**Verificação:** {verification_levels.get(guild.verification_level, 'Desconhecido')}\n"
                  f"**Filtro de Conteúdo:** {content_filters.get(guild.explicit_content_filter, 'Desconhecido')}",
            inline=True
        )
        
        # Features
        if guild.features:
            features_translated = {
                'ANIMATED_ICON': 'Ícone Animado',
                'BANNER': 'Banner',
                'COMMERCE': 'Comércio',
                'COMMUNITY': 'Comunidade',
                'DISCOVERABLE': 'Descobrível',
                'FEATURABLE': 'Destacável',
                'INVITE_SPLASH': 'Convite Personalizado',
                'MEMBER_VERIFICATION_GATE_ENABLED': 'Portão de Verificação',
                'NEWS': 'Canal de Notícias',
                'PARTNERED': 'Parceiro',
                'PREVIEW_ENABLED': 'Pré-visualização',
                'VANITY_URL': 'URL Personalizada',
                'VERIFIED': 'Verificado',
                'VIP_REGIONS': 'Regiões VIP',
                'WELCOME_SCREEN_ENABLED': 'Tela de Boas-vindas'
            }
            
            features_list = []
            for feature in guild.features:
                translated = features_translated.get(feature, feature.replace('_', ' ').title())
                features_list.append(f"✓ {translated}")
            
            if features_list:
                embed.add_field(
                    name="✨ **RECURSOS**",
                    value='\n'.join(features_list[:5]) + ('...' if len(features_list) > 5 else ''),
                    inline=False
                )
        
        # Ícones
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        if guild.banner:
            embed.set_image(url=guild.banner.url)
        
        embed.set_footer(text=f"ID: {guild.id} • Membros online: {sum(1 for m in guild.members if m.status != discord.Status.offline)}/{guild.member_count}")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="userinfo", aliases=["user", "uinfo", "whois"])
    async def informacoes_usuario(self, ctx, membro: discord.Member = None):
        """
        Mostra informações de um usuário
        Uso: !userinfo [@usuário]
        """
        
        membro = membro or ctx.author
        
        # Status traduzido
        status_translated = {
            'online': '🟢 Online',
            'idle': '🟡 Ausente',
            'dnd': '🔴 Não Perturbe',
            'offline': '⚫ Offline',
            'invisible': '⚫ Invisível'
        }
        
        # Atividade
        activity = "Nenhuma"
        if membro.activity:
            if isinstance(membro.activity, discord.CustomActivity):
                activity = f"**Personalizada:** {membro.activity.name}"
            elif isinstance(membro.activity, discord.Game):
                activity = f"🎮 **Jogando:** {membro.activity.name}"
            elif isinstance(membro.activity, discord.Streaming):
                activity = f"🎥 **Transmitindo:** {membro.activity.name}"
            elif isinstance(membro.activity, discord.Spotify):
                activity = f"🎵 **Ouvindo:** {membro.activity.title}"
            else:
                activity = f"**{membro.activity.type.name.title()}:** {membro.activity.name}"
        
        # Cargos (exceto @everyone)
        roles = [role.mention for role in membro.roles[1:]]  # Pula @everyone
        if not roles:
            roles_str = "Nenhum cargo"
        elif len(roles) <= 5:
            roles_str = ', '.join(roles)
        else:
            roles_str = f"{', '.join(roles[:5])} e mais {len(roles) - 5} cargos"
        
        # Badges
        badges = []
        public_flags = membro.public_flags
        
        flag_translations = {
            'staff': '👨‍💼 Staff do Discord',
            'partner': '🤝 Parceiro',
            'hypesquad': '🏠 HypeSquad',
            'bug_hunter': '🐛 Bug Hunter',
            'hypesquad_bravery': '⚔️ Bravery',
            'hypesquad_brilliance': '🎓 Brilliance',
            'hypesquad_balance': '⚖️ Balance',
            'early_supporter': '🎗️ Early Supporter',
            'verified_bot_developer': '🤖 Dev Verificado',
            'active_developer': '💻 Dev Ativo'
        }
        
        for flag, translation in flag_translations.items():
            if getattr(public_flags, flag, False):
                badges.append(translation)
        
        embed = discord.Embed(
            title=f"👤 **{membro.display_name}**",
            color=membro.color if membro.color.value != 0 else 0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        # Informações básicas
        embed.add_field(
            name="📝 **INFORMAÇÕES**",
            value=f"**Nome:** {membro.name}\n"
                  f"**Tag:** #{membro.discriminator}\n"
                  f"**ID:** {membro.id}\n"
                  f"**Bot:** {'Sim 🤖' if membro.bot else 'Não 👤'}",
            inline=True
        )
        
        embed.add_field(
            name="📅 **DATAS**",
            value=f"**Criado:** <t:{int(membro.created_at.timestamp())}:D>\n"
                  f"**Entrou:** <t:{int(membro.joined_at.timestamp())}:D>\n"
                  f"**Status:** {status_translated.get(str(membro.status), str(membro.status))}",
            inline=True
        )
        
        # Atividade e Cargo Principal
        embed.add_field(
            name="🎮 **ATIVIDADE**",
            value=activity,
            inline=False
        )
        
        embed.add_field(
            name="👑 **CARGO PRINCIPAL**",
            value=membro.top_role.mention if membro.top_role != ctx.guild.default_role else "@everyone",
            inline=True
        )
        
        embed.add_field(
            name="🏆 **BADGES**",
            value='\n'.join(badges) if badges else "Nenhum badge",
            inline=True
        )
        
        # Cargos
        embed.add_field(
            name=f"🎖️ **CARGOS ({len(roles)})**",
            value=roles_str,
            inline=False
        )
        
        # Avatar
        if membro.avatar:
            embed.set_thumbnail(url=membro.avatar.url)
            embed.set_image(url=membro.avatar.url)
        
        embed.set_footer(text=f"Solicitado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="botinfo", aliases=["bot", "binfo"])
    async def informacoes_bot(self, ctx):
        """
        Mostra informações sobre o bot
        Uso: !botinfo
        """
        
        # Uso de CPU e RAM
        cpu_usage = psutil.cpu_percent()
        ram = psutil.virtual_memory()
        ram_usage = ram.percent
        ram_total = ram.total / (1024 ** 3)  # Converter para GB
        
        # Tempo de atividade
        uptime = int(time.time() - self.start_time)
        days, remainder = divmod(uptime, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Estatísticas do bot
        total_guilds = len(self.bot.guilds)
        total_members = sum(g.member_count for g in self.bot.guilds)
        total_channels = sum(len(g.channels) for g in self.bot.guilds)
        
        embed = discord.Embed(
            title="🤖 **INFORMAÇÕES DO BOT**",
            description="Bot de Organização Automática de Servidores Discord",
            color=0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        # Informações básicas
        embed.add_field(
            name="📝 **INFORMAÇÕES**",
            value=f"**Nome:** {self.bot.user.name}\n"
                  f"**ID:** {self.bot.user.id}\n"
                  f"**Versão:** 2.0.0\n"
                  f"**Desenvolvedor:** Matheus\n"
                  f"**Prefixo:** `!`",
            inline=True
        )
        
        # Estatísticas
        embed.add_field(
            name="📊 **ESTATÍSTICAS**",
            value=f"**Servidores:** {total_guilds}\n"
                  f"**Membros:** {total_members:,}\n"
                  f"**Canais:** {total_channels}\n"
                  f"**Comandos:** {len(self.bot.commands)}",
            inline=True
        )
        
        # Sistema
        embed.add_field(
            name="💻 **SISTEMA**",
            value=f"**CPU:** {cpu_usage}%\n"
                  f"**RAM:** {ram_usage}% ({ram_total:.1f}GB)\n"
                  f"**Python:** {platform.python_version()}\n"
                  f"**discord.py:** {discord.__version__}",
            inline=True
        )
        
        # Tempo de atividade
        embed.add_field(
            name="⏱️ **TEMPO DE ATIVIDADE**",
            value=f"{days}d {hours}h {minutes}m {seconds}s",
            inline=True
        )
        
        # Latência
        latency = round(self.bot.latency * 1000)
        embed.add_field(
            name="📡 **LATÊNCIA**",
            value=f"{latency}ms",
            inline=True
        )
        
        # Links
        embed.add_field(
            name="🔗 **LINKS**",
            value="[GitHub](https://github.com) • [Documentação](https://discordpy.readthedocs.io)",
            inline=True
        )
        
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else self.bot.user.default_avatar.url)
        embed.set_footer(text=f"Solicitado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="convite", aliases=["invite", "addbot"])
    async def convidar_bot(self, ctx):
        """
        Mostra o link para convidar o bot
        Uso: !convite
        """
        
        embed = discord.Embed(
            title="📩 **CONVIDAR O BOT**",
            description="Para adicionar este bot ao seu servidor, use o link abaixo:",
            color=0x5865F2
        )
        
        # Link de convite genérico (substitua pelo seu Client ID)
        client_id = self.bot.user.id
        invite_link = f"https://discord.com/oauth2/authorize?client_id={client_id}&permissions=8&scope=bot%20applications.commands"
        
        embed.add_field(
            name="🔗 **Link de Convite**",
            value=f"[Clique aqui para adicionar o bot]({invite_link})",
            inline=False
        )
        
        embed.add_field(
            name="🔧 **Permissões Necessárias**",
            value="• Administrador (recomendado)\n"
                  "• Gerenciar Servidor\n"
                  "• Gerenciar Canais\n"
                  "• Gerenciar Cargos\n"
                  "• Gerenciar Mensagens\n"
                  "• Ver Logs de Auditoria",
            inline=False
        )
        
        embed.add_field(
            name="💡 **Dica**",
            value="Após adicionar o bot, use `!setup` para configurar seu servidor automaticamente!",
            inline=False
        )
        
        embed.set_footer(text="Você precisa ter a permissão 'Gerenciar Servidor'")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="avatar", aliases=["pfp", "foto"])
    async def mostrar_avatar(self, ctx, membro: discord.Member = None):
        """
        Mostra o avatar de um usuário
        Uso: !avatar [@usuário]
        """
        
        membro = membro or ctx.author
        
        if not membro.avatar and not membro.guild_avatar:
            await ctx.send("❌ Este usuário não tem avatar personalizado!")
            return
        
        embed = discord.Embed(
            title=f"🖼️ **Avatar de {membro.display_name}**",
            color=membro.color if membro.color.value != 0 else 0x5865F2
        )
        
        # Avatar global
        if membro.avatar:
            embed.set_image(url=membro.avatar.url)
            embed.add_field(
                name="🌍 **Avatar Global**",
                value=f"[Download]({membro.avatar.url})",
                inline=True
            )
        
        # Avatar do servidor
        if membro.guild_avatar:
            if not embed.image:  # Se não tiver imagem ainda
                embed.set_image(url=membro.guild_avatar.url)
            embed.add_field(
                name="🏠 **Avatar do Servidor**",
                value=f"[Download]({membro.guild_avatar.url})",
                inline=True
            )
        
        # Formato e tamanho
        if membro.avatar:
            embed.add_field(
                name="📐 **Formato**",
                value=membro.avatar.is_animated() and "GIF" or "PNG/JPG",
                inline=True
            )
        
        embed.set_footer(text=f"ID: {membro.id} • Solicitado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="emojiinfo", aliases=["emoji", "einfo"])
    async def informacoes_emoji(self, ctx, emoji: discord.Emoji):
        """
        Mostra informações sobre um emoji
        Uso: !emojiinfo :nome_emoji:
        """
        
        embed = discord.Embed(
            title=f"😀 **Informações do Emoji**",
            color=0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="📝 **Nome**", value=emoji.name, inline=True)
        embed.add_field(name="🆔 **ID**", value=emoji.id, inline=True)
        embed.add_field(name="🎨 **Animado**", value="Sim" if emoji.animated else "Não", inline=True)
        
        embed.add_field(name="📅 **Criado Em**", value=f"<t:{int(emoji.created_at.timestamp())}:D>", inline=True)
        embed.add_field(name="👑 **Criado Por**", value=emoji.user.mention if emoji.user else "Desconhecido", inline=True)
        embed.add_field(name="🏠 **Servidor**", value=emoji.guild.name if emoji.guild else "N/A", inline=True)
        
        embed.set_image(url=emoji.url)
        embed.set_footer(text=f"Solicitado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
    
    @commands.command(name="vote", aliases=["votar"])
    async def votar_bot(self, ctx):
        """
        Mostra links para votar no bot
        Uso: !vote
        """
        
        embed = discord.Embed(
            title="🗳️ **VOTAR NO BOT**",
            description="Ajude o bot a crescer votando nestes sites!",
            color=0x5865F2
        )
        
        embed.add_field(
            name="🔗 **Links de Votação**",
            value="[top.gg](https://top.gg)\n"
                  "[discordbotlist.com](https://discordbotlist.com)\n"
                  "[bots.ondiscord.xyz](https://bots.ondiscord.xyz)\n"
                  "[discord.bots.gg](https://discord.bots.gg)",
            inline=False
        )
        
        embed.add_field(
            name="💡 **Por que votar?**",
            value="• Mais visibilidade para o bot\n"
                  "• Ajuda outros usuários a encontrarem o bot\n"
                  "• Suporte ao desenvolvedor\n"
                  "• Possibilidade de features premium",
            inline=False
        )
        
        embed.set_footer(text="Obrigado pelo seu apoio! ❤️")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(UtilCommands(bot))