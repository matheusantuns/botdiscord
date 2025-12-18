"""
TEMPLATES PROFISSIONAIS PARA SERVIDORES DISCORD
Com emojis, categorias organizadas e cargos detalhados
"""

TEMPLATES = {
    # ========== TEMPLATE GAMING ULTRA ==========
    "gaming": {
        "name": "🎮 Gaming Universe",
        "emoji": "🎮",
        "description": "Servidor premium para gamers competitivos e casuais com organização profissional",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios oficiais e atualizações"},
                {"name": "📜│regras", "topic": "⚖️ Leia as regras antes de participar"},
                {"name": "👋│boas-vindas", "topic": "🎉 Apresente-se para a comunidade!"},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos membros"},
                {"name": "💬│geral", "topic": "💭 Conversas gerais sobre qualquer coisa"},
                {"name": "🎮│games-discussão", "topic": "🕹️ Discussão geral sobre jogos"},
                {"name": "🎯│fps", "topic": "🔫 Valorant, CS2, COD, Rainbow Six"},
                {"name": "⚔️│moba", "topic": "🏰 League of Legends, Dota 2, Smite"},
                {"name": "🎲│casual", "topic": "🎪 Stardew Valley, Minecraft, Among Us"},
                {"name": "🎪│rpg", "topic": "🐉 D&D, Genshin Impact, Final Fantasy"},
                {"name": "🎵│musica", "topic": "🎧 Recomendações musicais e playlists"},
                {"name": "🎥│clips", "topic": "📹 Compartilhe seus melhores momentos!"},
                {"name": "🤣│memes", "topic": "😂 Memes e humor da comunidade"},
                {"name": "🎨│artes", "topic": "🖌️ Arte, designs e criatividade"},
                {"name": "🍿│filmes-series", "topic": "🎬 Recomendações de filmes e séries"},
                {"name": "💡│sugestões", "topic": "💭 Sugira melhorias para o servidor"},
                {"name": "❓│ajuda", "topic": "🆘 Precisa de ajuda? Pergunte aqui!"},
                {"name": "🏆│conquistas", "topic": "⭐ Compartilhe suas conquistas!"},
                {"name": "📱│offtopic", "topic": "💬 Conversas fora do tema gaming"}
            ],
            "voice": [
                {"name": "🎮│Lobby Principal", "user_limit": 0},
                {"name": "🎯│FPS Squad", "user_limit": 5},
                {"name": "⚔️│MOBA Team", "user_limit": 5},
                {"name": "🎲│Casual Chat", "user_limit": 10},
                {"name": "🎪│RPG Session", "user_limit": 6},
                {"name": "🎵│Ouvindo Música", "user_limit": 5},
                {"name": "🎤│Karaokê", "user_limit": 10},
                {"name": "🎧│Foco Total", "user_limit": 1},
                {"name": "💤│AFK Zone", "user_limit": 0},
                {"name": "🎮│Torneio 1", "user_limit": 10},
                {"name": "🎮│Torneio 2", "user_limit": 10}
            ],
            "stage": [
                {"name": "🎤│Palco Principal", "topic": "Eventos e anúncios importantes"},
                {"name": "🏆│Cerimônia", "topic": "Premiações e eventos especiais"}
            ]
        },
        "roles": [
            {"name": "👑│Dono", "color": "gold", "hoist": True},
            {"name": "⚡│Co-Fundador", "color": "purple", "hoist": True},
            {"name": "🛡️│Administrador", "color": "red", "hoist": True},
            {"name": "⭐│Moderador", "color": "blue", "hoist": True},
            {"name": "🎮│Pro Player", "color": "green", "hoist": True},
            {"name": "🌟│VIP", "color": "orange", "hoist": True},
            {"name": "🤖│Bot", "color": "teal", "hoist": False},
            {"name": "🎥│Streamer", "color": "pink", "hoist": True},
            {"name": "🏆│Campeão", "color": "yellow", "hoist": True},
            {"name": "🎯│Competitivo", "color": "dark_red", "hoist": False},
            {"name": "🎲│Casual", "color": "dark_green", "hoist": False},
            {"name": "🎨│Artista", "color": "magenta", "hoist": False},
            {"name": "🎵│DJ", "color": "cyan", "hoist": False},
            {"name": "🔔│Notificado", "color": "light_blue", "hoist": False},
            {"name": "🎪│Membro", "color": "default", "hoist": False},
            {"name": "👀│Spectator", "color": "grey", "hoist": False}
        ],
        "categories": [
            {"name": "📢│INFORMAÇÕES", "position": 0},
            {"name": "💬│COMUNIDADE", "position": 1},
            {"name": "🎮│JOGOS", "position": 2},
            {"name": "🎤│VOICE CHAT", "position": 3},
            {"name": "🏆│TORNEIOS", "position": 4},
            {"name": "🎨│CRIATIVIDADE", "position": 5}
        ]
    },
    
    # ========== TEMPLATE ESTUDO PRO ==========
    "estudo": {
        "name": "📚 Academia Pro",
        "emoji": "📚",
        "description": "Plataforma educacional completa com recursos para aprendizado colaborativo",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes e avisos"},
                {"name": "📜│regras", "topic": "⚖️ Regras da comunidade de estudos"},
                {"name": "👋│boas-vindas", "topic": "🎉 Boas-vindas! Conte-nos sobre você"},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos alunos"},
                {"name": "💬│geral", "topic": "💭 Conversas gerais sobre estudos"},
                {"name": "📚│material", "topic": "📖 Compartilhe materiais de estudo"},
                {"name": "❓│dúvidas", "topic": "🤔 Tire suas dúvidas aqui"},
                {"name": "📅│calendário", "topic": "🗓️ Datas importantes e prazos"},
                {"name": "📝│anotações", "topic": "✏️ Anotações compartilhadas e resumos"},
                {"name": "🔬│ciências", "topic": "🧪 Biologia, Química, Física"},
                {"name": "🧮│matemática", "topic": "📐 Cálculo, Álgebra, Geometria"},
                {"name": "💻│programação", "topic": "👨‍💻 Python, JavaScript, Java, C++"},
                {"name": "🌍│humanas", "topic": "📖 História, Geografia, Filosofia"},
                {"name": "💼│administração", "topic": "📊 Negócios, Economia, Marketing"},
                {"name": "🎨│artes", "topic": "🖌️ Arte, Design, Música"},
                {"name": "🏆│conquistas", "topic": "⭐ Compartilhe suas conquistas!"},
                {"name": "💡│dicas", "topic": "💭 Técnicas de estudo e produtividade"},
                {"name": "📖│recomendações", "topic": "📚 Livros, cursos e recursos"},
                {"name": "☕│descontração", "topic": "🎮 Hora do café e descanso"}
            ],
            "voice": [
                {"name": "📚│Sala de Estudos 1", "user_limit": 5},
                {"name": "📚│Sala de Estudos 2", "user_limit": 5},
                {"name": "📚│Sala de Estudos 3", "user_limit": 5},
                {"name": "💭│Sala de Discussão", "user_limit": 10},
                {"name": "🎤│Aula Online", "user_limit": 50},
                {"name": "🎧│Foco Total", "user_limit": 1},
                {"name": "👥│Grupo de Estudo", "user_limit": 8},
                {"name": "☕│Pausa Café", "user_limit": 10},
                {"name": "🎵│Ambiente Calmo", "user_limit": 3}
            ],
            "stage": [
                {"name": "🎤│Palestra", "topic": "Aulas e palestras ao vivo"},
                {"name": "💡│Workshop", "topic": "Workshops e tutoriais"}
            ]
        },
        "roles": [
            {"name": "👑│Coordenador", "color": "gold", "hoist": True},
            {"name": "👨‍🏫│Professor", "color": "blue", "hoist": True},
            {"name": "📚│Monitor", "color": "green", "hoist": True},
            {"name": "🎓│Aluno Avançado", "color": "purple", "hoist": True},
            {"name": "👨‍🎓│Aluno", "color": "default", "hoist": False},
            {"name": "💻│Programador", "color": "orange", "hoist": False},
            {"name": "🔬│Cientista", "color": "teal", "hoist": False},
            {"name": "🎨│Artista", "color": "pink", "hoist": False},
            {"name": "📖│Leitor", "color": "dark_blue", "hoist": False},
            {"name": "🎯│Focado", "color": "dark_green", "hoist": False},
            {"name": "⭐│Destaque", "color": "yellow", "hoist": True},
            {"name": "🤝│Voluntário", "color": "cyan", "hoist": False},
            {"name": "🎁│Convidado", "color": "grey", "hoist": False}
        ],
        "categories": [
            {"name": "📢│INFORMAÇÕES", "position": 0},
            {"name": "📚│ÁREAS DE ESTUDO", "position": 1},
            {"name": "🎤│SALAS DE ESTUDO", "position": 2},
            {"name": "💬│COMUNIDADE", "position": 3},
            {"name": "🏆│PROGRESSO", "position": 4}
        ]
    },
    
    # ========== TEMPLATE STREAMER PRO ==========
    "streamer": {
        "name": "🎥 Streamer Pro",
        "emoji": "🎥",
        "description": "Servidor profissional para streamers com ferramentas para crescimento e engajamento",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios das lives e novidades"},
                {"name": "📜│regras", "topic": "⚖️ Regras da comunidade do streamer"},
                {"name": "👋│boas-vindas", "topic": "🎉 Bem-vindo à comunidade!"},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos viewers"},
                {"name": "💬│chat-geral", "topic": "💭 Conversas da comunidade"},
                {"name": "🎮│games", "topic": "🕹️ Discussão sobre jogos"},
                {"name": "🎥│clips", "topic": "📹 Compartilhe seus melhores clips"},
                {"name": "🤣│memes", "topic": "😂 Memes da comunidade"},
                {"name": "💬│sugestões", "topic": "💭 Sugira jogos e ideias para lives"},
                {"name": "🎵│playlist", "topic": "🎧 Sugestões musicais"},
                {"name": "📊│metas", "topic": "📈 Metas do canal e conquistas"},
                {"name": "💻│setup", "topic": "🖥️ Equipamentos e configurações"},
                {"name": "🎨│artes", "topic": "🖌️ Artes, overlays e designs"},
                {"name": "🤝│colabs", "topic": "👥 Propostas de colaborações"},
                {"name": "🏆│highlights", "topic": "⭐ Melhores momentos da semana"},
                {"name": "💰│doações", "topic": "💸 Informações sobre doações"},
                {"name": "❓│ajuda", "topic": "🆘 Precisa de ajuda? Pergunte aqui!"},
                {"name": "☕│offstream", "topic": "💬 Conversas fora das lives"}
            ],
            "voice": [
                {"name": "🎤│Sala do Streamer", "user_limit": 1},
                {"name": "🎮│Gaming com Subs", "user_limit": 5},
                {"name": "💬│Call da Comunidade", "user_limit": 0},
                {"name": "🎵│Ouvindo Música", "user_limit": 0},
                {"name": "🎤│Karaokê", "user_limit": 10},
                {"name": "🎧│Edição", "user_limit": 3},
                {"name": "👥│Colaboração", "user_limit": 4},
                {"name": "💤│AFK", "user_limit": 0},
                {"name": "🎮│Torneio 1", "user_limit": 10},
                {"name": "🎮│Torneio 2", "user_limit": 10}
            ],
            "stage": [
                {"name": "🎤│Ao Vivo", "topic": "Transmissões ao vivo"},
                {"name": "🏆│Eventos", "topic": "Eventos especiais e sorteios"}
            ]
        },
        "roles": [
            {"name": "🎥│Streamer", "color": "purple", "hoist": True},
            {"name": "👑│Dono", "color": "gold", "hoist": True},
            {"name": "⭐│Moderador", "color": "blue", "hoist": True},
            {"name": "🔔│Notificado", "color": "green", "hoist": False},
            {"name": "🤖│Bot", "color": "teal", "hoist": False},
            {"name": "👑│Subscriber", "color": "red", "hoist": True},
            {"name": "🌟│VIP", "color": "orange", "hoist": True},
            {"name": "🎮│Gamer", "color": "green", "hoist": False},
            {"name": "🎨│Designer", "color": "pink", "hoist": False},
            {"name": "💻│Tech", "color": "cyan", "hoist": False},
            {"name": "💰│Doador", "color": "yellow", "hoist": True},
            {"name": "🏆│Campeão", "color": "magenta", "hoist": True},
            {"name": "👥│Comunidade", "color": "default", "hoist": False}
        ],
        "categories": [
            {"name": "📢│INFORMAÇÕES", "position": 0},
            {"name": "🎥│COMUNIDADE", "position": 1},
            {"name": "🎮│CONTEÚDO", "position": 2},
            {"name": "🎤│VOICE", "position": 3},
            {"name": "💼│NEGÓCIOS", "position": 4}
        ]
    },
    
    # ========== TEMPLATE EMPRESA CORPORATIVO ==========
    "empresa": {
        "name": "💼 Nexus Corporativo",
        "emoji": "💼",
        "description": "Ambiente profissional para empresas com estrutura para departamentos e comunicação eficiente",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Comunicados corporativos oficiais"},
                {"name": "📜│regras", "topic": "⚖️ Políticas e normas da empresa"},
                {"name": "👋│boas-vindas", "topic": "🎉 Boas-vindas à equipe!"},
                {"name": "🎯│onboarding", "topic": "✨ Guia de integração de novos colaboradores"},
                {"name": "💬│geral", "topic": "💭 Comunicação geral da empresa"},
                {"name": "💼│rh", "topic": "👥 Recursos Humanos e administrativo"},
                {"name": "📊│financeiro", "topic": "💰 Finanças e contabilidade"},
                {"name": "🛠️│ti", "topic": "💻 Tecnologia da Informação"},
                {"name": "📈│vendas", "topic": "🛒 Vendas e comercial"},
                {"name": "🎯│marketing", "topic": "📣 Marketing e publicidade"},
                {"name": "⚙️│ops", "topic": "🚚 Operações e logística"},
                {"name": "💡│projetos", "topic": "📋 Gerenciamento de projetos"},
                {"name": "📝│relatórios", "topic": "📄 Relatórios e métricas"},
                {"name": "🎯│metas", "topic": "⭐ Metas e objetivos trimestrais"},
                {"name": "🤝│clientes", "topic": "👨‍💼 Atendimento ao cliente"},
                {"name": "💡│ideias", "topic": "💭 Sugestões e melhorias"},
                {"name": "🏆│conquistas", "topic": "🎉 Celebrando conquistas da equipe"},
                {"name": "☕│break", "topic": "🎮 Momento descontração e café"}
            ],
            "voice": [
                {"name": "💼│Reunião Geral", "user_limit": 50},
                {"name": "💼│Reunião Diretoria", "user_limit": 10},
                {"name": "💼│Reunião de Equipe", "user_limit": 15},
                {"name": "💬│Call Rápida", "user_limit": 5},
                {"name": "🎤│Apresentações", "user_limit": 100},
                {"name": "🤝│Sala de Clientes", "user_limit": 10},
                {"name": "☕│Cafeteria Virtual", "user_limit": 20},
                {"name": "🎧│Foco Individual", "user_limit": 1}
            ],
            "stage": [
                {"name": "🎤│Treinamento", "topic": "Treinamentos corporativos"},
                {"name": "💡│Brainstorm", "topic": "Sessões de brainstorming"}
            ]
        },
        "roles": [
            {"name": "👑│CEO", "color": "gold", "hoist": True},
            {"name": "👔│Diretor", "color": "purple", "hoist": True},
            {"name": "👨‍💼│Gerente", "color": "blue", "hoist": True},
            {"name": "💼│Líder", "color": "green", "hoist": True},
            {"name": "👨‍💻│Sênior", "color": "orange", "hoist": False},
            {"name": "💼│Pleno", "color": "cyan", "hoist": False},
            {"name": "🎯│Júnior", "color": "teal", "hoist": False},
            {"name": "🤝│Estagiário", "color": "pink", "hoist": False},
            {"name": "💻│TI", "color": "red", "hoist": False},
            {"name": "📊│Financeiro", "color": "dark_green", "hoist": False},
            {"name": "📈│Vendas", "color": "yellow", "hoist": False},
            {"name": "🎯│Marketing", "color": "magenta", "hoist": False},
            {"name": "🤖│Bot", "color": "grey", "hoist": False},
            {"name": "👥│Colaborador", "color": "default", "hoist": False}
        ],
        "categories": [
            {"name": "📢│CORPORATIVO", "position": 0},
            {"name": "💼│DEPARTAMENTOS", "position": 1},
            {"name": "🎤│REUNIÕES", "position": 2},
            {"name": "💬│COMUNICAÇÃO", "position": 3},
            {"name": "🏆│DESENVOLVIMENTO", "position": 4}
        ]
    },
    
    # ========== TEMPLATE COMUNIDADE INTERNACIONAL ==========
    "comunidade": {
        "name": "🌍 Comunidade Global",
        "emoji": "🌍",
        "description": "Servidor para comunidades diversas com espaço para todos os interesses e culturas",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes da comunidade"},
                {"name": "📜│regras", "topic": "⚖️ Regras gerais da comunidade"},
                {"name": "👋│boas-vindas", "topic": "🎉 Seja bem-vindo! Conte sobre você"},
                {"name": "🎯│introdução", "topic": "✨ Guia rápido para novos membros"},
                {"name": "💬│geral", "topic": "💭 Conversas gerais"},
                {"name": "🎮│games", "topic": "🕹️ Jogos e entretenimento"},
                {"name": "🎬│filmes-series", "topic": "🎬 Filmes, séries e animes"},
                {"name": "🎵│musica", "topic": "🎧 Música e artistas"},
                {"name": "📚│livros", "topic": "📖 Livros e literatura"},
                {"name": "💻│tecnologia", "topic": "🖥️ Tecnologia e inovação"},
                {"name": "🏃│esportes", "topic": "⚽ Esportes e atividades físicas"},
                {"name": "🍳│culinária", "topic": "🍰 Receitas e culinária"},
                {"name": "✈️│viagens", "topic": "🗺️ Viagens e culturas"},
                {"name": "🎨│artes", "topic": "🖌️ Arte e criatividade"},
                {"name": "🤣│memes", "topic": "😂 Memes e humor"},
                {"name": "❓│ajuda", "topic": "🆘 Ajuda e suporte"},
                {"name": "💡│sugestões", "topic": "💭 Sugestões para a comunidade"},
                {"name": "🏆│eventos", "topic": "🎉 Eventos e atividades"}
            ],
            "voice": [
                {"name": "💬│Sala Geral", "user_limit": 0},
                {"name": "🎮│Gaming Lounge", "user_limit": 0},
                {"name": "🎵│Music Room", "user_limit": 0},
                {"name": "🎬│Watch Party", "user_limit": 10},
                {"name": "☕│Café Virtual", "user_limit": 10},
                {"name": "🎤│Karaokê", "user_limit": 10},
                {"name": "🌍│Internacional", "user_limit": 0},
                {"name": "💤│AFK", "user_limit": 0}
            ],
            "stage": [
                {"name": "🎤│Eventos", "topic": "Eventos comunitários"},
                {"name": "💡│Debates", "topic": "Debates e discussões"}
            ]
        },
        "roles": [
            {"name": "👑│Fundador", "color": "gold", "hoist": True},
            {"name": "⚡│Co-Fundador", "color": "purple", "hoist": True},
            {"name": "🛡️│Administrador", "color": "red", "hoist": True},
            {"name": "⭐│Moderador", "color": "blue", "hoist": True},
            {"name": "🌟│VIP", "color": "orange", "hoist": True},
            {"name": "🎮│Gamer", "color": "green", "hoist": False},
            {"name": "🎨│Artista", "color": "pink", "hoist": False},
            {"name": "💻│Tech", "color": "cyan", "hoist": False},
            {"name": "📚│Leitor", "color": "teal", "hoist": False},
            {"name": "🎵│Músico", "color": "magenta", "hoist": False},
            {"name": "🏃│Esportista", "color": "dark_green", "hoist": False},
            {"name": "🍳│Chef", "color": "yellow", "hoist": False},
            {"name": "🤖│Bot", "color": "grey", "hoist": False},
            {"name": "🌍│Membro", "color": "default", "hoist": False}
        ],
        "categories": [
            {"name": "📢│INFORMAÇÕES", "position": 0},
            {"name": "💬│COMUNIDADE", "position": 1},
            {"name": "🎮│ENTRETENIMENTO", "position": 2},
            {"name": "🎤│VOICE CHAT", "position": 3},
            {"name": "🌍│INTERNACIONAL", "position": 4}
        ]
    },
    
    # ========== TEMPLATE ARTES CRIATIVAS ==========
    "artes": {
        "name": "🎨 Creative Hub",
        "emoji": "🎨",
        "description": "Comunidade para artistas, designers e criativos de todas as áreas",
        "channels": {
            "text": [
                {"name": "📢│anúncios", "topic": "📌 Anúncios importantes da comunidade"},
                {"name": "📜│regras", "topic": "⚖️ Regras para compartilhamento de arte"},
                {"name": "👋│boas-vindas", "topic": "🎉 Apresente-se e mostre seu trabalho!"},
                {"name": "🎯│introdução", "topic": "✨ Guia para novos artistas"},
                {"name": "💬│geral", "topic": "💭 Conversas gerais sobre arte"},
                {"name": "🎨│arte-digital", "topic": "🖥️ Photoshop, Illustrator, Procreate"},
                {"name": "🖌️│tradicional", "topic": "✏️ Pintura, desenho, escultura"},
                {"name": "🎭│conceito", "topic": "💡 Character design, concept art"},
                {"name": "📷│fotografia", "topic": "📸 Fotografia e edição"},
                {"name": "🎬│animação", "topic": "🎞️ Animação 2D/3D e motion graphics"},
                {"name": "🎵│musica", "topic": "🎧 Produção musical e composição"},
                {"name": "✍️│escrita", "topic": "📝 Poesia, contos, roteiros"},
                {"name": "💻│design", "topic": "🖋️ Design gráfico e UI/UX"},
                {"name": "🏗️│3d", "topic": "🔄 Modelagem 3D e renderização"},
                {"name": "💡│feedback", "topic": "👁️‍🗨️ Peça e dê feedback construtivo"},
                {"name": "🤝│colabs", "topic": "👥 Projetos colaborativos"},
                {"name": "💰│comissions", "topic": "💸 Informações sobre comissions"},
                {"name": "📚│recursos", "topic": "📖 Tutoriais, brushes, referências"},
                {"name": "🏆│portfólio", "topic": "⭐ Mostre seu melhor trabalho!"},
                {"name": "☕│descontração", "topic": "🎮 Hora do café e inspiração"}
            ],
            "voice": [
                {"name": "🎨│Sala de Arte", "user_limit": 0},
                {"name": "🎧│Foco Criativo", "user_limit": 5},
                {"name": "💭│Brainstorm", "user_limit": 8},
                {"name": "👁️│Feedback Live", "user_limit": 10},
                {"name": "🎵│Ouvindo Música", "user_limit": 5},
                {"name": "☕│Café Virtual", "user_limit": 10},
                {"name": "💤│AFK", "user_limit": 0}
            ],
            "stage": [
                {"name": "🎤│Workshop", "topic": "Workshops e demonstrações ao vivo"},
                {"name": "💡│Critique", "topic": "Sessões de crítica construtiva"}
            ]
        },
        "roles": [
            {"name": "👑│Fundador", "color": "gold", "hoist": True},
            {"name": "🎨│Artista Sênior", "color": "purple", "hoist": True},
            {"name": "🛡️│Moderador", "color": "blue", "hoist": True},
            {"name": "🎭│Character Designer", "color": "pink", "hoist": False},
            {"name": "🖥️│Digital Artist", "color": "cyan", "hoist": False},
            {"name": "🖌️│Traditional Artist", "color": "orange", "hoist": False},
            {"name": "📷│Fotógrafo", "color": "teal", "hoist": False},
            {"name": "🎬│Animador", "color": "magenta", "hoist": False},
            {"name": "🎵│Músico", "color": "green", "hoist": False},
            {"name": "✍️│Escritor", "color": "yellow", "hoist": False},
            {"name": "💻│Designer", "color": "red", "hoist": False},
            {"name": "🏗️│3D Artist", "color": "dark_blue", "hoist": False},
            {"name": "🤖│Bot", "color": "grey", "hoist": False},
            {"name": "🎨│Artista", "color": "default", "hoist": False}
        ],
        "categories": [
            {"name": "📢│INFORMAÇÕES", "position": 0},
            {"name": "🎨│ÁREAS CRIATIVAS", "position": 1},
            {"name": "💬│COMUNIDADE", "position": 2},
            {"name": "🎤│VOICE CHAT", "position": 3},
            {"name": "🏆│PORTFÓLIO", "position": 4}
        ]
    }
}

# Mapeamento de cores estendido
COLOR_MAP = {
    "red": 0xFF0000,
    "gold": 0xFFD700,
    "blue": 0x0000FF,
    "green": 0x00FF00,
    "purple": 0x800080,
    "orange": 0xFFA500,
    "pink": 0xFFC0CB,
    "teal": 0x008080,
    "cyan": 0x00FFFF,
    "magenta": 0xFF00FF,
    "yellow": 0xFFFF00,
    "dark_red": 0x8B0000,
    "dark_green": 0x006400,
    "dark_blue": 0x00008B,
    "light_blue": 0xADD8E6,
    "grey": 0x808080,
    "default": None
}