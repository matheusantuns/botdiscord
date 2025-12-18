"""
COMANDOS ADMINISTRATIVOS COMPLETOS
"""

import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import re

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="limpar", aliases=["clear", "clean"])
    @commands.has_permissions(manage_messages=True)
    async def limpar_mensagens(self, ctx, quantidade: int = 10):
        """
        Limpa mensagens do canal
        Uso: !limpar [quantidade] (padrão: 10, máximo: 100)
        """
        
        if quantidade < 1:
            await ctx.send("❌ A quantidade deve ser maior que 0!")
            return
        
        if quantidade > 100:
            quantidade = 100
            await ctx.send("⚠️ Limitado a 100 mensagens por segurança.")
        
        embed = discord.Embed(
            title="🧹 **LIMPEZA DE MENSAGENS**",
            description=f"Deletando **{quantidade}** mensagens...",
            color=0xFEE75C
        )
        embed.set_footer(text="Aguarde...")
        status_msg = await ctx.send(embed=embed)
        
        # Adiciona o comando à quantidade
        quantidade += 1
        
        try:
            deleted = await ctx.channel.purge(
                limit=quantidade,
                check=lambda m: not m.pinned,  # Não deleta mensagens fixadas
                before=ctx.message
            )
            
            deleted_count = len(deleted) - 1  # Remove o próprio comando da contagem
            
            # Resultado
            embed.title = "✅ **LIMPEZA CONCLUÍDA**"
            embed.description = f"**{deleted_count}** mensagens foram deletadas com sucesso!"
            embed.color = 0x57F287
            
            await status_msg.edit(embed=embed)
            
            # Auto-deleta após 5 segundos
            await asyncio.sleep(5)
            await status_msg.delete()
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO NA LIMPEZA**",
                description=f"Ocorreu um erro:\n```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="criarcategoria", aliases=["newcat", "addcategory"])
    @commands.has_permissions(manage_channels=True)
    async def criar_categoria(self, ctx, *, nome):
        """
        Cria uma nova categoria
        Uso: !criarcategoria [nome]
        """
        
        # Verifica se a categoria já existe
        categoria_existente = discord.utils.get(ctx.guild.categories, name=nome)
        if categoria_existente:
            await ctx.send(f"❌ A categoria **{nome}** já existe!")
            return
        
        try:
            categoria = await ctx.guild.create_category(name=nome)
            
            embed = discord.Embed(
                title="✅ **CATEGORIA CRIADA**",
                description=f"Categoria **{nome}** criada com sucesso!",
                color=0x57F287
            )
            embed.add_field(name="📊 Info", value=f"**ID:** {categoria.id}\n**Posição:** {categoria.position}")
            embed.set_footer(text=f"Criado por {ctx.author.name}")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO CRIAR CATEGORIA**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="criarcanal", aliases=["newchannel", "addchannel"])
    @commands.has_permissions(manage_channels=True)
    async def criar_canal(self, ctx, tipo="texto", *, nome):
        """
        Cria um novo canal (texto ou voz)
        Uso: !criarcanal [tipo] [nome]
        Tipos: texto, voz, anuncios
        """
        
        tipo = tipo.lower()
        guild = ctx.guild
        
        # Verifica se o canal já existe
        canal_existente = discord.utils.get(guild.channels, name=nome)
        if canal_existente:
            await ctx.send(f"❌ O canal **{nome}** já existe!")
            return
        
        try:
            if tipo in ["texto", "text", "txt", "t"]:
                canal = await guild.create_text_channel(nome)
                tipo_display = "📝 Texto"
                
            elif tipo in ["voz", "voice", "call", "v"]:
                canal = await guild.create_voice_channel(nome)
                tipo_display = "🎤 Voz"
                
            elif tipo in ["anuncios", "announce", "news", "a"]:
                canal = await guild.create_text_channel(
                    nome,
                    topic="📢 Canal de anúncios",
                    slowmode_delay=300  # 5 minutos entre mensagens
                )
                tipo_display = "📢 Anúncios"
                await canal.set_permissions(guild.default_role, send_messages=False)
                
            else:
                embed = discord.Embed(
                    title="❌ **TIPO INVÁLIDO**",
                    description="**Tipos disponíveis:**\n• `texto` - Canal de texto\n• `voz` - Canal de voz\n• `anuncios` - Canal de anúncios",
                    color=0xED4245
                )
                await ctx.send(embed=embed)
                return
            
            embed = discord.Embed(
                title="✅ **CANAL CRIADO**",
                description=f"Canal **{tipo_display}** criado com sucesso!",
                color=0x57F287
            )
            embed.add_field(name="📝 Nome", value=canal.name, inline=True)
            embed.add_field(name="🎯 Tipo", value=tipo_display, inline=True)
            embed.add_field(name="🆔 ID", value=canal.id, inline=True)
            embed.set_footer(text=f"Criado por {ctx.author.name}")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO CRIAR CANAL**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="criarcargo", aliases=["newrole", "addrole"])
    @commands.has_permissions(manage_roles=True)
    async def criar_cargo(self, ctx, *, nome):
        """
        Cria um novo cargo
        Uso: !criarcargo [nome]
        """
        
        guild = ctx.guild
        
        # Verifica se o cargo já existe
        cargo_existente = discord.utils.get(guild.roles, name=nome)
        if cargo_existente:
            await ctx.send(f"❌ O cargo **{nome}** já existe!")
            return
        
        try:
            cargo = await guild.create_role(name=nome)
            
            embed = discord.Embed(
                title="✅ **CARGO CRIADO**",
                description=f"Cargo **{nome}** criado com sucesso!",
                color=0x57F287
            )
            embed.add_field(name="🆔 ID", value=cargo.id, inline=True)
            embed.add_field(name="🎨 Cor", value=str(cargo.color), inline=True)
            embed.add_field(name="👥 Posição", value=cargo.position, inline=True)
            embed.set_footer(text=f"Criado por {ctx.author.name}")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO CRIAR CARGO**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="ban", aliases=["banir"])
    @commands.has_permissions(ban_members=True)
    async def banir_membro(self, ctx, membro: discord.Member, *, motivo=None):
        """
        Bane um membro do servidor
        Uso: !ban [@membro] [motivo]
        """
        
        if membro == ctx.author:
            await ctx.send("❌ Você não pode banir a si mesmo!")
            return
        
        if membro.top_role >= ctx.author.top_role:
            await ctx.send("❌ Você não pode banir alguém com cargo igual ou superior!")
            return
        
        try:
            await membro.ban(reason=motivo)
            
            embed = discord.Embed(
                title="🔨 **MEMBRO BANIDO**",
                description=f"**{membro.name}** foi banido do servidor.",
                color=0xED4245,
                timestamp=datetime.utcnow()
            )
            
            if motivo:
                embed.add_field(name="📝 Motivo", value=motivo, inline=False)
            
            embed.add_field(name="👤 Membro", value=f"{membro.mention}\n{str(membro)}", inline=True)
            embed.add_field(name="👮‍♂️ Moderador", value=ctx.author.mention, inline=True)
            embed.set_thumbnail(url=membro.avatar.url if membro.avatar else membro.default_avatar.url)
            embed.set_footer(text="Banimento registrado")
            
            await ctx.send(embed=embed)
            
            # Tenta enviar DM para o membro banido
            try:
                dm_embed = discord.Embed(
                    title="🚫 **Você foi banido**",
                    description=f"Você foi banido do servidor **{ctx.guild.name}**.",
                    color=0xED4245,
                    timestamp=datetime.utcnow()
                )
                
                if motivo:
                    dm_embed.add_field(name="📝 Motivo", value=motivo, inline=False)
                
                dm_embed.add_field(name="👮‍♂️ Moderador", value=str(ctx.author), inline=True)
                dm_embed.set_footer(text="Banimento aplicado")
                
                await membro.send(embed=dm_embed)
            except:
                pass  # Não conseguiu enviar DM
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO BANIR**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="kick", aliases=["expulsar"])
    @commands.has_permissions(kick_members=True)
    async def expulsar_membro(self, ctx, membro: discord.Member, *, motivo=None):
        """
        Expulsa um membro do servidor
        Uso: !kick [@membro] [motivo]
        """
        
        if membro == ctx.author:
            await ctx.send("❌ Você não pode expulsar a si mesmo!")
            return
        
        if membro.top_role >= ctx.author.top_role:
            await ctx.send("❌ Você não pode expulsar alguém com cargo igual ou superior!")
            return
        
        try:
            await membro.kick(reason=motivo)
            
            embed = discord.Embed(
                title="👢 **MEMBRO EXPULSO**",
                description=f"**{membro.name}** foi expulso do servidor.",
                color=0xFEE75C,
                timestamp=datetime.utcnow()
            )
            
            if motivo:
                embed.add_field(name="📝 Motivo", value=motivo, inline=False)
            
            embed.add_field(name="👤 Membro", value=f"{membro.mention}\n{str(membro)}", inline=True)
            embed.add_field(name="👮‍♂️ Moderador", value=ctx.author.mention, inline=True)
            embed.set_thumbnail(url=membro.avatar.url if membro.avatar else membro.default_avatar.url)
            embed.set_footer(text="Expulsão registrada")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO EXPULSAR**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="mute", aliases=["silenciar"])
    @commands.has_permissions(moderate_members=True)
    async def silenciar_membro(self, ctx, membro: discord.Member, tempo: int = 60, *, motivo=None):
        """
        Silencia um membro por um período
        Uso: !mute [@membro] [tempo em minutos] [motivo]
        """
        
        if tempo < 1:
            await ctx.send("❌ O tempo deve ser pelo menos 1 minuto!")
            return
        
        if tempo > 10080:  # 7 dias
            tempo = 10080
            await ctx.send("⚠️ Tempo limitado a 7 dias (10080 minutos).")
        
        try:
            duration = timedelta(minutes=tempo)
            await membro.timeout(duration, reason=motivo)
            
            embed = discord.Embed(
                title="🔇 **MEMBRO SILENCIADO**",
                description=f"**{membro.name}** foi silenciado.",
                color=0xFEE75C,
                timestamp=datetime.utcnow()
            )
            
            embed.add_field(name="⏰ Duração", value=f"{tempo} minutos", inline=True)
            embed.add_field(name="⏱️ Até", value=f"<t:{(datetime.utcnow() + duration).timestamp():.0f}:R>", inline=True)
            
            if motivo:
                embed.add_field(name="📝 Motivo", value=motivo, inline=False)
            
            embed.add_field(name="👤 Membro", value=f"{membro.mention}\n{str(membro)}", inline=True)
            embed.add_field(name="👮‍♂️ Moderador", value=ctx.author.mention, inline=True)
            embed.set_thumbnail(url=membro.avatar.url if membro.avatar else membro.default_avatar.url)
            embed.set_footer(text="Silenciamento aplicado")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO SILENCIAR**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="unmute", aliases=["dessilenciar"])
    @commands.has_permissions(moderate_members=True)
    async def dessilenciar_membro(self, ctx, membro: discord.Member, *, motivo=None):
        """
        Remove o silenciamento de um membro
        Uso: !unmute [@membro] [motivo]
        """
        
        try:
            await membro.timeout(None, reason=motivo)
            
            embed = discord.Embed(
                title="🔊 **SILENCIAMENTO REMOVIDO**",
                description=f"O silenciamento de **{membro.name}** foi removido.",
                color=0x57F287,
                timestamp=datetime.utcnow()
            )
            
            if motivo:
                embed.add_field(name="📝 Motivo", value=motivo, inline=False)
            
            embed.add_field(name="👤 Membro", value=f"{membro.mention}\n{str(membro)}", inline=True)
            embed.add_field(name="👮‍♂️ Moderador", value=ctx.author.mention, inline=True)
            embed.set_thumbnail(url=membro.avatar.url if membro.avatar else membro.default_avatar.url)
            embed.set_footer(text="Silenciamento removido")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO DESSILENCIAR**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)
    
    @commands.command(name="backup", aliases=["backupserver"])
    @commands.has_permissions(administrator=True)
    async def backup_servidor(self, ctx):
        """
        Cria um backup das informações do servidor
        Uso: !backup
        """
        
        guild = ctx.guild
        
        embed = discord.Embed(
            title="💾 **BACKUP DO SERVIDOR**",
            description=f"Backup criado para **{guild.name}**",
            color=0x5865F2,
            timestamp=datetime.utcnow()
        )
        
        # Informações básicas
        embed.add_field(
            name="📊 **INFORMAÇÕES GERAIS**",
            value=f"**Nome:** {guild.name}\n"
                  f"**ID:** {guild.id}\n"
                  f"**Dono:** {guild.owner.mention}\n"
                  f"**Criado:** <t:{int(guild.created_at.timestamp())}:D>\n"
                  f"**Membros:** {guild.member_count}\n"
                  f"**Boosts:** {guild.premium_subscription_count} (Nível {guild.premium_tier})",
            inline=False
        )
        
        # Canais
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        total_channels = text_channels + voice_channels
        
        embed.add_field(
            name="💬 **CANAIS**",
            value=f"**Categorias:** {categories}\n"
                  f"**Texto:** {text_channels}\n"
                  f"**Voz:** {voice_channels}\n"
                  f"**Total:** {total_channels}",
            inline=True
        )
        
        # Cargos
        roles = len(guild.roles)
        embed.add_field(
            name="👑 **CARGOS**",
            value=f"**Total:** {roles}\n"
                  f"**Lista:** {', '.join([role.name for role in guild.roles[1:6]])}{'...' if roles > 6 else ''}",
            inline=True
        )
        
        # Emojis e Stickers
        emojis = len(guild.emojis)
        stickers = len(guild.stickers)
        
        embed.add_field(
            name="🎨 **EMOJIS & STICKERS**",
            value=f"**Emojis:** {emojis}/50\n"
                  f"**Stickers:** {stickers}/15",
            inline=True
        )
        
        # Configurações
        verification_level = str(guild.verification_level).replace("_", " ").title()
        explicit_content_filter = str(guild.explicit_content_filter).replace("_", " ").title()
        
        embed.add_field(
            name="⚙️ **CONFIGURAÇÕES**",
            value=f"**Nível de Verificação:** {verification_level}\n"
                  f"**Filtro de Conteúdo:** {explicit_content_filter}\n"
                  f"**Região:** {guild.preferred_locale}",
            inline=True
        )
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        embed.set_footer(text=f"Backup criado por {ctx.author.name}")
        
        await ctx.send(embed=embed)
        
        # Cria um arquivo de texto com informações detalhadas
        backup_info = f"""
=== BACKUP DO SERVIDOR ===
Data: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}
Servidor: {guild.name} (ID: {guild.id})
Dono: {guild.owner} (ID: {guild.owner.id})

=== MEMBROS ===
Total: {guild.member_count}

=== CARGOS ===
Total: {roles}
Lista: {', '.join([role.name for role in guild.roles])}

=== CATEGORIAS ===
Total: {categories}
"""
        
        for i, category in enumerate(guild.categories, 1):
            backup_info += f"\n{i}. {category.name} ({len(category.channels)} canais)"
        
        backup_info += f"\n\n=== CANAIS DE TEXTO ===\nTotal: {text_channels}\n"
        
        for i, channel in enumerate(guild.text_channels, 1):
            backup_info += f"\n{i}. {channel.name} (Categoria: {channel.category.name if channel.category else 'Nenhuma'})"
        
        # Envia como arquivo
        from io import StringIO
        file = StringIO(backup_info)
        
        await ctx.send(
            content="📁 **Arquivo de backup detalhado:**",
            file=discord.File(fp=file, filename=f"backup_{guild.name}_{datetime.utcnow().strftime('%Y%m%d')}.txt")
        )
    
    @commands.command(name="audit", aliases=["auditlog", "logs"])
    @commands.has_permissions(view_audit_log=True)
    async def verificar_logs(self, ctx, quantidade: int = 10):
        """
        Mostra as últimas entradas do log de auditoria
        Uso: !audit [quantidade] (padrão: 10, máximo: 50)
        """
        
        if quantidade < 1:
            await ctx.send("❌ A quantidade deve ser maior que 0!")
            return
        
        if quantidade > 50:
            quantidade = 50
        
        try:
            embed = discord.Embed(
                title="📋 **LOG DE AUDITORIA**",
                description=f"Mostrando as últimas **{quantidade}** entradas",
                color=0x5865F2,
                timestamp=datetime.utcnow()
            )
            
            async for entry in ctx.guild.audit_logs(limit=quantidade):
                # Formata a ação
                action = str(entry.action).replace("_", " ").title()
                
                # Formata o alvo
                target = str(entry.target)
                if hasattr(entry.target, 'mention'):
                    target = entry.target.mention
                
                # Formata o usuário
                user = entry.user.mention if entry.user else "Desconhecido"
                
                # Adiciona ao embed (limitando a 5 campos)
                if len(embed.fields) < 5:
                    embed.add_field(
                        name=f"**{action}**",
                        value=f"👤 **Usuário:** {user}\n🎯 **Alvo:** {target}\n📝 **Motivo:** {entry.reason or 'Nenhum'}\n⏰ **Quando:** <t:{int(entry.created_at.timestamp())}:R>",
                        inline=False
                    )
            
            if not embed.fields:
                embed.description = "Nenhuma entrada encontrada no log de auditoria."
            
            embed.set_footer(text=f"Solicitado por {ctx.author.name}")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ **ERRO AO ACESSAR LOGS**",
                description=f"```{str(e)}```",
                color=0xED4245
            )
            await ctx.send(embed=error_embed)

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))