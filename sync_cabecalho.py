#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================
 SINCRONIZADOR DE CABEÇALHO E RODAPÉ — Acorn Advisory
=============================================================
Quando você mudar o menu (adicionar/remover item, trocar link),
edite as configurações abaixo e rode:

    python sync_cabecalho.py

Ele atualiza o cabeçalho e o rodapé de TODAS as páginas de uma vez,
mantendo os caminhos relativos corretos de cada uma.

NÃO edite o cabeçalho/rodapé direto nas páginas — suas mudanças
seriam sobrescritas na próxima sincronização. Edite AQUI.
=============================================================
"""
import os, re

# ---------- CONFIGURAÇÃO DO MENU (edite aqui) ----------
MENU = {
    "pt": {"home":"Home", "quem-somos":"Quem Somos", "servicos":"Serviços e Especialidades",
           "cases":"Cases", "carreira":"Carreira", "na-midia":"Na Mídia", "contato":"Contato"},
    "en": {"home":"Home", "quem-somos":"About Us", "servicos":"Services and Specialties",
           "cases":"Cases", "carreira":"Careers", "na-midia":"News", "contato":"Contact"},
}
LINKS = {
    "pt": {"home":"", "quem-somos":"quem-somos/", "servicos":"servicos-e-especialidades/",
           "cases":"cases/", "carreira":"carreira/", "na-midia":"na-midia/", "contato":"contato/"},
    "en": {"home":"en/", "quem-somos":"en/about-us/", "servicos":"en/services-and-specialties/",
           "cases":"en/cases/", "carreira":"en/careers/", "na-midia":"en/news/", "contato":"en/contact/"},
}
ENDERECO = """Av. Juscelino Kubitschek, 1700, 7° andar<br>
            Itaim Bibi, São Paulo – SP<br>
            CEP: 04543.000"""
EMAIL = "contato@acornad.com.br"
SOCIAIS = {
    "linkedin":"https://br.linkedin.com/company/acornadvisory",
    "instagram":"https://www.instagram.com/acornadvisory/",
    "youtube":"https://www.youtube.com/@AcornAdvisory",
}

# ---------- MAPA DE PÁGINAS (pasta -> prefixo, idioma, item ativo) ----------
PAGINAS = [
    ("",                            "",       "pt", "home"),
    ("quem-somos",                  "../",    "pt", "quem-somos"),
    ("servicos-e-especialidades",   "../",    "pt", "servicos"),
    ("cases",                       "../",    "pt", "cases"),
    ("carreira",                    "../",    "pt", "carreira"),
    ("na-midia",                    "../",    "pt", "na-midia"),
    ("contato",                     "../",    "pt", "contato"),
    ("politica-de-privacidade",     "../",    "pt", ""),
    ("en",                          "../",    "en", "home"),
    ("en/about-us",                 "../../", "en", "quem-somos"),
    ("en/services-and-specialties", "../../", "en", "servicos"),
    ("en/cases",                    "../../", "en", "cases"),
    ("en/careers",                  "../../", "en", "carreira"),
    ("en/news",                     "../../", "en", "na-midia"),
    ("en/contact",                  "../../", "en", "contato"),
    ("en/privacy-policy",           "../../", "en", ""),
]

def cabecalho(prefixo, lang, ativo):
    m, L = MENU[lang], LINKS[lang]
    cta = "Contato" if lang=="pt" else "Contact"
    def cls(k): return ' class="active"' if k==ativo else ''
    itens = "\n".join(
        f'        <li><a href="{prefixo}{L[k]}"{cls(k)}>{m[k]}</a></li>'
        for k in ["home","quem-somos","servicos","cases","carreira","na-midia"])
    pt_active = ' class="active"' if lang=="pt" else ''
    en_active = ' class="active"' if lang=="en" else ''
    return f'''  <!-- ===== CABEÇALHO (gerado por sync_cabecalho.py — não edite aqui) ===== -->
  <header class="site-header">
    <nav class="nav">
      <a class="nav-logo" href="{prefixo}{L['home']}"><img src="{prefixo}assets/img/Acorn-Logo.png" alt="Acorn Advisory"></a>
      <ul class="nav-menu" id="navMenu">
{itens}
      </ul>
      <div class="nav-right">
        <a class="nav-cta" href="{prefixo}{L['contato']}">{cta}</a>
        <span class="nav-langs">
          <a{pt_active} href="{prefixo}" title="Português"><img src="https://flagcdn.com/br.svg" alt="PT"></a>
          <a{en_active} href="{prefixo}en/" title="English"><img src="https://flagcdn.com/gb.svg" alt="EN"></a>
        </span>
        <button class="nav-toggle" id="navToggle" aria-label="Menu"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </header>
  <!-- ===== FIM CABEÇALHO ===== -->'''

def rodape(prefixo, lang):
    m, L = MENU[lang], LINKS[lang]
    if lang=="pt":
        h1,h2,h3 = "Links Rápidos","Serviços e especialidades","Contato"
        serv = ["M&A","Captação de Recursos","Assessoria Estratégica","Transaction Services"]
        dir_ = "© 2026 Acorn Advisory. Todos os direitos reservados."
    else:
        h1,h2,h3 = "Quick Links","Services and specialties","Contact"
        serv = ["M&A","Fundraising","Strategic Advisory","Transaction Services"]
        dir_ = "© 2026 Acorn Advisory. All rights reserved."
    links_menu = "\n".join(f'            <li><a href="{prefixo}{L[k]}">{m[k]}</a></li>'
                           for k in ["quem-somos","servicos","cases","carreira","na-midia","contato"])
    serv_menu = "\n".join(f'            <li><a href="{prefixo}{L["servicos"]}">{s}</a></li>' for s in serv)
    return f'''  <!-- ===== RODAPÉ (gerado por sync_cabecalho.py — não edite aqui) ===== -->
  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-col footer-logo">
          <img src="{prefixo}assets/img/Logo-Footer.png" alt="Acorn Advisory">
          <div class="footer-social">
            <a href="{SOCIAIS['linkedin']}" target="_blank" rel="noopener">in</a>
            <a href="{SOCIAIS['instagram']}" target="_blank" rel="noopener">ig</a>
            <a href="{SOCIAIS['youtube']}" target="_blank" rel="noopener">yt</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>{h1}</h4>
          <ul>
{links_menu}
          </ul>
        </div>
        <div class="footer-col">
          <h4>{h2}</h4>
          <ul>
{serv_menu}
          </ul>
        </div>
        <div class="footer-col">
          <h4>{h3}</h4>
          <p class="footer-addr">
            {ENDERECO}<br><br>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </p>
        </div>
      </div>
      <div class="footer-bottom">{dir_}</div>
    </div>
  </footer>
  <!-- ===== FIM RODAPÉ ===== -->'''

def sync():
    base = os.path.dirname(os.path.abspath(__file__))
    n = 0
    for pasta, prefixo, lang, ativo in PAGINAS:
        caminho = os.path.join(base, pasta, "index.html")
        if not os.path.exists(caminho):
            print(f"  (pulado, não existe) {pasta}/index.html"); continue
        html = open(caminho, encoding="utf-8").read()
        novo_cab = cabecalho(prefixo, lang, ativo)
        novo_rod = rodape(prefixo, lang)
        # Substitui bloco de cabeçalho
        html = re.sub(r'  <!-- ===== CABEÇALHO.*?<!-- ===== FIM CABEÇALHO ===== -->',
                      novo_cab, html, flags=re.S)
        # Substitui bloco de rodapé
        html = re.sub(r'  <!-- ===== RODAPÉ.*?<!-- ===== FIM RODAPÉ ===== -->',
                      novo_rod, html, flags=re.S)
        open(caminho, "w", encoding="utf-8").write(html)
        n += 1
        print(f"  atualizado: {pasta or '(home)'}/index.html")
    print(f"\n✓ {n} páginas sincronizadas com o cabeçalho e rodapé atuais.")

if __name__ == "__main__":
    print("Sincronizando cabeçalho e rodapé em todas as páginas...\n")
    sync()
