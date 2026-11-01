# Como colocar no seu GitHub

1. Extraia o ZIP.
2. Abra o repositório público `mariitorrs/mariitorrs`.
3. Envie o `README.md`, a pasta `assets` e a pasta `.github` para a raiz do repositório, substituindo os arquivos anteriores. A capa continua em `assets/capa.gif`; mantenha esse nome e esse caminho.
4. Confirme as alterações e abra [seu perfil](https://github.com/mariitorrs).

Envie os arquivos extraídos, e não o ZIP. Os desenhos precisam da pasta `assets` para aparecer.

## Músicas recentes do Spotify

O card "o que eu ouvi por último" começa com um snapshot do print que você mandou. Para ele atualizar sozinho a cada 30 minutos, faça uma vez:

1. Em [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard), crie um app. Em *Redirect URI*, coloque `http://127.0.0.1:8888/callback` e marque *Web API*.
2. Abra este link no navegador, trocando `SEU_CLIENT_ID` pelo ID do app:
   `https://accounts.spotify.com/authorize?client_id=SEU_CLIENT_ID&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A8888%2Fcallback&scope=user-read-recently-played`
3. Depois de aceitar, o navegador vai para uma página que não abre. Copie o valor de `code` na barra de endereço.
4. No terminal, troque o código pelo *refresh token* (substitua os três valores):
   `curl -X POST https://accounts.spotify.com/api/token -H "Authorization: Basic $(echo -n SEU_CLIENT_ID:SEU_CLIENT_SECRET | base64)" -d grant_type=authorization_code -d code=SEU_CODE -d redirect_uri=http://127.0.0.1:8888/callback`
   O campo `refresh_token` da resposta é o que você precisa.
5. No repositório, vá em **Settings → Secrets and variables → Actions** e crie três segredos: `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` e `SPOTIFY_REFRESH_TOKEN`.
6. Na aba **Actions**, abra **Update Spotify recently played** e clique em **Run workflow**.

Os segredos ficam só no GitHub. Não coloque nenhum deles nos arquivos.

## Cobrinha de contribuições

A seção **Minha atividade no GitHub** usa a cobrinha do arquivo `.github/workflows/snake.yml`. Na aba **Actions**, execute **Generate raspberry contribution snake** em **Run workflow** para gerar a primeira imagem. Ela usa o token automático do GitHub, então não precisa de senha.

As estatísticas dependem de um serviço externo e podem demorar a aparecer.

## Editar depois

- Textos e links: `README.md`.
- Capa: substitua `assets/capa.gif` por outro GIF com o mesmo nome.
- Títulos, tecnologias, projetos e rodapé: edite `build_assets.py` e rode `python build_assets.py`.
- Sprites e jardim em pixel art (framboesa, flor, coração, brilho e a faixa animada): edite `pixel.py` e rode `python pixel.py` na pasta do projeto, ou `python -c "import pixel; pixel.write_all('assets')"`.
- Músicas: rode `python fetch_spotify.py` localmente com os três segredos no ambiente, ou deixe o workflow fazer isso.
- Textos de tecnologias e projetos ficam dentro de `build_assets.py`, então é só trocar as palavras e gerar de novo.
