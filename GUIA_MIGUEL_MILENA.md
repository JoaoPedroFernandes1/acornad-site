# 📝 Guia rápido — Como editar o site da Acorn (Miguel e Milena)

Oi! Este guia é pra vocês conseguirem **atualizar o site sem saber programar**.
Vocês vão conversar com uma IA (em português normal) e ela faz as mudanças.
Vocês conferem e publicam. Simples assim.

---

## 🧠 A ideia em 1 minuto

- Vocês **pedem** a mudança escrevendo em português (como se pedissem pra um colega).
- A IA **prepara** a alteração numa "versão de teste" (uma *branch*) e abre um **PR**
  (um pedido de publicação) — nada mexe no site no ar ainda.
- Um de vocês **confere, aprova e publica** quando estiver do jeito que querem.

Ou seja: nada vai pro site no ar automaticamente. A IA faz, mas **uma pessoa sempre
revisa e aprova** antes de publicar. Vocês são os responsáveis pelo site.

---

## ✅ Como pedir bem (quanto mais claro, melhor)

Pensem como se estivessem explicando pra uma pessoa. Dê **todos os detalhes**:

### Exemplo 1 — Publicar uma notícia nova
> "Quero publicar uma notícia nova na seção Na Mídia.
> **Título:** Acorn assessora venda da Empresa X para a Empresa Y
> **Data:** 15 de outubro de 2026
> **Texto:** [cola aqui o texto completo da notícia]
> **Imagem:** [anexa a imagem ou descreve qual usar]
> Faz também a versão em inglês, traduzindo o texto."

### Exemplo 2 — Trocar um texto
> "Na página Quem Somos, troca o parágrafo que começa com 'Somos uma boutique...'
> pelo novo texto: [cola o texto novo]. Faz igual no inglês."

### Exemplo 3 — Atualizar a equipe
> "Na página Quem Somos, adiciona um novo membro da equipe:
> **Nome:** Fulano de Tal | **Cargo:** Analista | **Foto:** [anexa]"

### Exemplo 4 — Trocar um número/dado
> "Na Home, onde diz 'R$ X bilhões em transações', muda pra 'R$ Y bilhões'.
> Atualiza no português e no inglês."

---

## 💡 Dicas pra não dar erro

- **Dê o texto pronto.** A IA escreve bem, mas o conteúdo (nomes, valores, datas)
  tem que vir de vocês, certinho.
- **Diga sempre se é pra fazer nos dois idiomas** (português E inglês). Quase sempre é.
- **Uma coisa de cada vez.** Prefira pedir "adiciona essa notícia" do que "adiciona
  essa notícia, muda a home, troca a foto do time e o rodapé" tudo junto.
- **Mande as imagens** junto do pedido (ou diga exatamente qual imagem usar).
- **Revise o texto antes de mandar** — ortografia, nomes de empresas, valores.

---

## ⚠️ O que pedir com cautela (coisas de maior risco)

Essas coisas mexem na estrutura do site e têm mais risco. Vocês **podem** fazer,
mas com cautela extra (e, se tiver qualquer dúvida, chamem o suporte técnico — o João Pedro):

- Mudar o **layout** / as cores / o menu do site
- Mexer nos **formulários** (os campos de Contato, Carreira, Newsletter)
- Criar uma **página totalmente nova** (tipo uma seção que não existe)

O dia a dia (notícias, textos, equipe, dados), podem pedir à vontade — é seguro.

---

## 🔄 O que acontece depois que vocês pedem

1. A IA prepara a mudança numa branch e abre um **PR** (pedido de publicação).
2. Vocês abrem o PR no GitHub e veem **exatamente o que mudou** (a aba "Files changed").
3. Se estiver bom:
   - Clicam em **"Review changes"** (ou "Add your review") → **"Approve"** → enviam.
   - Depois, botão **"Merge pull request"** → confirmam. Agora sim publica.
   Se quiser ajustar algo, é só pedir à IA que ela corrige na mesma branch, antes de aprovar.
4. Em ~1 minuto depois do merge, já está no site **acornad.com.br**.

> **Detalhe importante:** o site exige **1 aprovação** antes de publicar, e o GitHub
> **não deixa a mesma pessoa que abriu um PR aprovar o próprio PR**. Como é a **IA** quem
> abre o PR, qualquer um de vocês dois pode aprovar sem problema. Mas se um dia um de vocês
> abrir um PR na mão (sem a IA), o **outro** é quem aprova. Por isso vocês dois têm acesso —
> um sempre pode aprovar o do outro.

Nada vai pro ar sem a aprovação + o merge. Vocês controlam o que publica e quando.

---

## 🆘 Deu alguma dúvida?

- Não entendeu o que a IA fez? **Pergunta pra ela** em português ("o que você mudou?").
- Achou que ficou errado? **Fala** — ela refaz na branch, antes de você publicar.
- Deu algo grave, ou ficou inseguro(a)? **Chama o João Pedro** (suporte técnico).

**Relaxa:** como tudo passa por uma versão de teste (branch) antes de publicar, dá
sempre pra conferir e corrigir antes. E se algo der errado depois de publicado, o
histórico permite voltar atrás. Podem trabalhar com tranquilidade. 🚀
