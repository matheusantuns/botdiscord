import discord
from discord.ext import commands
import asyncio
from ..templates import TEMPLATES, COLOR_MAP

class SetupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="setup")
    @commands.has_permissions(administrator=True)
    async def setup_server(self, ctx, template_name="gaming"):
        """Configura o servidor com um template específico"""
        
        template_name = template_name.lower()
        
        if template_name not in TEMPLATES:
            embed = discord.Embed(
                title="❌ Template não encontrado",
                description=f"**Templates disponíveis:**\n" + 
                           "\n".join([f"• **{name}** - {data['description']}" 
                                     for name, data in TEMPLATES.items()]),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        
        template = TEMPLATES[template_name]
        
        # Confirmação
        confirm_embed = discord.Embed(
            title="⚠️ CONFIRMAÇÃO DE SETUP",
            description=f"Você está prestes a configurar o servidor com o template **{template['name']}**\n\n"
                       "**Isso irá:**\n"
                       "• Criar novas categorias\n"
                       "• Criar novos canais\n"
                       "• Criar novos cargos\n"
                       "• Limpar organização atual\n\n"
                       "**Tem certeza?** Digite `sim` para confirmar ou `não` para cancelar.",
            color=discord.Color.orange()
        )
        confirm_embed.set_footer(text="Esta ação tem 30 segundos para ser confirmada")
        await ctx.send(embed=confirm_embed)
        
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['sim', 'não', 'nao']
        
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            
            if msg.content.lower() in ['não', 'nao']:
                await ctx.send("❌ Setup cancelado!")
                return
        except asyncio.TimeoutError:
            await ctx.send("⏰ Tempo esgotado! Setup cancelado.")
            return
        
        # Inicia setup
        progress_embed = discord.Embed(
            title=f"⚙️ CONFIGURANDO: {template['name']}",
            description="⏳ Iniciando configuração...",
            color=discord.Color.blue()
        )
        progress_msg = await ctx.send(embed=progress_embed)
        
        guild = ctx.guild
        
        try:
            # 1. Atualiza nome do servidor
            await guild.edit(name=template['name'])
            progress_embed.description = "✅ Nome do servidor atualizado\n⏳ Criando categorias..."
            await progress_msg.edit(embed=progress_embed)
            
            # 2. Cria categorias
            categories = {}
            for cat_info in template['categories']:
                category = await guild.create_category(cat_info['name'])
                await category.edit(position=cat_info['position'])
                categories[cat_info['name']] = category
                await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ Categorias criadas\n⏳ Criando canais de texto..."
            await progress_msg.edit(embed=progress_embed)
            
            # 3. Cria canais de texto
            for channel_info in template['channels']['text']:
                # Determina em qual categoria colocar
                if 'informações' in channel_info['name'].lower() or 'anúncios' in channel_info['name'].lower() or 'regras' in channel_info['name'].lower():
                    category = categories.get('📢 INFORMAÇÕES') or list(categories.values())[0]
                elif 'voz' in channel_info['name'].lower() or 'call' in channel_info['name'].lower():
                    category = categories.get('🎤 VOZ') or list(categories.values())[-1]
                else:
                    category = categories.get('🎮 COMUNIDADE') or list(categories.values())[1]
                
                channel = await category.create_text_channel(
                    name=channel_info['name'],
                    topic=channel_info.get('topic', '')
                )
                await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ Canais de texto criados\n⏳ Criando canais de voz..."
            await progress_msg.edit(embed=progress_embed)
            
            # 4. Cria canais de voz
            for channel_info in template['channels']['voice']:
                category = categories.get('🎤 VOZ') or list(categories.values())[-1]
                channel = await category.create_voice_channel(
                    name=channel_info['name'],
                    user_limit=channel_info.get('user_limit', 0)
                )
                await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ Canais de voz criados\n⏳ Criando cargos..."
            await progress_msg.edit(embed=progress_embed)
            
            # 5. Cria cargos
            for role_info in template['roles']:
                color_value = COLOR_MAP.get(role_info['color'], discord.Color.default())
                role = await guild.create_role(
                    name=role_info['name'],
                    color=color_value,
                    hoist=role_info.get('hoist', False)
                )
                await asyncio.sleep(0.5)
            
            progress_embed.description += "\n✅ Cargos criados\n⏳ Configurando permissões..."
            await progress_msg.edit(embed=progress_msg.embed)
            
            # 6. Configura permissões básicas
            for category in categories.values():
                # Permite que @everyone veja mas não envie mensagens em canais de info
                if 'INFORMAÇÕES' in category.name or 'CORPORATIVO' in category.name:
                    for channel in category.channels:
                        if isinstance(channel, discord.TextChannel):
                            await channel.set_permissions(
                                guild.default_role,
                                send_messages=False,
                                read_messages=True
                            )
            
            progress_embed.description += "\n✅ Permissões configuradas\n⏳ Criando mensagens de boas-vindas..."
            await progress_msg.edit(embed=progress_embed)
            
            # 7. Envia mensagem de boas-vindas
            try:
                welcome_channel = discord.utils.get(guild.text_channels, name="👋-boas-vindas")
                if welcome_channel:
                    welcome_embed = discord.Embed(
                        title=f"🎉 BEM-VINDO AO {template['name'].upper()}!",
                        description=f"Seja muito bem-vindo ao nosso servidor! 🎊\n\n"
                                   f"**Template usado:** {template['name']}\n"
                                   f"**Emoji:** {template['emoji']}\n"
                                   f"**Descrição:** {template['description']}\n\n"
                                   f"🔧 O servidor foi configurado automaticamente pelo bot.\n"
                                   f"👑 Configure os cargos conforme necessário.\n"
                                   f"🎨 Personalize à vontade!\n\n"
                                   f"**Comandos úteis:**\n"
                                   f"`!help` - Mostra todos os comandos\n"
                                   f"`!organizar` - Organiza canais\n"
                                   f"`!limpar` - Limpa mensagens\n"
                                   f"`!criarcanal` - Cria um novo canal",
                        color=discord.Color.green()
                    )
                    welcome_embed.set_footer(text="Configurado automaticamente • Digite !help para ajuda")
                    await welcome_channel.send(embed=welcome_embed)
            
            except Exception as e:
                print(f"Erro ao enviar mensagem de boas-vindas: {e}")
            
            # 8. Setup completo
            progress_embed.title = "✅ SETUP COMPLETO!"
            progress_embed.description = f"**Servidor configurado com sucesso!**\n\n"
            progress_embed.description += f"**Template:** {template['name']}\n"
            progress_embed.description += f"**Categorias criadas:** {len(categories)}\n"
            progress_embed.description += f"**Canais de texto:** {len(template['channels']['text'])}\n"
            progress_embed.description += f"**Canais de voz:** {len(template['channels']['voice'])}\n"
            progress_embed.description += f"**Cargos criados:** {len(template['roles'])}\n\n"
            progress_embed.description += "🎉 **Seu servidor está pronto!**\n"
            progress_embed.description += "👑 **Não se esqueça de:**\n"
            progress_embed.description += "• Configurar os cargos dos administradores\n"
            progress_embed.description += "• Adicionar regras específicas\n"
            progress_embed.description += "• Personalizar as cores e nomes\n"
            progress_embed.description += "• Convidar seus amigos!"
            progress_embed.color = discord.Color.green()
            
            await progress_msg.edit(embed=progress_embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ ERRO NO SETUP",
                description=f"Ocorreu um erro durante o setup:\n```{str(e)}```\n\n"
                           "Por favor, verifique as permissões do bot e tente novamente.",
                color=discord.Color.red()
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="templates")
    async def show_templates(self, ctx):
        """Mostra todos os templates disponíveis"""
        
        embed = discord.Embed(
            title="📁 TEMPLATES DISPONÍVEIS",
            description="Escolha um template para configurar seu servidor:\n",
            color=discord.Color.blue()
        )
        
        for template_name, template_data in TEMPLATES.items():
            channels_text = len(template_data['channels']['text'])
            channels_voice = len(template_data['channels']['voice'])
            roles_count = len(template_data['roles'])
            
            embed.add_field(
                name=f"{template_data['emoji']} **{template_name.upper()}**",
                value=f"**Nome:** {template_data['name']}\n"
                      f"**Descrição:** {template_data['description']}\n"
                      f"**Canais:** {channels_text} texto + {channels_voice} voz\n"
                      f"**Cargos:** {roles_count} cargos pré-configurados\n"
                      f"**Uso:** `!setup {template_name}`",
                inline=False
            )
        
        embed.set_footer(text="Use !setup [nome] para aplicar um template")
        await ctx.send(embed=embed)
    
    @commands.command(name="organizar")
    @commands.has_permissions(administrator=True)
    async def organize_channels(self, ctx):
        """Organiza todos os canais em categorias"""
        
        guild = ctx.guild
        
        embed = discord.Embed(
            title="🗂️ ORGANIZANDO CANAIS",
            description="⏳ Reorganizando canais em categorias...",
            color=discord.Color.blue()
        )
        msg = await ctx.send(embed=embed)
        
        # Cria categorias padrão se não existirem
        default_categories = [
            "📢 INFORMAÇÕES",
            "💬 COMUNICAÇÃO", 
            "🎤 VOZ",
            "🤖 BOTS",
            "📁 OUTROS"
        ]
        
        categories = {}
        for cat_name in default_categories:
            category = discord.utils.get(guild.categories, name=cat_name)
            if not category:
                category = await guild.create_category(cat_name)
            categories[cat_name] = category
        
        # Organiza canais existentes
        moved_count = 0
        
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                # Se já tem categoria, pula
                if channel.category:
                    continue
                
                # Determina categoria baseada no nome
                channel_lower = channel.name.lower()
                
                if any(x in channel_lower for x in ['regras', 'anúncios', 'avisos', 'boas-vindas']):
                    new_category = categories["📢 INFORMAÇÕES"]
                elif any(x in channel_lower for x in ['comandos', 'bot', 'ajuda']):
                    new_category = categories["🤖 BOTS"]
                else:
                    new_category = categories["💬 COMUNICAÇÃO"]
                
                try:
                    await channel.edit(category=new_category)
                    moved_count += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
        
        embed.title = "✅ ORGANIZAÇÃO COMPLETA"
        embed.description = f"**Canais reorganizados:** {moved_count}\n"
        embed.description += "**Categorias criadas/mantidas:**\n"
        for cat_name in default_categories:
            channel_count = len(categories[cat_name].channels)
            embed.description += f"• {cat_name}: {channel_count} canais\n"
        
        embed.color = discord.Color.green()
        await msg.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(SetupCommands(bot))