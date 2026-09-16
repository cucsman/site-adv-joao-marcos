# -*- coding: utf-8 -*-
"""Gera o site JMB trilíngue: /pt /en /es + detector na raiz. Saída: /home/claude/site-v3"""
import os, shutil

OUT = '/home/claude/site-v3'
BASE = 'https://www.jmbadv.com.br'
WA = 'https://wa.me/5511986213553'
WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor"><use href="#wa-path"/></svg>'
WA_SYMBOL = '''<svg style="display:none" xmlns="http://www.w3.org/2000/svg"><symbol id="wa-path" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5 0 1.47 1.07 2.9 1.22 3.1.15.2 2.1 3.2 5.1 4.49.71.31 1.27.49 1.7.63.72.23 1.37.2 1.88.12.57-.09 1.76-.72 2.01-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35M12.05 21.79h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.9-9.88a9.82 9.82 0 0 1 6.99 2.9 9.82 9.82 0 0 1 2.89 7c0 5.45-4.44 9.88-9.89 9.88m8.4-18.28A11.8 11.8 0 0 0 12.04 0C5.5 0 .16 5.33.16 11.89c0 2.1.55 4.14 1.59 5.94L.05 24l6.3-1.65a11.9 11.9 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.33 11.89-11.89 0-3.18-1.24-6.16-3.48-8.4"/></symbol></svg>'''

SCRIPT_BASE = '''<script>
document.getElementById('hamburger').addEventListener('click',function(){document.getElementById('navLinks').classList.toggle('open')});
document.querySelectorAll('#navLinks a').forEach(function(a){a.addEventListener('click',function(){document.getElementById('navLinks').classList.remove('open')})});
document.querySelectorAll('.faq-q').forEach(function(btn){btn.addEventListener('click',function(){var item=btn.parentElement;var answer=item.querySelector('.faq-a');var open=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(function(i){i.classList.remove('open');i.querySelector('.faq-a').style.maxHeight=null});if(!open){item.classList.add('open');answer.style.maxHeight=answer.scrollHeight+'px'}})});
document.querySelectorAll('[data-setlang]').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('jmb-lang',a.getAttribute('data-setlang'))}catch(e){}})});
</script>'''

SCRIPT_FORM = '''<script>
function enviarForm(e){e.preventDefault();var f=e.target;var msg=f.nome.value+' | '+f.assunto.value+'%0A'+encodeURIComponent(f.mensagem.value||'')+'%0A'+f.whatsapp.value;window.open('https://wa.me/5511986213553?text='+msg,'_blank');return false}
</script>'''

P = {  # ---------------- PORTUGUÊS ----------------
'lang':'pt','html_lang':'pt-BR',
'nav':[('criminal.html','Criminal'),('tributario.html','Tributário'),('internacional.html','Internacional'),('equipe.html','Equipe'),('noticias.html','Notícias'),('index.html#contato','Contato')],
'wa_default':'Ol%C3%A1%2C%20preciso%20falar%20com%20um%20advogado.','wa_urgente':'Urgente%3A%20preciso%20de%20um%20advogado%20criminal%20agora.','wa_empresa':'Ol%C3%A1%2C%20preciso%20falar%20sobre%20o%20caso%20da%20minha%20empresa.','wa_trib':'Ol%C3%A1%2C%20quero%20agendar%20uma%20an%C3%A1lise%20tribut%C3%A1ria.','wa_intl':'Hello%2C%20I%20need%20a%20criminal%20lawyer%20in%20Brazil.','wa_equipe':'Ol%C3%A1%2C%20gostaria%20de%20falar%20com%20a%20equipe.','wa_imprensa':'Ol%C3%A1%2C%20sou%20da%20imprensa.',
'wa_btn':'WhatsApp','wa_bar':'Falar no WhatsApp','logo_tag':'Advocacia e Consultoria',
'ft_nav':'Navegação','ft_contact':'Contato','ft_links':[('criminal.html','Advocacia Criminal'),('tributario.html','Advocacia Tributária'),('internacional.html','Internacional'),('equipe.html','Equipe'),('noticias.html','Notícias'),('index.html#contato','Contato')],
'ft_legal':'Conteúdo meramente informativo, em conformidade com o Provimento 205/2021 da OAB. Este site não constitui promessa de resultado.','ft_rights':'Todos os direitos reservados.',
# index
'ix_title':'Advogado Criminalista e Tributarista em São Paulo | João Marcos A. Batista',
'ix_desc':'Defesa criminal e tributária de alta complexidade em São Paulo. Do flagrante aos Tribunais Superiores, da autuação fiscal ao CARF. Atendimento pelo WhatsApp.',
'hero_eyebrow':'Advocacia Criminal e Tributária — São Paulo','hero_h1':'Defesa <em>criminal e tributária</em> em casos de alta complexidade.',
'hero_sub':'Do flagrante aos Tribunais Superiores. Da autuação fiscal ao CARF. Atuação desde 2014, com passagem pelo Ministério Público de São Paulo, pós-graduação em Direito Penal Econômico (FGV/SP) e escritório integrante da lista de advogados da Embaixada dos EUA no Brasil.',
'hero_badge':'Flagrantes e urgências — atendimento pelo WhatsApp','hero_cta1':'Falar com um advogado agora','hero_cta2':'Áreas de atuação',
'creds':[('OAB/SP 454.179','Inscrição ativa'),('Ministério Público','Passagem pelo MP de São Paulo'),('FGV/SP · PUC/RS','Pós em Penal Econômico e Finanças'),('IBCCRIM · IDDD · IBPT','Institutos de referência criminal e tributária'),('Embaixada dos EUA','Lista de advogados no Brasil')],
'urg_eyebrow':'Urgências criminais','urg_h2':'Prisão em flagrante?<br>As primeiras horas são decisivas.',
'urg_p1':'Após uma prisão em flagrante, a audiência de custódia acontece em até 24 horas — e é nela que se discute a liberdade. Contar com defesa técnica desde o primeiro momento faz diferença no rumo de todo o processo.',
'urg_p2':'Fale conosco pelo WhatsApp. Um advogado orienta a família, acompanha a lavratura do flagrante e atua na audiência de custódia.',
'urg_cta':'Falar no WhatsApp','urg_card':'O que fazer agora',
'urg_steps':['Não preste declarações sem a presença de um advogado.','Reúna documentos e informações básicas sobre a ocorrência.','Fale conosco pelo WhatsApp — orientamos os próximos passos.'],
'ar_eyebrow':'Áreas de atuação','ar_h2':'Dois pilares, uma mesma estratégia','ar_p':'Advocacia criminal e tributária com profundidade técnica — e domínio da interseção entre as duas.',
'ar_crim_h':'Advocacia Criminal','ar_crim_p':'Defesa em todas as fases — do inquérito e do flagrante aos recursos nos Tribunais Superiores, incluindo Tribunal do Júri e crimes econômicos.','ar_crim_a':'Ver atuação criminal →',
'ar_trib_h':'Advocacia Tributária','ar_trib_p':'Planejamento tributário, recuperação de créditos, parcelamentos estratégicos e contencioso administrativo e judicial — inclusive no CARF.','ar_trib_a':'Ver atuação tributária →',
'ar_intl_h':'Clientes Internacionais','ar_intl_p':'Defesa criminal de estrangeiros no Brasil, com atendimento em inglês e espanhol. Escritório integrante da lista de advogados da Embaixada dos EUA.','ar_intl_a':'International clients →',
'po_eyebrow':'Direito Penal Econômico','po_h2':'Quando o problema fiscal vira processo criminal',
'po_p1':'Autuações e execuções fiscais podem evoluir para acusações de crime contra a ordem tributária, lavagem de dinheiro e crimes contra o sistema financeiro. São poucas as bancas preparadas para atuar nos dois tabuleiros ao mesmo tempo.',
'po_p2':'É exatamente nessa interseção que o escritório concentra sua especialização: pós-graduação em Direito Penal Econômico pela FGV/SP, formação em Finanças pela PUC/RS e atuação simultânea no contencioso tributário e na defesa penal empresarial.',
'po_cta':'Falar sobre o caso da sua empresa',
'tl_eyebrow':'Como atuamos','tl_h2':'Do primeiro contato à decisão final',
'tl':[('Atendimento imediato','Análise do caso no primeiro contato, com orientação clara sobre riscos e caminhos possíveis.'),('Estratégia de defesa','Estudo aprofundado dos autos e definição da tese, sem soluções de prateleira.'),('Todas as instâncias','Audiências, sustentações orais, recursos e Habeas Corpus, inclusive no STJ e no STF, em Brasília.'),('Acompanhamento constante','Cliente e família informados a cada movimentação do processo, em linguagem acessível.')],
'in_eyebrow':'International Practice','in_h2':'Defesa criminal de estrangeiros no Brasil',
'in_p':'O escritório integra a lista de advogados da Embaixada e dos Consulados dos EUA no Brasil, com atuação em casos criminais envolvendo estrangeiros desde 2016 — em inglês, português e espanhol.',
'in_en':"Arrested or under investigation in Brazil? Our firm is included in the U.S. Embassy's list of attorneys in Brazil. We speak English and Spanish.",'in_a':'International clients →',
'nw_eyebrow':'Na mídia','nw_h2':'Notícias e reportagens','nw_p':'A atuação do escritório em casos de repercussão, registrada pela imprensa.','nw_read':'Ler matéria →','nw_all':'Ver todas as notícias →','nw_veiculo':'[Veículo]','nw_title':'[Título da reportagem sobre o caso]','nw_sum':'[Resumo em uma linha do que a matéria cobre.]',
'rv_eyebrow':'Avaliações','rv_h2':'O que dizem nossos clientes','rv_rating':'5,0 no Google · avaliações verificadas',
'rv1':'"Excelente atendimento desde o primeiro contato até a resolução do caso. Sempre muito solícito, tirando todas as dúvidas e nos deixando a par de tudo. Só tenho elogios e agradecimento."','rv1n':'Marta de Farias','rv1t':'',
'rv2':'"Obrigado por dedicar todo o seu esforço e habilidade, e por priorizar o caso. Você estava sempre cuidando. Conheci um excelente advogado."','rv2n':'Gandy Arias','rv2t':'Cliente internacional — Bolívia',
'rv3':'"Profissional dedicado e atencioso, sempre disponível para esclarecer dúvidas e acompanhar cada etapa do processo."','rv3n':'Avaliação no Google','rv3t':'[substituir por depoimento real do perfil]',
'rv_link':'Ver todas as avaliações no Google',
'fq_eyebrow':'Dúvidas frequentes','fq_h2':'Perguntas frequentes',
'faq_home':[('Meu familiar foi preso em flagrante. O que devo fazer primeiro?','Procure um advogado imediatamente e não incentive declarações sem defesa técnica presente. A audiência de custódia ocorre em até 24 horas e é o primeiro momento em que a liberdade pode ser discutida. Orientamos a família desde o primeiro contato pelo WhatsApp.'),('Minha empresa foi autuada pelo Fisco. O que fazer?','A autuação pode ser contestada administrativa e judicialmente — inclusive no CARF — e, em muitos casos, o passivo pode ser reduzido, parcelado ou compensado com créditos. O importante é agir dentro dos prazos de defesa. Em situações mais graves, a atuação conjunta com a defesa penal evita que a questão fiscal evolua para a esfera criminal.'),('O escritório atende fora de São Paulo?','Sim. A atuação é em todo o território nacional, incluindo Tribunais Superiores em Brasília. O atendimento inicial pode ser feito por videochamada ou WhatsApp.'),('Vocês atendem estrangeiros?','Sim. O escritório integra a lista de advogados da Embaixada dos EUA no Brasil e atende em inglês, português e espanhol, incluindo contato com familiares no exterior e representações consulares.'),('Como funciona a primeira consulta?','O caso é analisado com sigilo absoluto e o cliente recebe uma avaliação honesta dos riscos e das estratégias possíveis, com honorários definidos de forma transparente antes de qualquer contratação.')],
'ct_eyebrow':'Contato','ct_h2':'Fale com o escritório','ct_email':'E-mail','ct_addr':'Endereço','ct_map':'Ver no mapa →','ct_redes':'Redes',
'ct_f_nome':'Nome','ct_f_wa':'WhatsApp','ct_f_ass':'Assunto','ct_f_opts':['Criminal — urgência','Criminal','Tributário','Internacional / English','Outro'],'ct_f_msg':'Conte brevemente o seu caso (sigilo absoluto)','ct_f_lgpd':'Li e aceito a Política de Privacidade. Seus dados são tratados com sigilo, conforme a LGPD.','ct_f_btn':'Enviar mensagem','ct_f_micro':'Retornamos em até 1 hora em dias úteis. <b>Urgências: use o WhatsApp.</b>',
# criminal page
'cr_title':'Advocacia Criminal em São Paulo | João Marcos A. Batista','cr_desc':'Defesa criminal em todas as fases: flagrante, audiência de custódia, Tribunal do Júri, Habeas Corpus e Revisão Criminal.',
'cr_eyebrow':'Advocacia Criminal','cr_h1':'Defesa em <em>todas as fases</em> do processo penal.','cr_sub':'Do inquérito e da prisão em flagrante às sustentações no Tribunal do Júri e aos Habeas Corpus nos Tribunais Superiores — com estratégia definida caso a caso.','cr_cta':'Falar no WhatsApp',
'cr_urg_h2':'As primeiras 24 horas decidem muito','cr_urg_p':'Na prisão em flagrante, a audiência de custódia acontece em até 24 horas — é nela que se discute a liberdade. Atuamos desde a delegacia: orientação à família, acompanhamento da lavratura e defesa imediata na custódia.',
'cr_sub_eyebrow':'Frentes de atuação','cr_sub_h2':'Advocacia criminal completa',
'cr_cards':[('Direito Penal','Defesa em acusações de crimes financeiros, tráfico de entorpecentes, crimes sexuais, porte de arma, lesão corporal, crimes patrimoniais, receptação, estelionato e crimes contra a honra, entre outros.'),('Do flagrante até a liberdade','Acompanhamos todos os atos da prisão em flagrante e das investigações: defesas escritas e orais, audiências, sustentações e Habeas Corpus estratégicos nos Tribunais Superiores.'),('Tribunal do Júri','Defesa completa em crimes contra a vida — homicídio, infanticídio, aborto e instigação ou auxílio ao suicídio — conduzida por advogados experientes em plenário.'),('Erro judiciário','Em condenações definitivas injustas, com ou sem novas provas, atuamos com a Revisão Criminal para buscar a absolvição ou a redução da pena.'),('Defesa de vítimas','Atuação na defesa de vítimas de crimes, com destaque para violência doméstica, crimes sexuais, homicídios, ameaça e estelionato.'),('Empresas e compliance penal','Assessoria completa em compliance para matérias penais, incluindo crimes contra o sistema financeiro, e defesa de empresas vítimas de delitos como furto, apropriação indébita e estelionato.')],
'cr_faq':[('Advogado particular faz diferença em relação à defensoria?','A Defensoria Pública presta um serviço essencial, mas atende milhares de casos simultaneamente. A defesa particular permite dedicação integral ao caso, estratégia individualizada, acompanhamento constante da família e atuação rápida em cada prazo.'),('O que é a audiência de custódia?','É a audiência realizada em até 24 horas após a prisão em flagrante, na qual o juiz decide se a prisão será mantida, convertida em preventiva ou substituída pela liberdade. É o momento mais importante do início do caso.'),('Vocês atuam em processos já em andamento?','Sim. Assumimos casos em qualquer fase — inquérito, instrução, júri, recursos ou execução penal —, inclusive com Revisão Criminal de condenações definitivas.')],
'cr_band_h':'Precisa de defesa criminal?','cr_band_p':'Atendimento pelo WhatsApp. Sigilo absoluto desde a primeira conversa.','cr_band_b':'Falar com um advogado agora','cr_band_wa':'Ol%C3%A1%2C%20preciso%20de%20defesa%20criminal.',
# tributario page
'tb_title':'Advocacia Tributária Empresarial — CARF, Recuperação de Créditos | João Marcos A. Batista','tb_desc':'Planejamento tributário, recuperação de tributos, parcelamento de ICMS e contencioso no CARF.',
'tb_eyebrow':'Advocacia Tributária','tb_h1':'Estratégia fiscal para proteger o <em>caixa e o patrimônio</em> da sua empresa.','tb_sub':'Planejamento, recuperação de créditos, parcelamentos estratégicos e contencioso de alta complexidade — do processo administrativo e do CARF às ações judiciais.','tb_cta':'Agendar análise do caso',
'tb_why_eyebrow':'Por que o escritório','tb_why_h2':'Atuação tributária de alta complexidade',
'tb_why_p1':'O escritório atua em contencioso tributário administrativo e judicial — incluindo processos no CARF, execuções fiscais de valores relevantes e reestruturação do passivo de empresas em recuperação judicial.',
'tb_why_p2':'A base técnica combina pós-graduação em Direito Penal Econômico (FGV/SP), formação em Finanças, Investimentos e Banking (PUC/RS) e participação no Instituto Brasileiro de Planejamento e Tributação — o que permite tratar o problema fiscal como ele é: uma questão jurídica e financeira ao mesmo tempo.',
'tb_sv_eyebrow':'Serviços','tb_sv_h2':'Frentes de atuação tributária',
'tb_cards':[('Planejamento tributário e otimização da carga','Diagnóstico completo das obrigações fiscais da empresa e recomendação do regime tributário adequado. O foco é otimizar os tributos devidos, evitando pagamentos excessivos e aproveitando incentivos fiscais, isenções e oportunidades de redução.'),('Recuperação de tributos pagos indevidamente','Revisão detalhada de tributos como ICMS, PIS, COFINS e IPI para identificar valores pagos a mais e recuperá-los por compensação ou restituição junto aos órgãos competentes.'),('Parcelamento e empresas em recuperação','Negociação de parcelamentos de dívidas fiscais, como ICMS, junto à Secretaria da Fazenda, para empresas em recuperação judicial ou extrajudicial — com preservação do fluxo de caixa.'),('Contencioso tributário e defesa em ações fiscais','Defesa em autuações e litígios com o Fisco, contestando cobranças em ações administrativas e judiciais — inclusive no CARF — para evitar penalidades e proteger o patrimônio da empresa.')],
'tb_po_h2':'O diferencial: defesa fiscal e penal no mesmo escritório',
'tb_po_p1':'Autuações fiscais podem evoluir para acusações de crime contra a ordem tributária, lavagem de dinheiro e crimes contra o sistema financeiro — atingindo diretamente sócios e administradores.',
'tb_po_p2':'Aqui, a defesa tributária e a defesa penal empresarial caminham juntas desde o primeiro dia: a estratégia fiscal já nasce considerando os reflexos criminais, e vice-versa.',
'tb_faq':[('Minha empresa foi autuada. Quais são os caminhos?','A autuação pode ser contestada na esfera administrativa — inclusive no CARF — e depois judicialmente. Em muitos casos o passivo pode ser reduzido, parcelado ou compensado com créditos. O essencial é agir dentro dos prazos de defesa.'),('Minha empresa pode ter tributos a recuperar?','É comum — principalmente em ICMS, PIS/COFINS e IPI. A revisão fiscal dos últimos 5 anos identifica pagamentos indevidos que podem ser recuperados por compensação ou restituição.'),('Dívida fiscal pode virar caso criminal?','Pode. Determinadas condutas ligadas ao inadimplemento ou à apuração de tributos são tratadas como crime contra a ordem tributária. Por isso o escritório atua nas duas frentes de forma coordenada.')],
'tb_band_h':'Quanto a sua empresa está pagando a mais?','tb_band_p':'Análise inicial do cenário fiscal da empresa, com sigilo e retorno objetivo sobre riscos e oportunidades.','tb_band_b':'Agendar análise do caso',
# internacional page
'il_title':'Atuação Internacional — Lista de Advogados da Embaixada dos EUA | JMB Advocacia','il_desc':'Defesa criminal de estrangeiros no Brasil. Escritório na lista de advogados da Embaixada dos EUA. Atendimento em inglês e espanhol.',
'il_eyebrow':'International Practice','il_h1':'Defesa criminal de <em>estrangeiros</em> no Brasil.','il_sub':'O escritório integra a lista de advogados da Embaixada dos EUA no Brasil e representa cidadãos estrangeiros em casos criminais em todo o país — em inglês, português e espanhol.','il_cta':'Falar com um advogado agora',
'il_how_eyebrow':'Como ajudamos','il_how_h2':'Da prisão ao acompanhamento completo do caso',
'il_how_p1':'Desde 2016 o escritório representa cidadãos estrangeiros em casos criminais no Brasil — da prisão em flagrante e audiência de custódia ao Tribunal do Júri e aos recursos nos Tribunais Superiores, em Brasília.',
'il_how_p2':'Mantemos as famílias informadas no exterior, fazemos a ponte com as representações consulares e conduzimos cada etapa processual em português para que o cliente não precise se preocupar com isso.',
'il_how_box':'Em caso de prisão, fale conosco pelo WhatsApp: um advogado explica a situação no seu idioma e atua na audiência de custódia — que acontece em até 24 horas após a prisão no Brasil.',
'il_ar_eyebrow':'Frentes de atuação','il_ar_h2':'O que atendemos',
'il_cards':[('Prisões e audiências de custódia','Resposta imediata a prisões de estrangeiros em qualquer lugar do Brasil, com defesa na audiência de custódia e Habeas Corpus quando necessário.'),('Investigações e processos criminais','Defesa completa em investigações e processos, incluindo acusações relacionadas a drogas, crimes financeiros e Tribunal do Júri.'),('Crimes econômicos e tributários','Defesa em direito penal econômico: crimes contra o sistema financeiro, acusações de lavagem de dinheiro e crimes tributários envolvendo empresas e executivos.'),('Ponte consular e familiar','Comunicação constante com consulados e com a família do cliente no exterior, com atualizações do caso em inglês ou espanhol.')],
'il_band_h':'Preso ou investigado no Brasil?','il_band_p':'Fale conosco pelo WhatsApp. Um advogado criminalista fala com você no seu idioma e explica exatamente os próximos passos.','il_band_b':'WhatsApp — atendimento imediato',
# equipe page
'eq_title':'Equipe — João Marcos A. Batista Advocacia e Consultoria','eq_desc':'João Marcos A. Batista (OAB/SP 454.179), Leonardo Almeida Santos, Willian Moura Rodrigues e Gabriel Mantovani. Advocacia criminal e tributária em São Paulo.',
'eq_eyebrow':'Equipe','eq_h1':'Quem conduz a <em>sua defesa</em>.','eq_sub':'Uma equipe dedicada exclusivamente à advocacia criminal e tributária, liderada por João Marcos A. Batista.',
'eq_role':'Sócio-gestor',
'eq_bio1':'Advogado criminalista desde 2014. Iniciou a carreira no Fórum Criminal da Barra Funda e no Ministério Público de São Paulo, onde acompanhou de perto a rotina da acusação — experiência que hoje aplica na defesa, com destaque para crimes comuns, crimes econômicos e Tribunal do Júri.',
'eq_bio2':'Pós-graduado em Direito Penal Econômico pela FGV/SP e em Finanças, Investimentos e Banking pela PUC/RS. Conselheiro de Prerrogativas da OAB/SP, membro do IDDD, associado ao IBCCRIM e membro do Instituto Brasileiro de Planejamento e Tributação.',
'eq_bio3':'O escritório integra a lista de advogados da Embaixada dos EUA no Brasil, com atuação em casos criminais internacionais desde 2016.',
'eq_adv_eyebrow':'Advogados','eq_adv_h2':'Equipe jurídica',
'eq_o_role':'Advogado Cível e Criminal · OAB/SP 545.361','eq_o_bio':'Graduado pela FMU/SP, integra o escritório desde 2025, com atuação nas áreas cível e criminal e acompanhamento próximo de cada processo.',
'eq_at_eyebrow':'Atendimento','eq_at_h2':'Equipe de relacionamento','eq_at_p':'Profissionais que cuidam do primeiro contato, da organização do atendimento e da comunicação entre você e os advogados.','eq_w_role':'Gestão comercial e atendimento','eq_w_bio':'Responsável pela operação de atendimento do escritório e pela ponte entre o cliente e a equipe jurídica, do primeiro contato ao acompanhamento do caso. Graduado em Engenharia Mecânica pela FMU/SP.','eq_g_role':'Atendimento e relacionamento','eq_g_bio':'Atua no primeiro atendimento e na qualificação dos casos, garantindo clareza na comunicação e organização do fluxo até os advogados responsáveis.','eq_band_h':'Fale diretamente com a equipe','eq_band_p':'Atendimento com sigilo absoluto, em português, inglês ou espanhol.','eq_band_b':'Falar no WhatsApp',
# noticias page
'nt_title':'Notícias e Reportagens — João Marcos A. Batista Advocacia','nt_desc':'Reportagens e notícias sobre a atuação do escritório em casos criminais e tributários de repercussão.',
'nt_eyebrow':'Na mídia','nt_h1':'Notícias e <em>reportagens</em>.','nt_sub':'A atuação do escritório em casos de repercussão, registrada pela imprensa — além de artigos e análises sobre direito criminal e tributário.',
'nw_kind':{'tv':'Entrevista','doc':'Série','rep':'Reportagem','art':'Artigo'},'nw_watch':'Assistir →',
'nt_band_h':'Imprensa','nt_band_p':'Para entrevistas, comentários técnicos e análises sobre direito criminal e tributário, fale com o escritório.','nt_band_b':'Contato para imprensa',
}

E = dict(P)  # ---------------- ENGLISH ----------------
E.update({
'lang':'en','html_lang':'en',
'nav':[('criminal.html','Criminal'),('tributario.html','Tax'),('internacional.html','International'),('equipe.html','Team'),('noticias.html','News'),('index.html#contato','Contact')],
'wa_default':'Hello%2C%20I%20need%20to%20speak%20with%20a%20lawyer.','wa_urgente':'Urgent%3A%20I%20need%20a%20criminal%20lawyer%20in%20Brazil%20now.','wa_empresa':'Hello%2C%20I%20need%20to%20discuss%20my%20company%27s%20case.','wa_trib':'Hello%2C%20I%20would%20like%20a%20tax%20assessment%20review.','wa_intl':'Hello%2C%20I%20need%20a%20criminal%20lawyer%20in%20Brazil.','wa_equipe':'Hello%2C%20I%20would%20like%20to%20speak%20with%20the%20team.','wa_imprensa':'Hello%2C%20press%20inquiry.',
'wa_btn':'WhatsApp','wa_bar':'Talk on WhatsApp','logo_tag':'Attorneys at Law',
'ft_nav':'Navigation','ft_contact':'Contact','ft_links':[('criminal.html','Criminal Defense'),('tributario.html','Tax Law'),('internacional.html','International'),('equipe.html','Team'),('noticias.html','News'),('index.html#contato','Contact')],
'ft_legal':'Informational content only, in accordance with Brazilian Bar Association (OAB) Rule 205/2021. This website is not a promise of results.','ft_rights':'All rights reserved.',
'ix_title':'Criminal & Tax Lawyer in São Paulo, Brazil | João Marcos A. Batista','ix_desc':'High-stakes criminal and tax defense in Brazil. From arrest to the Superior Courts. U.S. Embassy attorney list. English and Spanish spoken.',
'hero_eyebrow':'Criminal & Tax Law — São Paulo, Brazil','hero_h1':'<em>Criminal and tax</em> defense for high-stakes cases.',
'hero_sub':"From arrest to Brazil's Superior Courts. From tax assessments to the CARF tribunal. Practicing since 2014, with experience at the São Paulo Prosecutor's Office, a graduate degree in Economic Criminal Law (FGV/SP), and inclusion in the U.S. Embassy's list of attorneys in Brazil.",
'hero_badge':'Arrests and emergencies — reach us on WhatsApp','hero_cta1':'Talk to a lawyer now','hero_cta2':'Practice areas',
'creds':[('OAB/SP 454.179','Active bar registration'),("Prosecutor's Office",'Experience at the São Paulo MP'),('FGV/SP · PUC/RS','Graduate degrees in Criminal Law & Finance'),('IBCCRIM · IDDD · IBPT','Leading criminal and tax law institutes'),('U.S. Embassy','Attorney list in Brazil')],
'urg_eyebrow':'Criminal emergencies','urg_h2':'Arrested in Brazil?<br>The first hours are decisive.',
'urg_p1':'After an arrest in flagrante, the custody hearing takes place within 24 hours — and that is where release is decided. Having a defense lawyer from the very first moment changes the course of the entire case.',
'urg_p2':'Reach us on WhatsApp. A lawyer guides the family, follows the arrest paperwork and acts at the custody hearing.',
'urg_cta':'Talk on WhatsApp','urg_card':'What to do now',
'urg_steps':['Do not give any statement without a lawyer present.','Gather basic documents and information about the incident.','Reach us on WhatsApp — we will guide you on the next steps.'],
'ar_eyebrow':'Practice areas','ar_h2':'Two pillars, one strategy','ar_p':'Criminal and tax law with technical depth — and command of the intersection between the two.',
'ar_crim_h':'Criminal Defense','ar_crim_p':'Defense at every stage — from investigation and arrest to appeals before the Superior Courts, including jury trials and financial crimes.','ar_crim_a':'Criminal practice →',
'ar_trib_h':'Tax Law','ar_trib_p':'Tax planning, credit recovery, strategic installment agreements and administrative and judicial litigation — including CARF.','ar_trib_a':'Tax practice →',
'ar_intl_h':'International Clients','ar_intl_p':"Criminal defense for foreign nationals in Brazil, in English and Spanish. Included in the U.S. Embassy's attorney list.",'ar_intl_a':'International clients →',
'po_eyebrow':'Economic Criminal Law','po_h2':'When a tax problem becomes a criminal case',
'po_p1':'Tax assessments and enforcement can evolve into charges of tax crimes, money laundering and crimes against the financial system. Few firms are prepared to play on both boards at once.',
'po_p2':'That intersection is exactly where the firm concentrates its expertise: a graduate degree in Economic Criminal Law (FGV/SP), training in Finance (PUC/RS), and simultaneous work in tax litigation and corporate criminal defense.',
'po_cta':"Discuss your company's case",
'tl_eyebrow':'How we work','tl_h2':'From first contact to final decision',
'tl':[('Immediate response','Case assessment at first contact, with clear guidance on risks and possible paths.'),('Defense strategy','In-depth study of the case files and a tailored thesis — no off-the-shelf solutions.'),('Every court level','Hearings, oral arguments, appeals and Habeas Corpus, including the STJ and STF in Brasília.'),('Constant updates','Client and family informed at every step of the case, in plain language.')],
'in_eyebrow':'International Practice','in_h2':'Criminal defense for foreign nationals in Brazil',
'in_p':"The firm is included in the U.S. Embassy and Consulates' list of attorneys in Brazil, and has handled criminal cases involving foreign nationals since 2016 — in English, Portuguese and Spanish.",
'in_en':'Arrested or under investigation in Brazil? Reach us on WhatsApp — we speak English and Spanish.','in_a':'International clients →',
'nw_eyebrow':'In the press','nw_h2':'News and coverage','nw_p':"The firm's work in high-profile cases, as covered by the press.",'nw_read':'Read article →','nw_all':'All news →','nw_veiculo':'[Outlet]','nw_title':'[Headline of the story]','nw_sum':'[One line on the case and our role.]',
'rv_eyebrow':'Reviews','rv_h2':'What our clients say','rv_rating':'5.0 on Google · verified reviews',
'rv1':'"Excellent service from the first contact to the resolution of the case. Always available, answering every question and keeping us informed of everything."','rv1n':'Marta de Farias','rv1t':'',
'rv2':'"Thank you for dedicating all your effort and skill, and for prioritizing the case. You were always taking care of us. I met an excellent lawyer."','rv2n':'Gandy Arias','rv2t':'International client — Bolivia',
'rv3':'"A dedicated and attentive professional, always available to answer questions and follow every stage of the case."','rv3n':'Google review','rv3t':'[replace with a real review]',
'rv_link':'See all reviews on Google',
'fq_eyebrow':'FAQ','fq_h2':'Frequently asked questions',
'faq_home':[('A family member was arrested in Brazil. What should I do first?','Contact a lawyer immediately and do not encourage any statement without defense counsel present. The custody hearing happens within 24 hours and is the first moment release can be argued. We guide families from the first contact on WhatsApp.'),('My company received a tax assessment. What now?','The assessment can be challenged administratively — including before CARF — and in court. In many cases the liability can be reduced, paid in installments or offset with credits. Acting within the defense deadlines is essential.'),('Do you handle cases outside São Paulo?','Yes. We act nationwide, including before the Superior Courts in Brasília. Initial consultations can be held by video call or WhatsApp.'),('Do you work with foreign clients?',"Yes. The firm is included in the U.S. Embassy's attorney list in Brazil and works in English, Portuguese and Spanish, including liaison with families abroad and consular offices."),('How does the first consultation work?','Your case is reviewed in strict confidence and you receive an honest assessment of risks and possible strategies, with fees set transparently before any engagement.')],
'ct_eyebrow':'Contact','ct_h2':'Contact the firm','ct_email':'E-mail','ct_addr':'Address','ct_map':'View on map →','ct_redes':'Social',
'ct_f_nome':'Name','ct_f_wa':'WhatsApp / phone','ct_f_ass':'Subject','ct_f_opts':['Criminal — urgent','Criminal','Tax','International','Other'],'ct_f_msg':'Briefly describe your case (strictly confidential)','ct_f_lgpd':'I have read and accept the Privacy Policy. Your data is handled confidentially under Brazilian data protection law (LGPD).','ct_f_btn':'Send message','ct_f_micro':'We reply within 1 hour on business days. <b>Emergencies: use WhatsApp.</b>',
'cr_title':'Criminal Defense in Brazil | João Marcos A. Batista','cr_desc':'Criminal defense at every stage: arrest, custody hearing, jury trial, Habeas Corpus and post-conviction review.',
'cr_eyebrow':'Criminal Defense','cr_h1':'Defense at <em>every stage</em> of the criminal case.','cr_sub':'From investigation and arrest to jury trials and Habeas Corpus before the Superior Courts — with a strategy built case by case.','cr_cta':'Talk on WhatsApp',
'cr_urg_h2':'The first 24 hours decide a lot','cr_urg_p':'After an arrest in flagrante, the custody hearing happens within 24 hours — that is where release is argued. We act from the police station on: guiding the family, following the paperwork, and defending at the hearing.',
'cr_sub_eyebrow':'Practice fronts','cr_sub_h2':'Full-service criminal defense',
'cr_cards':[('Criminal Law','Defense against charges of financial crimes, drug offenses, sexual offenses, weapons possession, bodily harm, property crimes, fraud and defamation, among others.'),('From arrest to release','We follow every step of the arrest and investigation: written and oral defenses, hearings, oral arguments, and strategic Habeas Corpus before the Superior Courts.'),('Jury trials','Complete defense in crimes against life — homicide, infanticide, abortion and assisted suicide — led by lawyers experienced in the courtroom.'),('Wrongful convictions','In unjust final convictions, with or without new evidence, we pursue Criminal Review to seek acquittal or sentence reduction.'),('Victim representation','Representation of crime victims, with emphasis on domestic violence, sexual offenses, homicide, threats and fraud.'),('Corporate criminal compliance','Full compliance counsel for criminal matters, including crimes against the financial system, and defense of companies victimized by theft, embezzlement and fraud.')],
'cr_faq':[('Does a private lawyer make a difference versus the public defender?','Public defenders provide an essential service but handle thousands of cases at once. Private defense allows full dedication, an individualized strategy, constant updates to the family, and fast action on every deadline.'),('What is the custody hearing?','It is the hearing held within 24 hours of an arrest in flagrante, where the judge decides whether the arrest is upheld, converted into pre-trial detention, or replaced with release. It is the most important moment at the start of the case.'),('Do you take over ongoing cases?','Yes. We take cases at any stage — investigation, trial, jury, appeals or sentence enforcement — including Criminal Review of final convictions.')],
'cr_band_h':'Need criminal defense in Brazil?','cr_band_p':'Reach us on WhatsApp. Strict confidentiality from the first conversation. English and Spanish spoken.','cr_band_b':'Talk to a lawyer now','cr_band_wa':'Hello%2C%20I%20need%20criminal%20defense%20in%20Brazil.',
'tb_title':'Tax Law in Brazil — CARF, Tax Recovery | João Marcos A. Batista','tb_desc':'Tax planning, recovery of overpaid taxes, ICMS installment agreements and litigation before CARF.',
'tb_eyebrow':'Tax Law','tb_h1':"Tax strategy to protect your company's <em>cash and assets</em>.",'tb_sub':'Planning, credit recovery, strategic installment agreements and high-stakes litigation — from administrative proceedings and CARF to the courts.','tb_cta':'Request a case review',
'tb_why_eyebrow':'Why this firm','tb_why_h2':'High-stakes tax practice',
'tb_why_p1':'The firm litigates tax matters at the administrative and judicial levels — including CARF proceedings, high-value tax enforcement actions, and restructuring of tax liabilities for companies in judicial reorganization.',
'tb_why_p2':'The technical base combines a graduate degree in Economic Criminal Law (FGV/SP), training in Finance, Investments and Banking (PUC/RS), and membership in the Brazilian Institute of Tax Planning — treating a tax problem as what it is: a legal and financial question at once.',
'tb_sv_eyebrow':'Services','tb_sv_h2':'Tax practice fronts',
'tb_cards':[('Tax planning and burden optimization','Complete diagnosis of the company\'s tax obligations and recommendation of the right tax regime — optimizing taxes due, avoiding overpayment, and using incentives, exemptions and reduction opportunities.'),('Recovery of overpaid taxes','Detailed review of taxes such as ICMS, PIS, COFINS and IPI to identify overpayments and recover them through offset or refund before the competent authorities.'),('Installments and companies in reorganization','Negotiation of tax debt installment agreements, such as ICMS, with the State Treasury for companies in judicial or extrajudicial reorganization — preserving cash flow.'),('Tax litigation and defense','Defense against assessments and disputes with tax authorities, challenging charges in administrative and judicial proceedings — including CARF — to avoid penalties and protect company assets.')],
'tb_po_h2':'The differential: tax and criminal defense in one firm',
'tb_po_p1':'Tax assessments can evolve into charges of tax crimes, money laundering and crimes against the financial system — reaching partners and executives directly.',
'tb_po_p2':'Here, tax defense and corporate criminal defense move together from day one: the tax strategy is built with its criminal implications in mind, and vice versa.',
'tb_faq':[('My company was assessed. What are the options?','The assessment can be challenged administratively — including before CARF — and then in court. In many cases the liability can be reduced, paid in installments or offset with credits. Acting within the defense deadlines is essential.'),('Could my company have taxes to recover?','It is common — especially ICMS, PIS/COFINS and IPI. A review of the last 5 years identifies overpayments recoverable through offset or refund.'),('Can tax debt become a criminal case?','Yes. Certain conduct related to non-payment or tax reporting is treated as a crime against the tax order, reaching partners and executives. That is why the firm works both fronts in a coordinated way.')],
'tb_band_h':'How much is your company overpaying?','tb_band_p':'Initial review of the company\'s tax scenario, confidential, with an objective read on risks and opportunities.','tb_band_b':'Request a case review',
'il_title':'Criminal Lawyer for Foreigners in Brazil — U.S. Embassy Attorney List | JMB Law','il_desc':'Criminal defense for foreign nationals in Brazil. U.S. Embassy attorney list. English and Spanish spoken.',
'il_eyebrow':'International Practice','il_h1':'Criminal defense for <em>foreign nationals</em> in Brazil.','il_sub':"Our firm is included in the U.S. Embassy's list of attorneys in Brazil and represents foreign nationals in criminal cases nationwide — in English, Portuguese and Spanish.",'il_cta':'Talk to a lawyer now',
'il_how_eyebrow':'How we help','il_how_h2':'From arrest to full case representation',
'il_how_p1':'Since 2016 the firm has represented foreign citizens in criminal cases in Brazil — from arrest in flagrante and custody hearings to jury trials and appeals before the Superior Courts in Brasília.',
'il_how_p2':"We keep families informed abroad, liaise with consular representations, and handle every procedural step in Portuguese so you don't have to.",
'il_how_box':'In case of arrest, reach us on WhatsApp: a lawyer explains the situation in English, and acts at the custody hearing — which happens within 24 hours of an arrest in Brazil.',
'il_ar_eyebrow':'Practice areas','il_ar_h2':'What we handle',
'il_cards':[('Arrests & custody hearings','Immediate response to arrests of foreign nationals anywhere in Brazil, with defense at the custody hearing and habeas corpus petitions when needed.'),('Investigations & trials','Full defense in criminal investigations and proceedings, including drug-related charges, financial crimes and jury trials.'),('White-collar & tax matters','Defense in economic criminal law: crimes against the financial system, money laundering allegations and tax-related criminal charges.'),('Consular & family liaison',"Ongoing communication with consulates and the client's family abroad, with case updates in English or Spanish at every stage.")],
'il_band_h':'Arrested or under investigation in Brazil?','il_band_p':'Reach us on WhatsApp. A criminal lawyer will speak with you in English and explain exactly what happens next.','il_band_b':'WhatsApp — English spoken',
'eq_title':'Team — João Marcos A. Batista Attorneys at Law','eq_desc':'Meet the team: João Marcos A. Batista (OAB/SP 454.179), Leonardo Almeida Santos, Willian Moura Rodrigues and Gabriel Mantovani.',
'eq_eyebrow':'Team','eq_h1':'The people behind <em>your defense</em>.','eq_sub':'A team dedicated exclusively to criminal and tax law, led by João Marcos A. Batista.',
'eq_role':'Managing Partner',
'eq_bio1':"A criminal lawyer since 2014. He began his career at the Barra Funda Criminal Courthouse and the São Paulo Prosecutor's Office, where he learned the prosecution's playbook from the inside — experience he now applies to the defense, with emphasis on common crimes, financial crimes and jury trials.",
'eq_bio2':'Graduate degrees in Economic Criminal Law (FGV/SP) and in Finance, Investments and Banking (PUC/RS). Prerogatives Counselor at the São Paulo Bar (OAB/SP), member of IDDD, associate of IBCCRIM, and member of the Brazilian Institute of Tax Planning.',
'eq_bio3':"The firm is included in the U.S. Embassy's attorney list in Brazil, handling international criminal cases since 2016.",
'eq_adv_eyebrow':'Lawyers','eq_adv_h2':'Legal team',
'eq_o_role':'Civil & Criminal Lawyer · OAB/SP 545.361','eq_o_bio':'Graduated from FMU/SP, with the firm since 2025, working in civil and criminal matters with close follow-up of every case.',
'eq_at_eyebrow':'Client services','eq_at_h2':'Client relations team','eq_at_p':'The people who handle first contact, organize your case intake and keep communication flowing between you and the lawyers.','eq_w_role':'Client services & operations','eq_w_bio':'Runs the firm\'s client-service operation and acts as the bridge between clients and the legal team, from first contact to case follow-up. Mechanical Engineering degree from FMU/SP.','eq_g_role':'Client intake & relations','eq_g_bio':'Handles first contact and case intake, ensuring clear communication and an organized hand-off to the responsible lawyers.','eq_band_h':'Speak directly with the team','eq_band_p':'Strictly confidential, in English, Portuguese or Spanish.','eq_band_b':'WhatsApp',
'nt_title':'News & Press — João Marcos A. Batista Attorneys at Law','nt_desc':"Press coverage of the firm's work in high-profile criminal and tax cases.",
'nt_eyebrow':'In the press','nt_h1':'News and <em>coverage</em>.','nt_sub':"The firm's work in high-profile cases as covered by the press — plus articles and analysis on criminal and tax law.",
'nw_kind':{'tv':'Interview','doc':'Series','rep':'Coverage','art':'Article'},'nw_watch':'Watch →',
'nt_band_h':'Press','nt_band_p':'For interviews, expert commentary and analysis on criminal and tax law, contact the firm.','nt_band_b':'Press contact',
})

S = dict(P)  # ---------------- ESPAÑOL ----------------
S.update({
'lang':'es','html_lang':'es',
'nav':[('criminal.html','Penal'),('tributario.html','Tributario'),('internacional.html','Internacional'),('equipe.html','Equipo'),('noticias.html','Noticias'),('index.html#contato','Contacto')],
'wa_default':'Hola%2C%20necesito%20hablar%20con%20un%20abogado.','wa_urgente':'Urgente%3A%20necesito%20un%20abogado%20penalista%20en%20Brasil%20ahora.','wa_empresa':'Hola%2C%20necesito%20hablar%20sobre%20el%20caso%20de%20mi%20empresa.','wa_trib':'Hola%2C%20quiero%20agendar%20un%20an%C3%A1lisis%20tributario.','wa_intl':'Hola%2C%20necesito%20un%20abogado%20penalista%20en%20Brasil.','wa_equipe':'Hola%2C%20quisiera%20hablar%20con%20el%20equipo.','wa_imprensa':'Hola%2C%20soy%20de%20la%20prensa.',
'wa_btn':'WhatsApp','wa_bar':'Hablar por WhatsApp','logo_tag':'Abogados',
'ft_nav':'Navegación','ft_contact':'Contacto','ft_links':[('criminal.html','Derecho Penal'),('tributario.html','Derecho Tributario'),('internacional.html','Internacional'),('equipe.html','Equipo'),('noticias.html','Noticias'),('index.html#contato','Contacto')],
'ft_legal':'Contenido meramente informativo, conforme a la norma 205/2021 del Colegio de Abogados de Brasil (OAB). Este sitio no constituye promesa de resultado.','ft_rights':'Todos los derechos reservados.',
'ix_title':'Abogado Penalista y Tributarista en São Paulo, Brasil | João Marcos A. Batista','ix_desc':'Defensa penal y tributaria de alta complejidad en Brasil. De la detención a los Tribunales Superiores. Lista de abogados de la Embajada de EE.UU. Atención en español.',
'hero_eyebrow':'Derecho Penal y Tributario — São Paulo, Brasil','hero_h1':'Defensa <em>penal y tributaria</em> en casos de alta complejidad.',
'hero_sub':'De la detención en flagrancia a los Tribunales Superiores de Brasil. De la liquidación fiscal al tribunal CARF. En ejercicio desde 2014, con experiencia en la Fiscalía de São Paulo, posgrado en Derecho Penal Económico (FGV/SP) y despacho incluido en la lista de abogados de la Embajada de EE.UU. en Brasil.',
'hero_badge':'Detenciones y urgencias — atención por WhatsApp','hero_cta1':'Hablar con un abogado ahora','hero_cta2':'Áreas de práctica',
'creds':[('OAB/SP 454.179','Colegiatura activa'),('Fiscalía','Experiencia en la Fiscalía de São Paulo'),('FGV/SP · PUC/RS','Posgrados en Penal Económico y Finanzas'),('IBCCRIM · IDDD · IBPT','Institutos de referencia penal y tributaria'),('Embajada de EE.UU.','Lista de abogados en Brasil')],
'urg_eyebrow':'Urgencias penales','urg_h2':'¿Detenido en Brasil?<br>Las primeras horas son decisivas.',
'urg_p1':'Tras una detención en flagrancia, la audiencia de custodia se realiza dentro de las 24 horas — y es allí donde se discute la libertad. Contar con defensa técnica desde el primer momento cambia el rumbo de todo el proceso.',
'urg_p2':'Contáctenos por WhatsApp. Un abogado orienta a la familia, acompaña el registro de la detención y actúa en la audiencia de custodia.',
'urg_cta':'Hablar por WhatsApp','urg_card':'Qué hacer ahora',
'urg_steps':['No declare sin la presencia de un abogado.','Reúna documentos e información básica sobre el hecho.','Contáctenos por WhatsApp — le orientamos sobre los próximos pasos.'],
'ar_eyebrow':'Áreas de práctica','ar_h2':'Dos pilares, una misma estrategia','ar_p':'Derecho penal y tributario con profundidad técnica — y dominio de la intersección entre ambos.',
'ar_crim_h':'Derecho Penal','ar_crim_p':'Defensa en todas las etapas — de la investigación y la detención a los recursos ante los Tribunales Superiores, incluidos el jurado y los delitos económicos.','ar_crim_a':'Ver práctica penal →',
'ar_trib_h':'Derecho Tributario','ar_trib_p':'Planificación fiscal, recuperación de créditos, acuerdos de pago estratégicos y litigio administrativo y judicial — incluido el CARF.','ar_trib_a':'Ver práctica tributaria →',
'ar_intl_h':'Clientes Internacionales','ar_intl_p':'Defensa penal de extranjeros en Brasil, con atención en español e inglés. Despacho incluido en la lista de abogados de la Embajada de EE.UU.','ar_intl_a':'Clientes internacionales →',
'po_eyebrow':'Derecho Penal Económico','po_h2':'Cuando el problema fiscal se vuelve un caso penal',
'po_p1':'Las liquidaciones y ejecuciones fiscales pueden evolucionar a acusaciones de delitos tributarios, lavado de dinero y delitos contra el sistema financiero. Pocos despachos están preparados para jugar en los dos tableros a la vez.',
'po_p2':'Es exactamente en esa intersección donde el despacho concentra su especialización: posgrado en Derecho Penal Económico (FGV/SP), formación en Finanzas (PUC/RS) y actuación simultánea en litigio tributario y defensa penal corporativa.',
'po_cta':'Hablar sobre el caso de su empresa',
'tl_eyebrow':'Cómo trabajamos','tl_h2':'Del primer contacto a la decisión final',
'tl':[('Atención inmediata','Análisis del caso en el primer contacto, con orientación clara sobre riesgos y caminos posibles.'),('Estrategia de defensa','Estudio profundo del expediente y definición de la tesis, sin soluciones de estante.'),('Todas las instancias','Audiencias, alegatos orales, recursos y Habeas Corpus, incluso ante el STJ y el STF, en Brasilia.'),('Seguimiento constante','Cliente y familia informados en cada movimiento del proceso, en lenguaje claro.')],
'in_eyebrow':'Práctica Internacional','in_h2':'Defensa penal de extranjeros en Brasil',
'in_p':'El despacho integra la lista de abogados de la Embajada y los Consulados de EE.UU. en Brasil, con actuación en casos penales de extranjeros desde 2016 — en español, portugués e inglés.',
'in_en':'¿Detenido o investigado en Brasil? Contáctenos por WhatsApp — hablamos español e inglés.','in_a':'Clientes internacionales →',
'nw_eyebrow':'En la prensa','nw_h2':'Noticias y reportajes','nw_p':'La actuación del despacho en casos de repercusión, registrada por la prensa.','nw_read':'Leer nota →','nw_all':'Todas las noticias →','nw_veiculo':'[Medio]','nw_title':'[Titular del reportaje]','nw_sum':'[Una línea sobre el caso y nuestro papel.]',
'rv_eyebrow':'Reseñas','rv_h2':'Lo que dicen nuestros clientes','rv_rating':'5,0 en Google · reseñas verificadas',
'rv1':'"Excelente atención desde el primer contacto hasta la resolución del caso. Siempre disponible, resolviendo todas las dudas y manteniéndonos informados de todo."','rv1n':'Marta de Farias','rv1t':'',
'rv2':'"Gracias por dedicar todo su esfuerzo y habilidad, y por priorizar el caso. Siempre estaba cuidando de nosotros. Conocí a un excelente abogado."','rv2n':'Gandy Arias','rv2t':'Cliente internacional — Bolivia',
'rv3':'"Profesional dedicado y atento, siempre disponible para aclarar dudas y acompañar cada etapa del proceso."','rv3n':'Reseña en Google','rv3t':'[reemplazar por reseña real]',
'rv_link':'Ver todas las reseñas en Google',
'fq_eyebrow':'Preguntas frecuentes','fq_h2':'Preguntas frecuentes',
'faq_home':[('Un familiar fue detenido en Brasil. ¿Qué hago primero?','Contacte a un abogado de inmediato y no permita declaraciones sin defensa presente. La audiencia de custodia ocurre dentro de las 24 horas y es el primer momento en que puede discutirse la libertad. Orientamos a la familia desde el primer contacto por WhatsApp.'),('Mi empresa recibió una liquidación fiscal. ¿Qué hacer?','La liquidación puede impugnarse en vía administrativa — incluso ante el CARF — y judicial. En muchos casos el pasivo puede reducirse, fraccionarse o compensarse con créditos. Lo esencial es actuar dentro de los plazos de defensa.'),('¿Atienden fuera de São Paulo?','Sí. Actuamos en todo Brasil, incluidos los Tribunales Superiores en Brasilia. La primera consulta puede hacerse por videollamada o WhatsApp.'),('¿Atienden a extranjeros?','Sí. El despacho integra la lista de abogados de la Embajada de EE.UU. en Brasil y atiende en español, portugués e inglés, incluido el contacto con familiares en el exterior y oficinas consulares.'),('¿Cómo funciona la primera consulta?','El caso se analiza con absoluta confidencialidad y el cliente recibe una evaluación honesta de los riesgos y estrategias posibles, con honorarios definidos de forma transparente antes de cualquier contratación.')],
'ct_eyebrow':'Contacto','ct_h2':'Hable con el despacho','ct_email':'E-mail','ct_addr':'Dirección','ct_map':'Ver en el mapa →','ct_redes':'Redes',
'ct_f_nome':'Nombre','ct_f_wa':'WhatsApp / teléfono','ct_f_ass':'Asunto','ct_f_opts':['Penal — urgencia','Penal','Tributario','Internacional','Otro'],'ct_f_msg':'Cuente brevemente su caso (confidencialidad absoluta)','ct_f_lgpd':'He leído y acepto la Política de Privacidad. Sus datos se tratan con confidencialidad conforme a la ley brasileña de protección de datos (LGPD).','ct_f_btn':'Enviar mensaje','ct_f_micro':'Respondemos dentro de 1 hora en días hábiles. <b>Urgencias: use el WhatsApp.</b>',
'cr_title':'Defensa Penal en Brasil | João Marcos A. Batista','cr_desc':'Defensa penal en todas las etapas: detención, audiencia de custodia, jurado, Habeas Corpus y revisión criminal.',
'cr_eyebrow':'Derecho Penal','cr_h1':'Defensa en <em>todas las etapas</em> del proceso penal.','cr_sub':'De la investigación y la detención en flagrancia a los alegatos ante el jurado y los Habeas Corpus ante los Tribunales Superiores — con estrategia definida caso a caso.','cr_cta':'Hablar por WhatsApp',
'cr_urg_h2':'Las primeras 24 horas deciden mucho','cr_urg_p':'En la detención en flagrancia, la audiencia de custodia ocurre dentro de las 24 horas — allí se discute la libertad. Actuamos desde la comisaría: orientación a la familia, seguimiento del registro y defensa inmediata en la audiencia.',
'cr_sub_eyebrow':'Frentes de actuación','cr_sub_h2':'Defensa penal completa',
'cr_cards':[('Derecho Penal','Defensa ante acusaciones de delitos financieros, tráfico de drogas, delitos sexuales, porte de armas, lesiones, delitos patrimoniales, receptación, estafa y delitos contra el honor, entre otros.'),('De la detención a la libertad','Acompañamos todos los actos de la detención y la investigación: defensas escritas y orales, audiencias, alegatos y Habeas Corpus estratégicos ante los Tribunales Superiores.'),('Tribunal del Jurado','Defensa completa en delitos contra la vida — homicidio, infanticidio, aborto e instigación o auxilio al suicidio — conducida por abogados con experiencia en sala.'),('Error judicial','En condenas firmes injustas, con o sin nuevas pruebas, actuamos con la Revisión Criminal para buscar la absolución o la reducción de la pena.'),('Defensa de víctimas','Representación de víctimas de delitos, con énfasis en violencia doméstica, delitos sexuales, homicidios, amenazas y estafas.'),('Empresas y compliance penal','Asesoría completa en compliance penal, incluidos los delitos contra el sistema financiero, y defensa de empresas víctimas de hurto, apropiación indebida y estafa.')],
'cr_faq':[('¿Un abogado particular hace diferencia frente al defensor público?','La defensoría pública presta un servicio esencial, pero atiende miles de casos a la vez. La defensa particular permite dedicación integral, estrategia individualizada, información constante a la familia y acción rápida en cada plazo.'),('¿Qué es la audiencia de custodia?','Es la audiencia realizada dentro de las 24 horas de la detención en flagrancia, donde el juez decide si la prisión se mantiene, se convierte en preventiva o se sustituye por la libertad. Es el momento más importante del inicio del caso.'),('¿Toman casos ya en curso?','Sí. Asumimos casos en cualquier etapa — investigación, juicio, jurado, recursos o ejecución penal —, incluida la Revisión Criminal de condenas firmes.')],
'cr_band_h':'¿Necesita defensa penal en Brasil?','cr_band_p':'Atención por WhatsApp. Confidencialidad absoluta desde la primera conversación. Hablamos español.','cr_band_b':'Hablar con un abogado ahora','cr_band_wa':'Hola%2C%20necesito%20defensa%20penal%20en%20Brasil.',
'tb_title':'Derecho Tributario en Brasil — CARF, Recuperación de Impuestos | João Marcos A. Batista','tb_desc':'Planificación fiscal, recuperación de impuestos pagados de más, acuerdos de pago de ICMS y litigio ante el CARF.',
'tb_eyebrow':'Derecho Tributario','tb_h1':'Estrategia fiscal para proteger la <em>caja y el patrimonio</em> de su empresa.','tb_sub':'Planificación, recuperación de créditos, acuerdos de pago estratégicos y litigio de alta complejidad — del proceso administrativo y el CARF a los tribunales.','tb_cta':'Agendar análisis del caso',
'tb_why_eyebrow':'Por qué este despacho','tb_why_h2':'Práctica tributaria de alta complejidad',
'tb_why_p1':'El despacho litiga en materia tributaria administrativa y judicial — incluidos procesos ante el CARF, ejecuciones fiscales de montos relevantes y reestructuración del pasivo de empresas en reorganización judicial.',
'tb_why_p2':'La base técnica combina posgrado en Derecho Penal Económico (FGV/SP), formación en Finanzas (PUC/RS) y membresía en el Instituto Brasileño de Planificación Tributaria — tratando el problema fiscal como lo que es: una cuestión jurídica y financiera a la vez.',
'tb_sv_eyebrow':'Servicios','tb_sv_h2':'Frentes de actuación tributaria',
'tb_cards':[('Planificación fiscal y optimización de la carga','Diagnóstico completo de las obligaciones fiscales de la empresa y recomendación del régimen adecuado — optimizando los tributos debidos, evitando pagos excesivos y aprovechando incentivos y exenciones.'),('Recuperación de impuestos pagados de más','Revisión detallada de tributos como ICMS, PIS, COFINS e IPI para identificar pagos en exceso y recuperarlos por compensación o devolución ante los órganos competentes.'),('Acuerdos de pago y empresas en reorganización','Negociación de fraccionamientos de deudas fiscales, como ICMS, ante la Hacienda estatal para empresas en reorganización judicial o extrajudicial — preservando el flujo de caja.'),('Litigio tributario y defensa fiscal','Defensa ante liquidaciones y litigios con el Fisco, impugnando cobros en vía administrativa y judicial — incluido el CARF — para evitar sanciones y proteger el patrimonio.')],
'tb_po_h2':'El diferencial: defensa fiscal y penal en el mismo despacho',
'tb_po_p1':'Las liquidaciones fiscales pueden evolucionar a acusaciones de delitos tributarios, lavado de dinero y delitos contra el sistema financiero — alcanzando directamente a socios y administradores.',
'tb_po_p2':'Aquí, la defensa tributaria y la defensa penal corporativa caminan juntas desde el primer día: la estrategia fiscal nace considerando sus reflejos penales, y viceversa.',
'tb_faq':[('Mi empresa fue liquidada por el Fisco. ¿Cuáles son los caminos?','La liquidación puede impugnarse en vía administrativa — incluso ante el CARF — y luego judicial. En muchos casos el pasivo puede reducirse, fraccionarse o compensarse con créditos. Lo esencial es actuar dentro de los plazos.'),('¿Mi empresa puede tener impuestos por recuperar?','Es común — sobre todo ICMS, PIS/COFINS e IPI. La revisión fiscal de los últimos 5 años identifica pagos indebidos recuperables por compensación o devolución.'),('¿Una deuda fiscal puede volverse un caso penal?','Sí. Ciertas conductas ligadas al impago o a la declaración de tributos se tratan como delito contra el orden tributario. Por eso el despacho actúa en los dos frentes de forma coordinada.')],
'tb_band_h':'¿Cuánto está pagando de más su empresa?','tb_band_p':'Análisis inicial del escenario fiscal de la empresa, confidencial y con una lectura objetiva de riesgos y oportunidades.','tb_band_b':'Agendar análisis del caso',
'il_title':'Abogado Penalista para Extranjeros en Brasil — Lista de la Embajada de EE.UU. | JMB','il_desc':'Defensa penal de extranjeros en Brasil. Lista de abogados de la Embajada de EE.UU. Atención en español.',
'il_eyebrow':'Práctica Internacional','il_h1':'Defensa penal de <em>extranjeros</em> en Brasil.','il_sub':'El despacho integra la lista de abogados de la Embajada de EE.UU. en Brasil y representa a ciudadanos extranjeros en casos penales en todo el país — en español, portugués e inglés.','il_cta':'Hablar con un abogado ahora',
'il_how_eyebrow':'Cómo ayudamos','il_how_h2':'De la detención a la representación completa',
'il_how_p1':'Desde 2016 el despacho representa a ciudadanos extranjeros en casos penales en Brasil — de la detención en flagrancia y la audiencia de custodia al jurado y los recursos ante los Tribunales Superiores en Brasilia.',
'il_how_p2':'Mantenemos informadas a las familias en el exterior, hacemos de puente con las oficinas consulares y conducimos cada etapa procesal en portugués para que usted no tenga que preocuparse.',
'il_how_box':'En caso de detención, contáctenos por WhatsApp: un abogado explica la situación en su idioma y actúa en la audiencia de custodia — que ocurre dentro de las 24 horas de la detención en Brasil.',
'il_ar_eyebrow':'Frentes de actuación','il_ar_h2':'Qué atendemos',
'il_cards':[('Detenciones y audiencias de custodia','Respuesta inmediata a detenciones de extranjeros en cualquier lugar de Brasil, con defensa en la audiencia de custodia y Habeas Corpus cuando sea necesario.'),('Investigaciones y procesos penales','Defensa completa en investigaciones y procesos, incluidas acusaciones por drogas, delitos financieros y jurado.'),('Delitos económicos y tributarios','Defensa en derecho penal económico: delitos contra el sistema financiero, acusaciones de lavado de dinero y delitos tributarios que involucran empresas y ejecutivos.'),('Puente consular y familiar','Comunicación constante con consulados y con la familia del cliente en el exterior, con actualizaciones del caso en español o inglés.')],
'il_band_h':'¿Detenido o investigado en Brasil?','il_band_p':'Contáctenos por WhatsApp. Un abogado penalista hablará con usted en español y le explicará exactamente los próximos pasos.','il_band_b':'WhatsApp — hablamos español',
'eq_title':'Equipo — João Marcos A. Batista Abogados','eq_desc':'Conozca al equipo: João Marcos A. Batista (OAB/SP 454.179), Leonardo Almeida Santos, Willian Moura Rodrigues y Gabriel Mantovani.',
'eq_eyebrow':'Equipo','eq_h1':'Quiénes conducen <em>su defensa</em>.','eq_sub':'Un equipo dedicado exclusivamente al derecho penal y tributario, liderado por João Marcos A. Batista.',
'eq_role':'Socio director',
'eq_bio1':'Abogado penalista desde 2014. Comenzó su carrera en el Fuero Criminal de Barra Funda y en la Fiscalía de São Paulo, donde conoció desde adentro la rutina de la acusación — experiencia que hoy aplica a la defensa, con énfasis en delitos comunes, delitos económicos y jurado.',
'eq_bio2':'Posgrados en Derecho Penal Económico (FGV/SP) y en Finanzas, Inversiones y Banca (PUC/RS). Consejero de Prerrogativas del Colegio de Abogados de São Paulo, miembro del IDDD, asociado al IBCCRIM y miembro del Instituto Brasileño de Planificación Tributaria.',
'eq_bio3':'El despacho integra la lista de abogados de la Embajada de EE.UU. en Brasil, con actuación en casos penales internacionales desde 2016.',
'eq_adv_eyebrow':'Abogados','eq_adv_h2':'Equipo jurídico',
'eq_o_role':'Abogado Civil y Penal · OAB/SP 545.361','eq_o_bio':'Graduado por FMU/SP, integra el despacho desde 2025, con actuación en materias civil y penal y seguimiento cercano de cada proceso.',
'eq_at_eyebrow':'Atención','eq_at_h2':'Equipo de atención al cliente','eq_at_p':'Profesionales que cuidan el primer contacto, la organización de la atención y la comunicación entre usted y los abogados.','eq_w_role':'Gestión comercial y atención','eq_w_bio':'Responsable de la operación de atención del despacho y del puente entre el cliente y el equipo jurídico, del primer contacto al seguimiento del caso. Graduado en Ingeniería Mecánica por FMU/SP.','eq_g_role':'Atención y relación con clientes','eq_g_bio':'Actúa en la primera atención y en la calificación de los casos, garantizando claridad en la comunicación y organización del flujo hasta los abogados responsables.','eq_band_h':'Hable directamente con el equipo','eq_band_p':'Confidencialidad absoluta, en español, portugués o inglés.','eq_band_b':'WhatsApp',
'nt_title':'Noticias y Prensa — João Marcos A. Batista Abogados','nt_desc':'Reportajes y noticias sobre la actuación del despacho en casos penales y tributarios de repercusión.',
'nt_eyebrow':'En la prensa','nt_h1':'Noticias y <em>reportajes</em>.','nt_sub':'La actuación del despacho en casos de repercusión, registrada por la prensa — además de artículos y análisis de derecho penal y tributario.',
'nw_kind':{'tv':'Entrevista','doc':'Serie','rep':'Reportaje','art':'Artículo'},'nw_watch':'Ver →',
'nt_band_h':'Prensa','nt_band_p':'Para entrevistas, comentarios técnicos y análisis de derecho penal y tributario, contacte al despacho.','nt_band_b':'Contacto de prensa',
})

LANGS = {'pt': P, 'en': E, 'es': S}

# ---------------- IMPRENSA (ordem = relevância; os 3 primeiros vão para a home) ----------------
NEWS = [
 {'veiculo':'Balanço Geral · Rede Record','kind':'tv','thumb':'news-balanco-geral.jpg',
  'url':'https://record.r7.com/balanco-geral/videos/gamer-morta-vivia-em-relacionamento-abusivo-com-assassino-15062022/',
  'pt':('Entrevista ao Balanço Geral sobre o caso da gamer morta em São Paulo','Conversas revelam relação abusiva entre acusado e vítima. João Marcos comenta o caso como advogado de defesa.'),
  'en':('Interview on Balanço Geral (Record TV) about the São Paulo gamer case','Messages reveal an abusive relationship between defendant and victim. João Marcos comments as defense counsel.'),
  'es':('Entrevista en Balanço Geral sobre el caso de la gamer asesinada en São Paulo','Conversaciones revelan una relación abusiva entre acusado y víctima. João Marcos comenta el caso como abogado defensor.')},
 {'veiculo':'Brasil Urgente · Band','kind':'tv','thumb':'news-brasil-urgente.jpg',
  'url':'https://www.youtube.com/watch?v=JL5jx7-o-yA&t=9915s',
  'pt':('Entrevista ao Datena no Brasil Urgente','Mensagens sugerem premeditação. A defesa comenta a investigação ao vivo no programa.'),
  'en':('Interview with Datena on Brasil Urgente (Band TV)','Messages suggest premeditation. Defense counsel discusses the investigation live on air.'),
  'es':('Entrevista con Datena en Brasil Urgente (Band)','Mensajes sugieren premeditación. La defensa comenta la investigación en vivo.')},
 {'veiculo':'Domingo Espetacular · Rede Record','kind':'tv','thumb':'news-domingo-espetacular.jpg',
  'url':'https://record.r7.com/domingo-espetacular/videos/roberto-cabrini-entrevista-jovem-que-matou-estudante-a-facadas-29062022/',
  'pt':('Reportagem especial de Roberto Cabrini no Domingo Espetacular','Cabrini reconstitui o caso e entrevista o acusado ao lado da defesa.'),
  'en':('Roberto Cabrini special report on Domingo Espetacular (Record TV)','Cabrini reconstructs the case and interviews the defendant alongside defense counsel.'),
  'es':('Reportaje especial de Roberto Cabrini en Domingo Espetacular','Cabrini reconstruye el caso y entrevista al acusado junto a la defensa.')},
 {'veiculo':'Investigação Criminal','kind':'doc','thumb':'news-investigacao-criminal.jpg',
  'url':'https://www.youtube.com/watch?v=Ex2CVMGXGx4',
  'pt':('Participação na série Investigação Criminal — episódio “Gamer Assassinada”','Série documental sobre crimes reais. O escritório participa como defesa no caso.'),
  'en':('Appearance in the series Investigação Criminal — “Gamer Assassinada” episode','True-crime documentary series. The firm appears as defense counsel in the case.'),
  'es':('Participación en la serie Investigação Criminal — episodio “Gamer Assassinada”','Serie documental sobre crímenes reales. El despacho participa como defensa en el caso.')},
 {'veiculo':'Fantástico · Rede Globo','kind':'rep','thumb':'news-fantastico.jpg',
  'url':'https://g1.globo.com/fantastico/noticia/2022/08/28/golpe-das-passagens-aereas-fantastico-mostra-historias-de-pessoas-que-revelam-ter-sofrido-calotes.ghtml',
  'pt':('Fantástico: golpe das passagens aéreas da agência TC Viagens','Reportagem com histórias das vítimas. João Marcos atua como advogado das pessoas lesadas.'),
  'en':('Fantástico (Globo TV): the TC Viagens airline-ticket scam','Report featuring victims\' stories. João Marcos represents the defrauded customers.'),
  'es':('Fantástico (Globo): la estafa de pasajes aéreos de la agencia TC Viagens','Reportaje con historias de las víctimas. João Marcos actúa como abogado de los afectados.')},
 {'veiculo':'G1 · São Paulo','kind':'rep','thumb':'news-g1.jpg',
  'url':'https://g1.globo.com/sp/sao-paulo/noticia/2021/02/23/estudante-e-suspeito-de-matar-jovem-jogadora-de-game-que-conheceu-pela-internet-ela-foi-morta-a-facadas-em-sp.ghtml',
  'pt':('G1: estudante é suspeito de matar jovem gamer que conheceu pela internet','Cobertura do G1 e da TV Globo sobre o caso, da investigação ao julgamento. O escritório atuou na defesa.'),
  'en':('G1: student suspected of killing young gamer he met online','G1 / Globo TV coverage of the case, from investigation to trial. The firm acted for the defense.'),
  'es':('G1: estudiante sospechoso de matar a joven gamer que conoció por internet','Cobertura de G1 y TV Globo sobre el caso, de la investigación al juicio. El despacho actuó en la defensa.')},
 {'veiculo':'Conjur','kind':'art','thumb':None,
  'url':'https://conjur.com.br/2024-abr-20/lavagem-ou-autolavagem-eis-a-questao/',
  'pt':('“Lavagem ou autolavagem: eis a questão” — artigo em coautoria de João Marcos A. Batista','Análise sobre a tipificação da autolavagem no direito penal econômico.'),
  'en':('“Money laundering or self-laundering: that is the question” — article co-authored by João Marcos A. Batista','Analysis of how self-laundering is treated under Brazilian economic criminal law.'),
  'es':('“Lavado o autolavado: esa es la cuestión” — artículo en coautoría de João Marcos A. Batista','Análisis sobre la tipificación del autolavado en el derecho penal económico.')},
 {'veiculo':'Manchete RJ','kind':'rep','thumb':None,
  'url':'https://mancheterj.com/escritorio-deixa-defesa-de-influencer-campista-alvo-de-operacao-contra-jogo-do-tigrinho/',
  'pt':('Atuação em caso envolvendo influenciador alvo de operação contra o “jogo do tigrinho”','Matéria sobre a participação do escritório na defesa em investigação de grande repercussão.'),
  'en':('Case involving an influencer targeted by the “Tigrinho” gambling operation','Report on the firm\'s role in the defense during a high-profile investigation.'),
  'es':('Actuación en caso de influencer investigado en la operación contra el “juego del tigrinho”','Nota sobre la participación del despacho en la defensa en una investigación de gran repercusión.')},
]


def news_card(t, lg, n):
    title, summ = n[lg]
    if n['thumb']:
        thumb = '<a class="thumb" href="' + n['url'] + '" target="_blank" rel="noopener"><img src="../assets/' + n['thumb'] + '" alt="' + n['veiculo'] + '" loading="lazy"></a>'
    else:
        thumb = '<a class="thumb thumb-alt" href="' + n['url'] + '" target="_blank" rel="noopener"><span>' + n['veiculo'].split(' · ')[0] + '</span></a>'
    return ('<article class="news">' + thumb + '<div class="news-body"><div class="veiculo">' + n['veiculo'] + ' <span class="kind">' + t['nw_kind'][n['kind']] + '</span></div>'
            '<h3><a href="' + n['url'] + '" target="_blank" rel="noopener">' + title + '</a></h3><p>' + summ + '</p>'
            '<a class="more" href="' + n['url'] + '" target="_blank" rel="noopener">' + (t['nw_watch'] if n['kind'] in ('tv','doc') else t['nw_read']) + '</a></div></article>')
LANG_NAMES = {'pt':'PT','en':'EN','es':'ES'}


def head(t, title, desc, fname, schema=False):
    alts = ''.join('<link rel="alternate" hreflang="%s" href="%s/%s/%s">' % (lg, BASE, lg, fname) for lg in LANGS)
    alts += '<link rel="alternate" hreflang="x-default" href="%s/en/%s">' % (BASE, fname)
    sch = ''
    if schema:
        sch = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"LegalService","name":"João Marcos A. Batista — Advocacia e Consultoria","url":"' + BASE + '","telephone":"+5511986213553","email":"joao@jmbadv.com.br","address":{"@type":"PostalAddress","streetAddress":"Rua Enxovia, 472, conj. 1504 e 1505 — Neo Corporate Offices, Brooklin","addressLocality":"São Paulo","addressRegion":"SP","postalCode":"04711-030","addressCountry":"BR"},"openingHours":"Mo-Su 00:00-24:00","founder":{"@type":"Person","name":"João Marcos A. Batista","jobTitle":"Advogado — OAB/SP 454.179"},"areaServed":"BR","knowsLanguage":["pt-BR","en","es"]}</script>')
    return ('<!DOCTYPE html>\n<html lang="' + t['html_lang'] + '">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + title + '</title>\n<meta name="description" content="' + desc + '">\n' + alts + '\n'
            '<link rel="icon" type="image/png" href="../assets/monograma.png">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n'
            '<link rel="stylesheet" href="../assets/style.css">\n' + sch + '</head>\n<body>\n' + WA_SYMBOL + '\n')


def header(t, active, fname):
    links = ''.join('<li><a href="%s"%s>%s</a></li>' % (h, ' class="active"' if h == active else '', lb) for h, lb in t['nav'])
    sw = ''.join('<a href="../%s/%s"%s data-setlang="%s">%s</a>' % (lg, fname, ' class="active"' if lg == t['lang'] else '', lg, LANG_NAMES[lg]) for lg in LANGS)
    return ('<header><div class="container nav">'
            '<a href="index.html" class="logo"><img src="../assets/monograma.png" alt="JMB"><div class="logo-text"><strong>JOÃO MARCOS A. BATISTA</strong><span>' + t['logo_tag'] + '</span></div></a>'
            '<ul class="nav-links" id="navLinks">' + links + '</ul>'
            '<div style="display:flex;align-items:center;gap:12px">'
            '<div class="lang-sw">' + sw + '</div>'
            '<a class="nav-cta" href="' + WA + '?text=' + t['wa_default'] + '" target="_blank" rel="noopener">' + WA_ICON + '<span>' + t['wa_btn'] + '</span></a>'
            '<button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>'
            '</div></div></header>\n')


def footer(t):
    links = ''.join('<li><a href="%s">%s</a></li>' % (h, lb) for h, lb in t['ft_links'])
    return ('<footer><div class="container"><div class="ft-grid">'
            '<div class="ft-brand"><img src="../assets/monograma.png" alt="JMB">'
            '<p><strong style="color:#fff">João Marcos A. Batista</strong><br>' + t['logo_tag'] + '<br>OAB/SP 454.179 · CNPJ 44.546.186/0001-54</p></div>'
            '<div class="ft"><h5>' + t['ft_nav'] + '</h5><ul>' + links + '</ul></div>'
            '<div class="ft"><h5>' + t['ft_contact'] + '</h5><ul>'
            '<li><a href="' + WA + '" target="_blank" rel="noopener">(11) 98621-3553</a></li>'
            '<li><a href="mailto:joao@jmbadv.com.br">joao@jmbadv.com.br</a></li>'
            '<li><a href="https://maps.google.com/?q=Rua+Enxovia+472+Brooklin+S%C3%A3o+Paulo" target="_blank" rel="noopener">Rua Enxovia, 472 — Brooklin, SP</a></li>'
            '<li><a href="https://www.instagram.com/adv.joaomarcosbatista" target="_blank" rel="noopener">Instagram</a></li></ul></div>'
            '</div><div class="ft-bottom">© 2026 João Marcos A. Batista. ' + t['ft_rights'] + '<br>' + t['ft_legal'] + '</div></div></footer>\n')


def floats(t):
    return ('<a class="wa-float" href="' + WA + '?text=' + t['wa_default'] + '" target="_blank" rel="noopener" aria-label="WhatsApp">' + WA_ICON + '</a>'
            '<a class="wa-bar" href="' + WA + '?text=' + t['wa_default'] + '" target="_blank" rel="noopener">' + WA_ICON + ' ' + t['wa_bar'] + '</a>\n')


def cta_band(h2, p, btn, wa_msg):
    return ('<section class="section cta-band"><div class="container"><h2>' + h2 + '</h2><p>' + p + '</p>'
            '<a class="btn btn-gold" href="' + WA + '?text=' + wa_msg + '" target="_blank" rel="noopener">' + btn + '</a></div></section>\n')


def faq_block(t, items):
    rows = ''.join('<div class="faq-item"><button class="faq-q">%s</button><div class="faq-a"><p>%s</p></div></div>' % qa for qa in items)
    return ('<section class="section"><div class="container"><div class="section-head"><div class="eyebrow">' + t['fq_eyebrow'] + '</div><h2>' + t['fq_h2'] + '</h2></div><div class="faq-list">' + rows + '</div></div></section>\n')


def urg_split(t, h2=None, p1=None, p2=None):
    steps = ''.join('<li>%s</li>' % s for s in t['urg_steps'])
    body = '<p style="margin-top:24px">' + (p1 or t['urg_p1']) + '</p>'
    if p2 is not False:
        body += '<p>' + (p2 or t['urg_p2']) + '</p>'
    return ('<section class="section"><div class="container split-grid"><div>'
            '<div class="eyebrow">' + t['urg_eyebrow'] + '</div><h2>' + (h2 or t['urg_h2']) + '</h2>' + body +
            '<a class="btn btn-gold" style="margin-top:12px" href="' + WA + '?text=' + t['wa_urgente'] + '" target="_blank" rel="noopener">' + t['urg_cta'] + '</a></div>'
            '<div class="card-passos"><h3>' + t['urg_card'] + '</h3><ol>' + steps + '</ol></div></div></section>\n')


def timeline(t):
    items = ''.join('<div class="tl-item"><div class="tl-num">0%d</div><h4>%s</h4><p>%s</p></div>' % (i + 1, h, p) for i, (h, p) in enumerate(t['tl']))
    return ('<section class="section timeline"><div class="container"><div class="eyebrow">' + t['tl_eyebrow'] + '</div><h2>' + t['tl_h2'] + '</h2><div class="tl-grid">' + items + '</div></div></section>\n')


ICONS = {'crim': '<svg viewBox="0 0 24 24"><path d="M12 3v18M5 7l7-4 7 4M5 7v3c0 2 1.5 3.5 3.5 3.5S12 12 12 10M19 7v3c0 2-1.5 3.5-3.5 3.5S12 12 12 10M7 21h10"/></svg>',
         'trib': '<svg viewBox="0 0 24 24"><path d="M4 20h16M6 20V10M12 20V4M18 20v-8"/></svg>',
         'intl': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9z"/></svg>'}


def body_index(t):
    creds = ''.join('<div class="cred"><b>%s</b>%s</div>' % c for c in t['creds'])
    faqs = faq_block(t, t['faq_home'])
    news = ''.join(news_card(t, t['_lg'], n) for n in NEWS[:3])
    opts = ''.join('<option>%s</option>' % o for o in t['ct_f_opts'])
    return ('''
<section class="hero" id="inicio"><div class="container hero-grid"><div>
<div class="eyebrow">''' + t['hero_eyebrow'] + '''</div>
<h1>''' + t['hero_h1'] + '''</h1>
<p class="hero-sub">''' + t['hero_sub'] + '''</p>
<div class="badge-plantao"><span class="pulse"></span> ''' + t['hero_badge'] + '''</div>
<div class="hero-ctas"><a class="btn btn-gold" href="''' + WA + '?text=' + t['wa_urgente'] + '''" target="_blank" rel="noopener">''' + t['hero_cta1'] + '''</a><a class="btn btn-outline" href="#areas">''' + t['hero_cta2'] + '''</a></div>
</div><div class="hero-photo"><img src="../assets/hero-joao.jpg" alt="João Marcos A. Batista"></div></div></section>
<div class="creds"><div class="container creds-grid">''' + creds + '''</div></div>
''' + urg_split(t) + '''
<section class="section areas" id="areas"><div class="container">
<div class="section-head"><div class="eyebrow">''' + t['ar_eyebrow'] + '''</div><h2>''' + t['ar_h2'] + '''</h2><p>''' + t['ar_p'] + '''</p></div>
<div class="macro-grid">
<div class="macro"><div class="macro-icon">''' + ICONS['crim'] + '''</div><h3>''' + t['ar_crim_h'] + '''</h3><p>''' + t['ar_crim_p'] + '''</p><a href="criminal.html">''' + t['ar_crim_a'] + '''</a></div>
<div class="macro"><div class="macro-icon">''' + ICONS['trib'] + '''</div><h3>''' + t['ar_trib_h'] + '''</h3><p>''' + t['ar_trib_p'] + '''</p><a href="tributario.html">''' + t['ar_trib_a'] + '''</a></div>
<div class="macro"><div class="macro-icon">''' + ICONS['intl'] + '''</div><h3>''' + t['ar_intl_h'] + '''</h3><p>''' + t['ar_intl_p'] + '''</p><a href="internacional.html">''' + t['ar_intl_a'] + '''</a></div>
</div></div></section>
<section class="section ponte"><div class="container split-grid"><div>
<div class="eyebrow">''' + t['po_eyebrow'] + '''</div><h2>''' + t['po_h2'] + '''</h2>
<p style="margin-top:24px">''' + t['po_p1'] + '''</p><p>''' + t['po_p2'] + '''</p>
<a class="btn btn-gold" style="margin-top:12px" href="''' + WA + '?text=' + t['wa_empresa'] + '''" target="_blank" rel="noopener">''' + t['po_cta'] + '''</a>
</div><div class="ponte-photo"><img src="../assets/joao-atuacao.jpg" alt="João Marcos A. Batista"></div></div></section>
''' + timeline(t) + '''
<section class="section"><div class="container split-grid"><div>
<div class="eyebrow">''' + t['in_eyebrow'] + '''</div><h2>''' + t['in_h2'] + '''</h2>
<p style="margin-top:24px">''' + t['in_p'] + '''</p>
<div class="intl-en">''' + t['in_en'] + '''</div>
<a class="btn btn-outline-dark" href="internacional.html">''' + t['in_a'] + '''</a>
</div><div class="foto-frame"><img src="../assets/joao-cidade.jpg" alt="International practice"></div></div></section>
<section class="section areas"><div class="container">
<div class="section-head"><div class="eyebrow">''' + t['nw_eyebrow'] + '''</div><h2>''' + t['nw_h2'] + '''</h2><p>''' + t['nw_p'] + '''</p></div>
<div class="news-grid">''' + news + '''</div>
<div class="rev-link"><a href="noticias.html" style="color:var(--dourado)">''' + t['nw_all'] + '''</a></div>
</div></section>
<section class="section reviews"><div class="container">
<div class="section-head"><div class="eyebrow">''' + t['rv_eyebrow'] + '''</div><h2>''' + t['rv_h2'] + '''</h2>
<div class="rating"><span class="stars">★★★★★</span> ''' + t['rv_rating'] + '''</div></div>
<div class="rev-grid">
<div class="rev"><div class="rev-stars">★★★★★</div><p>''' + t['rv1'] + '''</p><b>''' + t['rv1n'] + '''</b></div>
<div class="rev"><div class="rev-stars">★★★★★</div><p>''' + t['rv2'] + '''</p><b>''' + t['rv2n'] + '''</b><span>''' + t['rv2t'] + '''</span></div>
<div class="rev"><div class="rev-stars">★★★★★</div><p>''' + t['rv3'] + '''</p><b>''' + t['rv3n'] + '''</b><span>''' + t['rv3t'] + '''</span></div>
</div>
<div class="rev-link"><a href="https://www.google.com/search?q=jo%C3%A3o+marcos+a+batista+advocacia" target="_blank" rel="noopener">''' + t['rv_link'] + '''</a></div>
</div></section>
''' + faqs + '''
<section class="section contato" id="contato"><div class="container">
<div class="eyebrow">''' + t['ct_eyebrow'] + '''</div><h2>''' + t['ct_h2'] + '''</h2>
<div class="ct-grid"><div class="ct-info">
<a class="ct-wa" href="''' + WA + '?text=' + t['wa_default'] + '''" target="_blank" rel="noopener">''' + WA_ICON + ' ' + t['wa_btn'] + ''' — (11) 98621-3553</a>
<div class="ct-block"><h3>''' + t['ct_email'] + '''</h3><a href="mailto:joao@jmbadv.com.br">joao@jmbadv.com.br</a></div>
<div class="ct-block"><h3>''' + t['ct_addr'] + '''</h3>Neo Corporate Offices<br>Rua Enxovia, 472 — conj. 1504 e 1505<br>Brooklin, São Paulo/SP · CEP 04711-030<br><a href="https://maps.google.com/?q=Rua+Enxovia+472+Brooklin+S%C3%A3o+Paulo" target="_blank" rel="noopener" style="color:var(--dourado)">''' + t['ct_map'] + '''</a></div>
<div class="ct-block"><h3>''' + t['ct_redes'] + '''</h3><a href="https://www.instagram.com/adv.joaomarcosbatista" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.linkedin.com/" target="_blank" rel="noopener">LinkedIn</a> · <a href="https://www.facebook.com/joaomarcos951" target="_blank" rel="noopener">Facebook</a></div>
</div><div>
<form id="ctForm" onsubmit="return enviarForm(event)">
<div class="f-row"><input type="text" name="nome" placeholder="''' + t['ct_f_nome'] + '''" required><input type="tel" name="whatsapp" placeholder="''' + t['ct_f_wa'] + '''" required></div>
<select name="assunto" required><option value="" disabled selected>''' + t['ct_f_ass'] + '''</option>''' + opts + '''</select>
<textarea name="mensagem" placeholder="''' + t['ct_f_msg'] + '''"></textarea>
<label class="lgpd"><input type="checkbox" required> ''' + t['ct_f_lgpd'] + '''</label>
<button type="submit" class="btn btn-gold">''' + t['ct_f_btn'] + '''</button>
<p class="micro">''' + t['ct_f_micro'] + '''</p>
</form></div></div></div></section>
''')


def body_criminal(t):
    cards = ''.join('<div class="sub"><h4>%s</h4><p>%s</p></div>' % c for c in t['cr_cards'])
    return ('<section class="page-hero"><div class="container"><div class="eyebrow">' + t['cr_eyebrow'] + '</div><h1>' + t['cr_h1'] + '</h1><p class="hero-sub">' + t['cr_sub'] + '</p><div class="hero-ctas"><a class="btn btn-gold" href="' + WA + '?text=' + t['wa_urgente'] + '" target="_blank" rel="noopener">' + t['cr_cta'] + '</a></div></div></section>\n'
            + urg_split(t, h2=t['cr_urg_h2'], p1=t['cr_urg_p'], p2=False)
            + '<section class="section areas"><div class="container"><div class="section-head"><div class="eyebrow">' + t['cr_sub_eyebrow'] + '</div><h2>' + t['cr_sub_h2'] + '</h2></div><div class="sub-grid">' + cards + '</div></div></section>\n'
            + timeline(t) + faq_block(t, t['cr_faq'])
            + cta_band(t['cr_band_h'], t['cr_band_p'], t['cr_band_b'], t['cr_band_wa']))


def body_tributario(t):
    cards = ''.join('<div class="sub"><h4>%s</h4><p>%s</p></div>' % c for c in t['tb_cards'])
    return ('<section class="page-hero"><div class="container"><div class="eyebrow">' + t['tb_eyebrow'] + '</div><h1>' + t['tb_h1'] + '</h1><p class="hero-sub">' + t['tb_sub'] + '</p><div class="hero-ctas"><a class="btn btn-gold" href="' + WA + '?text=' + t['wa_trib'] + '" target="_blank" rel="noopener">' + t['tb_cta'] + '</a></div></div></section>\n'
            '<section class="section"><div class="container split-grid"><div><div class="eyebrow">' + t['tb_why_eyebrow'] + '</div><h2>' + t['tb_why_h2'] + '</h2><p style="margin-top:24px">' + t['tb_why_p1'] + '</p><p>' + t['tb_why_p2'] + '</p></div><div class="foto-frame"><img src="../assets/joao-blinds.jpg" alt="João Marcos A. Batista"></div></div></section>\n'
            '<section class="section areas"><div class="container"><div class="section-head"><div class="eyebrow">' + t['tb_sv_eyebrow'] + '</div><h2>' + t['tb_sv_h2'] + '</h2></div><div class="sub-grid cols2">' + cards + '</div></div></section>\n'
            '<section class="section ponte"><div class="container"><div class="eyebrow">' + t['po_eyebrow'] + '</div><h2>' + t['tb_po_h2'] + '</h2><p style="margin-top:24px;max-width:760px">' + t['tb_po_p1'] + '</p><p style="max-width:760px">' + t['tb_po_p2'] + '</p><a class="btn btn-gold" style="margin-top:22px" href="' + WA + '?text=' + t['wa_empresa'] + '" target="_blank" rel="noopener">' + t['po_cta'] + '</a></div></section>\n'
            + faq_block(t, t['tb_faq'])
            + cta_band(t['tb_band_h'], t['tb_band_p'], t['tb_band_b'], t['wa_trib']))


def body_internacional(t):
    cards = ''.join('<div class="sub"><h4>%s</h4><p>%s</p></div>' % c for c in t['il_cards'])
    return ('<section class="page-hero"><div class="container"><div class="eyebrow">' + t['il_eyebrow'] + '</div><h1>' + t['il_h1'] + '</h1><p class="hero-sub">' + t['il_sub'] + '</p><div class="hero-ctas"><a class="btn btn-gold" href="' + WA + '?text=' + t['wa_intl'] + '" target="_blank" rel="noopener">' + t['il_cta'] + '</a></div></div></section>\n'
            '<section class="section"><div class="container split-grid"><div><div class="eyebrow">' + t['il_how_eyebrow'] + '</div><h2>' + t['il_how_h2'] + '</h2><p style="margin-top:24px">' + t['il_how_p1'] + '</p><p>' + t['il_how_p2'] + '</p><div class="intl-en">' + t['il_how_box'] + '</div></div><div class="foto-frame"><img src="../assets/joao-cidade.jpg" alt="International criminal defense in Brazil"></div></div></section>\n'
            '<section class="section areas"><div class="container"><div class="section-head"><div class="eyebrow">' + t['il_ar_eyebrow'] + '</div><h2>' + t['il_ar_h2'] + '</h2></div><div class="sub-grid cols2">' + cards + '</div></div></section>\n'
            + cta_band(t['il_band_h'], t['il_band_p'], t['il_band_b'], t['wa_intl']))


def adv_card(name, role, bio, photo):
    if photo:
        ph = '<div class="adv-photo"><img src="../assets/' + photo + '" alt="' + name + '" loading="lazy"></div>'
    else:
        ph = '<div class="adv-photo adv-photo-alt"><span>' + ''.join(p[0] for p in name.split()[:2]) + '</span></div>'
    return '<div class="adv-card">' + ph + '<div class="adv-body"><h3>' + name + '</h3><div class="oab">' + role + '</div><p>' + bio + '</p></div></div>'


def body_equipe(t):
    return ('<section class="page-hero"><div class="container"><div class="eyebrow">' + t['eq_eyebrow'] + '</div><h1>' + t['eq_h1'] + '</h1><p class="hero-sub">' + t['eq_sub'] + '</p></div></section>\n'
            '<section class="section"><div class="container split-grid"><div class="foto-frame left"><img src="../assets/joao-sobre.jpg" alt="João Marcos A. Batista"></div><div>'
            '<div class="eyebrow">' + t['eq_role'] + '</div><h2>João Marcos A. Batista</h2>'
            '<p style="margin-top:6px;color:var(--dourado);font-weight:600;letter-spacing:.08em;font-size:13px">OAB/SP 454.179</p>'
            '<p style="margin-top:18px">' + t['eq_bio1'] + '</p><p>' + t['eq_bio2'] + '</p><p>' + t['eq_bio3'] + '</p></div></div></section>\n'
            '<section class="section areas"><div class="container"><div class="section-head"><div class="eyebrow">' + t['eq_adv_eyebrow'] + '</div><h2>' + t['eq_adv_h2'] + '</h2></div>'
            '<div class="adv-grid single">'
            + adv_card('Leonardo Almeida Santos', t['eq_o_role'], t['eq_o_bio'], 'equipe-leonardo.jpg')
            + '</div></div></section>\n'
            '<section class="section"><div class="container"><div class="section-head"><div class="eyebrow">' + t['eq_at_eyebrow'] + '</div><h2>' + t['eq_at_h2'] + '</h2><p>' + t['eq_at_p'] + '</p></div>'
            '<div class="adv-grid">'
            + adv_card('Willian Moura Rodrigues', t['eq_w_role'], t['eq_w_bio'], 'equipe-willian.jpg')
            + adv_card('Gabriel Mantovani', t['eq_g_role'], t['eq_g_bio'], 'equipe-gabriel.jpg')
            + '</div></div></section>\n'
            + cta_band(t['eq_band_h'], t['eq_band_p'], t['eq_band_b'], t['wa_equipe']))


def body_noticias(t):
    cards = ''.join(news_card(t, t['_lg'], n) for n in NEWS)
    return ('<section class="page-hero"><div class="container"><div class="eyebrow">' + t['nt_eyebrow'] + '</div><h1>' + t['nt_h1'] + '</h1><p class="hero-sub">' + t['nt_sub'] + '</p></div></section>\n'
            '<section class="section areas"><div class="container"><div class="news-grid">' + cards + '</div></div></section>\n'
            + cta_band(t['nt_band_h'], t['nt_band_p'], t['nt_band_b'], t['wa_imprensa']))


PAGES = [
    ('index.html', 'ix_title', 'ix_desc', body_index, True, True),
    ('criminal.html', 'cr_title', 'cr_desc', body_criminal, False, False),
    ('tributario.html', 'tb_title', 'tb_desc', body_tributario, False, False),
    ('internacional.html', 'il_title', 'il_desc', body_internacional, False, False),
    ('equipe.html', 'eq_title', 'eq_desc', body_equipe, False, False),
    ('noticias.html', 'nt_title', 'nt_desc', body_noticias, False, False),
]

DETECTOR = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>João Marcos A. Batista — Advocacia e Consultoria</title>
<meta name="robots" content="noindex">
<link rel="icon" type="image/png" href="assets/monograma.png">
<style>body{margin:0;background:#2E2F34;color:#DFA86B;font-family:Montserrat,Helvetica,sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center;text-align:center}a{color:#DFA86B;border:1px solid rgba(223,168,107,.5);padding:12px 26px;border-radius:2px;text-decoration:none;margin:6px;display:inline-block;letter-spacing:.1em;font-size:13px}img{height:64px;margin-bottom:24px}</style>
<script>
(function(){
  var s=null;try{s=localStorage.getItem('jmb-lang')}catch(e){}
  var l=(s||navigator.language||navigator.userLanguage||'en').toLowerCase();
  var d=l.indexOf('pt')===0?'pt':l.indexOf('es')===0?'es':'en';
  location.replace(d+'/index.html');
})();
</script>
<noscript><meta http-equiv="refresh" content="0;url=pt/index.html"></noscript>
</head>
<body><div><img src="assets/monograma.png" alt="JMB"><br>
<a href="pt/index.html">PORTUGUÊS</a><a href="en/index.html">ENGLISH</a><a href="es/index.html">ESPAÑOL</a>
</div></body>
</html>
'''

# build
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copytree('/home/claude/site-jmb/assets', OUT + '/assets')
if os.path.exists(OUT + '/assets/style.css'):
    pass
open(OUT + '/index.html', 'w').write(DETECTOR)
shutil.copy('/home/claude/site-jmb/bio.html', OUT + '/bio.html')

# redirect stubs na raiz (Vercel cleanUrls: /criminal -> criminal.html -> /{lang}/criminal.html)
STUB_PAGES = {
 'criminal.html':('Advocacia Criminal — João Marcos A. Batista',[('pt','Criminal'),('en','Criminal Defense'),('es','Defensa Penal')]),
 'tributario.html':('Advocacia Tributária — João Marcos A. Batista',[('pt','Tributário'),('en','Tax Law'),('es','Tributario')]),
 'internacional.html':('Atuação Internacional — João Marcos A. Batista',[('pt','Internacional'),('en','International'),('es','Internacional')]),
 'equipe.html':('Equipe — João Marcos A. Batista',[('pt','Equipe'),('en','Team'),('es','Equipo')]),
 'noticias.html':('Notícias — João Marcos A. Batista',[('pt','Notícias'),('en','News'),('es','Noticias')]),
}
for fname, (title, links) in STUB_PAGES.items():
    html = DETECTOR.replace('João Marcos A. Batista — Advocacia e Consultoria', title).replace("location.replace(d+'/index.html')", "location.replace(d+'/" + fname + "')").replace('url=pt/index.html', 'url=pt/' + fname)
    html = html.replace('<a href="pt/index.html">PORTUGUÊS</a><a href="en/index.html">ENGLISH</a><a href="es/index.html">ESPAÑOL</a>',
                        ''.join('<a href="%s/%s">%s</a>' % (lg, fname, lb) for lg, lb in links))
    open(OUT + '/' + fname, 'w').write(html)
open(OUT + '/vercel.json', 'w').write('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n')
for lg, t in LANGS.items():
    t['_lg'] = lg
    os.makedirs(OUT + '/' + lg, exist_ok=True)
    for fname, tk, dk, fn, schema, form in PAGES:
        html = head(t, t[tk], t[dk], fname, schema) + header(t, fname if fname != 'index.html#contato' else 'index.html', fname) + fn(t) + footer(t) + floats(t) + SCRIPT_BASE
        if form:
            html += SCRIPT_FORM
        html += '\n</body>\n</html>\n'
        open(OUT + '/' + lg + '/' + fname, 'w').write(html)
        print(lg + '/' + fname, len(html) // 1024, 'KB')
print('done')
