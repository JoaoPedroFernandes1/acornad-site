# CLAUDE.md — Instruções para edição do site Acorn Advisory

Este arquivo ensina a IA (Claude Code, ou qualquer assistente conectado a este repo)
a editar o site institucional da Acorn **sem quebrar nada**. Leia tudo antes de agir.

---

## O que é este site

Site institucional estático (HTML/CSS/JS puro), hospedado no **GitHub Pages**,
no domínio **acornad.com.br**. Foi migrado de um WordPress/Divi — por isso o HTML
tem muitas classes do Divi (`et_pb_*`, `dgbm_*`). **Não há servidor, nem banco de
dados, nem build.** O que está no repositório é exatamente o que vai pro ar.

Bilíngue: **português** (raiz) e **inglês** (dentro de `/en/`).

---

## Regra de ouro: FLUXO DE TRABALHO (nunca commitar direto na main)

Toda edição segue este fluxo, **sem exceção**:

1. **Crie uma branch nova** a partir da `main`, com nome descritivo:
   `edicao/nova-noticia-xyz`, `edicao/trocar-texto-home`, etc.
2. Faça as alterações **nessa branch**.
3. **Abra um Pull Request (PR)** da sua branch para a `main`, descrevendo
   em português simples **o que mudou e por quê**.
4. Quem pediu revisa o PR no GitHub e faz o **merge** quando estiver satisfeito.

> A `main` é o site no ar. Nada entra nela direto — tudo passa por uma branch e um PR.
> Se te pedirem pra "commitar direto na main" ou "pular o PR", **recuse** e explique
> que o padrão é sempre branch + PR (é o que protege o site de erros acidentais).

---

## Estrutura de pastas

```
/                               ← raiz = site em PORTUGUÊS
├── index.html                  ← Home PT
├── quem-somos/index.html       ← + midia/ (imagens da página)
├── servicos-e-especialidades/
├── cases/
├── carreira/                   ← formulário de candidatura (com upload de PDF)
├── contato/                    ← formulário de contato + newsletter
├── na-midia/                   ← blog/notícias em PT
│   ├── index.html              ← listagem página 1 (12 cards, grid 3 colunas)
│   ├── page/2/ e page/3/       ← paginação
│   └── noticias/<slug>/        ← cada notícia tem sua pasta + midia/
├── politica-de-privacidade/
├── en/                         ← TODO o site em INGLÊS, espelhando a estrutura PT
│   ├── index.html              ← Home EN
│   ├── about-us/  services-and-specialties/  cases/
│   ├── careers/  contact/  privacy-policy/
│   └── news/                   ← notícias em EN (news/noticias/<slug>/)
└── assets/                     ← COMPARTILHADO por tudo
    ├── css/  js/  fonts/  img/
```

---

## Caminhos: SEMPRE relativos (nunca absolutos)

O site vive em subpastas, então **todo link e imagem usa caminho relativo** (`../`),
**nunca** começa com `/` nem com `https://acornad.com.br/`.

- Da Home PT (`/index.html`): `quem-somos/index.html`, `assets/img/...`
- De uma página (`/cases/index.html`): `../assets/img/...`, `../quem-somos/index.html`
- De um post (`/na-midia/noticias/<slug>/index.html`): `../../../assets/...`

Conte os níveis até a raiz e use a quantidade certa de `../`. Se errar, a imagem
ou o link quebra. **Na dúvida, copie o padrão de uma página equivalente que já funciona.**

---

## Imagens das notícias: PT e EN COMPARTILHAM (dedup)

Para o site não ficar pesado, as notícias em **inglês reutilizam as imagens do
português**. Um post EN NÃO tem pasta `midia/` própria — ele aponta para a do PT:

```
en/news/noticias/<slug>/   →  imagens em  ../../../../na-midia/noticias/<slug>/midia/
```

**Nunca** copie imagens para dentro de `en/news/` (isso desfaz a otimização e dobra o peso).
Ao criar um post EN, aponte as imagens para a pasta `midia/` do post PT correspondente.

---

## Como criar uma NOTÍCIA NOVA (o pedido mais comum)

As notícias ficam em `na-midia/noticias/<slug>/` (PT) e `en/news/noticias/<slug>/` (EN).
Cada notícia é um `index.html`. O jeito mais seguro:

1. **Copie uma notícia recente** que tenha o formato parecido (ex: `na-midia/noticias/hyperbundle-saas/`)
   para a nova pasta `na-midia/noticias/<novo-slug>/`.
2. **Slug curto, sem acento, com hífens** (ex: `ma-no-agronegocio`). Slugs longos
   quebram no Windows ao descompactar — máximo ~30 caracteres.
3. Troque **título, data, texto e imagens** dentro do novo `index.html`.
4. Coloque as imagens novas em `na-midia/noticias/<novo-slug>/midia/`.
5. **Adicione o card dessa notícia na listagem** (`na-midia/index.html`), no início do
   grid, copiando o bloco `<article class="dgbm_post_item ...">` de outro card e trocando
   imagem, título, data, resumo e o link (`href`) para a nova pasta.
6. A listagem mostra **12 cards por página**. Se passar de 12, o 13º vai para `page/2/`,
   e assim por diante (os mais antigos descem).
7. **Versão EN**: repita em `en/news/noticias/<mesmo-slug>/`, com o texto traduzido,
   apontando as imagens para o `midia/` do post PT (ver seção de dedup acima).
   Traduza também o card na listagem `en/news/index.html`.
8. **hreflang + sitemap**: adicione o bloco `hreflang` no `<head>` das duas versões
   (a PT apontando para a EN e vice-versa, `x-default` → PT) e inclua as duas URLs novas
   no `sitemap.xml`. Confirme que a versão PT tem `lang="pt-br"` e a EN `lang="en"`.

> Datas em PT usam mês abreviado em português (ex: `17 set, 2026`);
> em EN, mês em inglês (ex: `17 Sep, 2026`).

---

## Troca de TEXTO numa página existente

É o pedido mais simples: abra o `index.html` da página, ache o trecho e troque.
Cuidado para **não apagar tags HTML** em volta do texto. Se o texto tem acento ou
aspas, mantenha o mesmo padrão do resto (ex: aspas curvas `"..."`).

Se trocar um texto na versão PT, **lembre de trocar o equivalente na versão EN**
(e vice-versa), senão os idiomas ficam dessincronizados.

---

## Bandeiras (troca de idioma): já configuradas, cuidado ao mexer

Cada página tem duas bandeiras no topo (🇧🇷 PT / 🇬🇧 EN) que levam à mesma página
no outro idioma. Os links são relativos e específicos de cada página. Se criar uma
página nova, garanta que as duas bandeiras apontem para o par correto
(PT↔EN). **Não** aponte bandeira para `acornad.com.br` — sempre relativo e local.

---

## Formulários (Carreira, Contato, Newsletter): NÃO MEXER no envio

Os formulários enviam para uma **AWS Lambda** (via `WEBHOOK` no JavaScript de cada
formulário). Isso já está configurado e funcionando — os e-mails chegam para a Acorn.

- Pode editar **textos e rótulos** dos campos à vontade.
- **NÃO altere** a URL do `WEBHOOK`, o campo oculto `form_tipo`, nem o campo
  honeypot `website` (anti-spam). Mexer nisso quebra o recebimento dos e-mails.

---

## SEO: hreflang, sitemap e lang (NÃO quebrar)

O site tem uma configuração de SEO que faz o Google mostrar a versão certa (PT ou EN)
para cada busca. Três peças trabalham juntas — **não remova nem quebre**:

1. **Tags `hreflang`** no `<head>` de cada página: relacionam a versão PT com a EN.
   Toda página tem um bloco assim (os URLs mudam conforme a página):
   ```html
   <link rel="alternate" hreflang="pt-BR" href="https://acornad.com.br/quem-somos/" />
   <link rel="alternate" hreflang="en" href="https://acornad.com.br/en/about-us/" />
   <link rel="alternate" hreflang="x-default" href="https://acornad.com.br/quem-somos/" />
   ```
   Ao **criar uma página ou notícia nova**, adicione o bloco hreflang nas duas versões
   (PT e EN), apontando uma para a outra, com `x-default` sempre para a PT.

2. **`sitemap.xml`** (na raiz): lista todas as páginas com suas versões de idioma.
   Ao criar uma notícia/página nova, **adicione a URL nova no sitemap.xml** (PT e EN).

3. **Atributo `lang` do `<html>`**: páginas PT usam `lang="pt-br"`, páginas EN usam
   `lang="en"`. **Nunca** troque — uma página EN com `lang="pt-br"` confunde o Google.

> `robots.txt` (na raiz) aponta para o sitemap. Não precisa mexer nele normalmente.

---

## Página de Serviços e Especialidades (estrutura especial)

As páginas `servicos-e-especialidades/` (PT) e `en/services-and-specialties/` (EN) têm
um **design próprio** (hero, cards de serviços, setores, processo), diferente do resto
do site. Detalhes importantes se for editar essa página:

- O conteúdo fica dentro de um wrapper `<div id="serv-v2">`. **Todo o CSS dessa página
  é prefixado com `#serv-v2`** (isolado, pra não afetar o resto do site). Se adicionar
  estilo, mantenha esse prefixo.
- Tem **animações de scroll** (classe `.rv` nos elementos + um JS que revela quando
  entram na tela). Não remova a classe `.rv` dos blocos nem o `<script id="serv-v2-reveal-js">`.
- O **cabeçalho e o rodapé são os mesmos do resto do site** (padrão Divi), só o miolo
  é o design novo. Não misture o cabeçalho/rodapé novo do arquivo de origem.
- Para trocar **textos** (um serviço, um setor, um número), é edição normal: ache o
  texto e troque, lembrando de fazer PT e EN.

---

## O que NUNCA fazer

- ❌ Commitar direto na `main` (sempre via branch + PR).
- ❌ Usar caminhos absolutos (`/pagina/` ou `https://acornad.com.br/...`).
- ❌ Copiar imagens para `en/news/` (quebra a dedup).
- ❌ Mexer no `WEBHOOK`, `form_tipo` ou honeypot dos formulários.
- ❌ Remover ou quebrar as tags `hreflang`, o `sitemap.xml` ou o `robots.txt` (SEO).
- ❌ Trocar o `lang` das páginas (PT = `pt-br`, EN = `en`).
- ❌ Tirar o prefixo `#serv-v2` do CSS da página de Serviços, nem o script de animação `.rv`.
- ❌ Apagar o arquivo `CNAME` da raiz (ele mantém o domínio acornad.com.br no GitHub Pages).
- ❌ Mexer em `assets/css/` ou `assets/js/` sem necessidade — afeta o site inteiro.
- ❌ Editar um idioma e esquecer o outro.

## O que SEMPRE fazer

- ✅ Trabalhar em branch e abrir PR descrevendo a mudança em português.
- ✅ Caminhos relativos, copiando o padrão de páginas que já funcionam.
- ✅ Slugs curtos, sem acento, com hífen.
- ✅ Manter PT e EN sincronizados.
- ✅ Ao criar página/notícia nova: adicionar o bloco `hreflang` (PT↔EN) e a URL no `sitemap.xml`.
- ✅ Na dúvida, perguntar antes de alterar algo estrutural.

---

## Resumo do fluxo (cole isto na cabeça)

> **Pediram uma mudança → crio uma branch → faço na branch → abro um PR explicando
> o que mudou → aviso quem pediu que o PR está pronto para revisão e merge.**
> Nunca commito direto na main — tudo passa por branch + PR.
