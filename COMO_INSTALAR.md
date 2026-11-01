# Como colocar no seu GitHub

1. Extraia o ZIP.
2. Abra o repositório público `mariitorrs/mariitorrs`.
3. Envie o `README.md`, a pasta `assets` e a pasta `.github` para a raiz do repositório, substituindo os arquivos anteriores. A capa continua em `assets/capa.gif`; mantenha esse nome e esse caminho.
4. Confirme as alterações e abra [seu perfil](https://github.com/mariitorrs).

Envie os arquivos extraídos, e não o ZIP. Os desenhos precisam da pasta `assets` para aparecer.

## Músicas recentes do Spotify

O card de músicas usa o serviço [spotify-recently-played-readme](https://github.com/kittinan/spotify-recently-played-readme) e não precisa de configuração. Ele atualiza sozinho. Para ele funcionar, o seu perfil do Spotify precisa estar com a atividade pública.

## Cobrinha de contribuições

A seção **Minha atividade no GitHub** usa a cobrinha do arquivo `.github/workflows/snake.yml`. Na aba **Actions**, execute **Generate raspberry contribution snake** em **Run workflow** para gerar a primeira imagem. Ela usa o token automático do GitHub, então não precisa de senha.

As estatísticas dependem de um serviço externo e podem demorar a aparecer.

## Editar depois

- Textos e links: `README.md`.
- Capa: substitua `assets/capa.gif` por outro GIF com o mesmo nome.
- Títulos, tecnologias, projetos e rodapé: edite `build_assets.py` e rode `python build_assets.py`.
- Sprites e jardim em pixel art (framboesa, flor, coração, brilho e a faixa animada): edite `pixel.py` e rode `python pixel.py` na pasta do projeto, ou `python -c "import pixel; pixel.write_all('assets')"`.
- Textos de tecnologias e projetos ficam dentro de `build_assets.py`, então é só trocar as palavras e gerar de novo.
