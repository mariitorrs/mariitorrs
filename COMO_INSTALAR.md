# Como colocar no seu GitHub

1. Extraia o ZIP.
2. Abra o repositório público `mariitorrs/mariitorrs`.
3. Envie o `README.md` e a pasta `assets` para a raiz do repositório, substituindo os arquivos anteriores. A imagem da capa está em `assets/capa.gif`; mantenha esse nome e esse caminho.
4. Confirme as alterações e abra [seu perfil](https://github.com/mariitorrs).

Envie os arquivos extraídos, e não o ZIP. O GIF e os desenhos do README precisam da pasta `assets` para aparecer.

## Cobrinha de contribuições

Se quiser usar a cobrinha da seção **Minha atividade no GitHub**, envie também `.github/workflows/snake.yml`. Como a pasta começa com ponto, alguns seletores podem escondê-la. Nesse caso, crie o arquivo no GitHub usando **Add file → Create new file** e cole o conteúdo nesse caminho.

Na aba **Actions**, execute **Generate raspberry contribution snake** em **Run workflow**. O workflow usa o token automático do GitHub e publica as imagens na branch `output`. Não é necessário colocar uma senha ou um token pessoal no arquivo.

A capa e os demais desenhos funcionam sem executar o workflow. As estatísticas dependem de um serviço externo; a cobrinha depende da primeira execução do workflow.

## Editar depois

- Textos e links: `README.md`.
- Capa: substitua `assets/capa.gif` por outro GIF usando o mesmo nome.
- Cores e desenhos: edite `build_assets.py` e execute `python build_assets.py`. O script usa apenas a biblioteca padrão do Python e não altera a capa.
- Links pessoais: os endereços do LinkedIn, Instagram e Spotify já estão no README.

O `build_assets.py` é opcional para publicar: os desenhos já estão prontos em `assets`.

Referências: [README de perfil — GitHub](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) · [Cobrinha de contribuições — Platane/snk](https://github.com/Platane/snk).
