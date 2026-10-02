# 📁 Organização dos Assets

Estrutura das pastas de recursos do site:

## assets/
- **css/** — folhas de estilo do site
- **js/** — scripts (carrosséis, menu, etc.)
- **fonts/** — fontes de ícones (setas, redes sociais)
- **img/** — todas as imagens, organizadas por categoria:
  - **marca/** — logos da Acorn (logo-acorn.png, logo-rodape.png, favicon.png)
  - **home/** — imagens da home (hero-fundo.jpg, mapa-mundi.png, mapa-textura.png, etc.)
  - **cases/** — logos/cards dos cases (abs-britech.png, metadados-volaris.png, etc.)
  - **icones/** — ícones dos serviços (servico-ma.png, servico-captacao.png, etc.)
  - **ui/** — elementos de interface (aspas.png, grafismo.png, bandeira-pt.svg, etc.)

## Como trocar uma imagem
1. Coloque a nova imagem na pasta certa (ex: um case novo vai em `img/cases/`)
2. No HTML da página, troque o caminho `assets/img/cases/nome-antigo.png` pelo novo
3. Mantenha o mesmo tamanho/proporção da imagem original pra não quebrar o layout

## Nomes das imagens (referência rápida)
| Categoria | Exemplos |
|-----------|----------|
| Logos | logo-acorn.png, logo-rodape.png, favicon.png |
| Home | hero-fundo.jpg, mapa-mundi.png, negocio-unico-textura.png |
| Serviços | servico-ma.png, servico-captacao.png, servico-assessoria.png |
| UI | aspas.png, grafismo.png, bandeira-pt.svg, bandeira-en.svg |
