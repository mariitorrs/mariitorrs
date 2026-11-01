# Como publicar o perfil da Mari

1. Crie um repositório público chamado `mariitorrs` em https://github.com/new (precisa ser idêntico ao usuário).
2. Faça upload de **todo o conteúdo desta pasta**, mantendo `README.md`, `assets/` e `.github/workflows/snake.yml` nos mesmos caminhos. O upload pelo navegador pode ocultar pastas começando com ponto; nesse caso use Git ou crie `.github/workflows/snake.yml` em Add file → Create new file. (Os arquivos `build_assets.py` e `shot.py` são opcionais, só servem para regenerar os SVGs.)
3. Na aba **Actions**, habilite workflows e execute **Generate pink contribution snake** em Run workflow. Ele cria a branch `output` com a cobrinha clara e escura; até lá a imagem fica vazia.
4. (Opcional) Spotify: autorize em https://spotify-recently-played.jeffreyca.workers.dev/ , gere o snippet e descomente o bloco da seção "soundtrack" no README.
5. Veja o resultado em https://github.com/mariitorrs.

Tudo que é desenho (banner, cards, divisor, gatinho) são SVGs locais animados em `assets/`. Ícones (skillicons), badges (shields.io) e estatísticas (github-readme-stats) dependem de serviços externos, e o card de estatísticas pode sofrer rate limit às vezes.
Para editar textos dos cards ou do banner, mexa em `build_assets.py` e rode `python3 build_assets.py`.
