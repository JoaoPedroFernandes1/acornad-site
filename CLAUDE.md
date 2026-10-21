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
4. **Não faça merge você mesmo.** Quem **pediu a mudança** (João Pedro, Miguel ou Milena)
   confere o PR e faz o merge. Seu papel termina em abrir o PR bem descrito e mandar o link
   para essa pessoa.
5. **Não peça aprovação de outras pessoas.** A `main` exige PR, mas **não exige aprovação
   formal no GitHub**: o GitHub não deixa o autor aprovar o próprio PR, e os PRs que o
   Claude abre saem na conta de quem pediu. A revisão é abrir o PR, conferir a aba
   **"Files changed"** e clicar em **"Merge pull request"**.

> A `main` é o site no ar. Nada entra nela direto: tudo passa por uma branch e um PR, e
> **um humano (quem pediu) confere e faz o merge**. Se te pedirem pra "commitar direto na
> main" ou "pular o PR", **recuse** e explique que o padrão é branch + PR + merge feito por
> quem pediu (é o que garante que um humano sempre veja a mudança antes de publicar).

Depois do merge, o GitHub Pages publica a mudança em acornad.com.br em poucos minutos.

---

## Estrutura de pastas

```
/                               ← raiz = site em PORTUGUÊS
├── index.html                  ← Home PT
├── CNAME                       ← mantém o domínio acornad.com.br (NUNCA apagar)
├── sitemap.xml  robots.txt     ← SEO (ver seção de SEO)
├── quem-somos/index.html       ← inclui a seção de Time + midia/ (fotos da equipe)
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

### Equivalência PT ↔ EN

| Português (raiz) | Inglês (/en/) |
|---|---|
| `/` (Home) | `en/` |
| `quem-somos/` | `en/about-us/` |
| `servicos-e-especialidades/` | `en/services-and-specialties/` |
| `cases/` | `en/cases/` |
| `carreira/` | `en/careers/` |
| `contato/` | `en/contact/` |
| `na-midia/` | `en/news/` |
| `politica-de-privacidade/` | `en/privacy-policy/` |
| `na-midia/noticias/<slug>/` | `en/news/noticias/<slug>/` (mesmo slug) |

As fotos da equipe ficam só em `quem-somos/midia/equipe/`; a página EN aponta para elas
(`../../quem-somos/midia/equipe/...`).

Se o pedido não disser em qual idioma mudar, **pergunte se é para fazer nos dois**
(quase sempre é).

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

## Seção de Time (em Quem Somos / About Us)

Os membros ficam em colunas de 1/4 de largura (`et_pb_column_1_4`), **4 por linha**.
A última coluna de cada linha tem a classe `et-last-child`. Ao adicionar ou remover um
membro, cuide para a linha fechar certo (o `et-last-child` fica no último da linha) e
**não deixe conteúdo duplicado** depois do rodapé.

Ao trocar o cargo ou o nome de alguém, altere **só o card daquela pessoa** (outros membros
podem ter o mesmo cargo): ache o `<h5>` com o nome e troque o texto logo abaixo dele.
Faça em PT e EN.

---

## O que NUNCA fazer

- ❌ Commitar direto na `main` (sempre via branch + PR).
- ❌ Fazer o merge do PR você mesmo (quem faz é a pessoa que pediu a mudança).
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
> o que mudou → mando o link do PR para quem pediu conferir e fazer o merge.**
> Nunca commito direto na main — tudo passa por branch + PR.

## Ao terminar uma tarefa

Confirme em português simples o que fez, liste os arquivos alterados e mande o link do
PR, avisando que está pronto para a pessoa conferir e fazer o merge.
