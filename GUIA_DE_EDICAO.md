# 📘 Guia de Uso e Edição — Site Acorn Advisory

Bem-vindo(a)! Este guia explica como mexer no site sem quebrar nada.
Leia com calma — é mais simples do que parece.

---

## 🗂️ Como o site é organizado

Cada página do site tem sua **própria pasta**. Dentro dela existe:
- Um arquivo **`index.html`** → é a página em si (o que aparece no navegador)
- Uma pasta **`midia/`** → imagens que **só aquela página** usa

```
site_acorn_advisory/
├── index.html              ← HOME em português (página inicial)
├── quem-somos/
│   ├── index.html          ← página "Quem Somos" em português
│   └── midia/              ← imagens dessa página
├── servicos-e-especialidades/
├── cases/
├── carreira/
├── na-midia/
├── contato/
├── politica-de-privacidade/
├── en/                     ← TODO o site em INGLÊS fica aqui dentro
│   ├── index.html          ← HOME em inglês
│   ├── about-us/           ← "Quem Somos" em inglês
│   ├── services-and-specialties/
│   ├── cases/
│   ├── careers/
│   ├── news/
│   └── contact/
├── assets/                 ← COMPARTILHADO por todas as páginas
│   ├── css/style.css       ← as cores, fontes e estilos do site inteiro
│   ├── js/main.js          ← funções (menu do celular)
│   └── img/                ← imagens usadas em várias páginas (logo, ícones)
├── sync_cabecalho.py       ← script para atualizar o menu (ver abaixo)
└── GUIA_DE_EDICAO.md       ← este guia
```

---

## ✏️ Como editar o TEXTO de uma página

1. Abra a pasta da página (ex: `quem-somos/`)
2. Abra o arquivo **`index.html`** num editor de texto
   (recomendado: **VS Code**, gratuito — https://code.visualstudio.com)
3. Procure a parte marcada com:
   ```
   <!-- ===== CONTEÚDO DA PÁGINA — EDITE AQUI ===== -->
   ```
4. **Só edite o texto entre as tags.** Exemplo:
   ```html
   <h1>Quem Somos</h1>          ← troque "Quem Somos" pelo texto novo
   <p>Texto do parágrafo...</p>  ← troque o texto do parágrafo
   ```
5. Salve o arquivo (Ctrl+S)

### ⚠️ O que NÃO mexer
- **Não apague** as `<tags>` (as coisas entre `<` e `>`)
- **Não mexa** no cabeçalho (menu) nem no rodapé direto na página
  (eles são atualizados pelo script — ver seção do menu)
- **Não mexa** nos nomes das pastas nem dos arquivos `index.html`

---

## 🖼️ Como trocar uma IMAGEM

1. Coloque a imagem nova na pasta **`midia/`** daquela página
   (ou em `assets/img/` se for usada em várias páginas)
2. No `index.html`, procure a imagem antiga:
   ```html
   <img src="midia/foto-antiga.jpg" alt="...">
   ```
3. Troque o nome do arquivo:
   ```html
   <img src="midia/foto-nova.jpg" alt="...">
   ```
4. Salve

💡 **Dica**: mantenha as imagens leves (menos de 300 KB) para o site carregar rápido.
Use JPG para fotos e PNG para logos/ícones com fundo transparente.

---

## 🍔 Como mudar o MENU (cabeçalho) ou o RODAPÉ

O menu aparece em **todas as páginas**. Para não ter que editar página por página,
existe um script que atualiza tudo de uma vez.

1. Abra o arquivo **`sync_cabecalho.py`**
2. No topo, edite a parte `MENU` e `LINKS` (nomes e destinos dos itens)
3. Salve
4. Rode o script (precisa ter o Python instalado):
   ```
   python sync_cabecalho.py
   ```
5. Pronto — o menu foi atualizado em todas as 16 páginas

⚠️ **Importante**: sempre edite o menu **pelo script**, nunca direto nas páginas.
Se editar direto numa página, sua mudança será apagada na próxima sincronização.

---

## 👀 Como TESTAR antes de publicar

Antes de subir qualquer mudança, veja como ficou:

**Jeito simples:** dê duplo clique no `index.html` → abre no navegador

**Jeito melhor** (links funcionam certinho):
1. Abra o terminal na pasta do site
2. Rode: `python -m http.server 8000`
3. Abra no navegador: `http://localhost:8000`
4. Navegue pelo site como um visitante veria

---

## 🚀 Como PUBLICAR as mudanças

O site fica hospedado no GitHub Pages. Depois de editar e testar:

1. Suba os arquivos alterados para o repositório no GitHub
   (via GitHub Desktop, VS Code, ou upload no site do GitHub)
2. Em 1-2 minutos, a mudança aparece no site no ar

*(A equipe técnica configura o GitHub — peça ajuda na primeira vez.)*

---

## ❓ Dúvidas frequentes

**"Editei e quebrou o visual, e agora?"**
→ Você provavelmente apagou uma tag sem querer. Desfaça (Ctrl+Z) ou
   peça a versão anterior para a equipe técnica (o Git guarda o histórico).

**"Como adiciono uma página nova?"**
→ Peça para a equipe técnica — envolve criar a pasta, o `index.html`
   e adicionar no menu (script). Não faça sozinho na primeira vez.

**"Posso editar direto pelo GitHub, no navegador?"**
→ Pode, para mudanças de texto simples. Mas teste sempre depois.

---

## 📞 Contato técnico

Dúvidas ou algo quebrou? Fale com o time de Tecnologia/Operações.

*Última atualização deste guia: pela equipe técnica.*
