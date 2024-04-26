# DJ Ellen

DJ Ellen é um bot de música para o Discord inspirado na personagem fictícia de uma aventura de RPG. O bot possui comandos para reproduzir música no canal de voz do Discord, com funcionalidades como pausar, retomar, colocar em loop, etc. Para mais informações sobre os comandos, basta usar o comando &help que ensina os demais.

<div style="display: flex; justify-content: space-around; align-items: center;">
    <img src="/imagensREADME/image.png" alt="Bot Ellen DJ" width="100%">
</div>

## Como Usar

O código apresentado é apenas a implementação Back-End do Bot, sendo necessário fazer a integração com o [portal de desenvolvimento de aplicações do Discord](https://discord.com/developers/docs/intro). A execução desse código não tem utilidade nenhuma se o usuário não possuir acesso ao link de inserção do Bot em servidores Discord e ao Token do Bot. Meu intuito é apenas compartilhar a estrutura do código para Bots de música, não a distribuição do Bot, por isso não compartilharei o link de inserção nem o Token do DJ Ellen.

### Pré-requisitos

Certifique-se de ter os módulos Python necessários instalados: discord.py, youtube_dl, PyNaCl e ffmpeg. Você pode instalar os 3 usando pip:

``pip install discord.py youtube_dl PyNaCl``

No caso do ffmpeg, você pode baixar um binário pré-compilado do site oficial do ffmpeg e seguir as instruções de instalação.

### Compilando e Executando o Programa

Certifique-se de que o ambiente Python esteja configurado corretamente com os módulos instalados. Em seguida, você pode iniciar o bot usando o seguinte comando:

`python main.py`

Certifique-se de que o arquivo main.py esteja presente no diretório atual.

## Módulos Utilizados

- **discord:** Uma biblioteca Python que facilita a criação de bots para o Discord.
- **youtube_dl:** Utilizada para baixar vídeos e músicas do YouTube.
- **PyNaCl:** Uma biblioteca Python que fornece binários de libopus e libnacl.
- **ffmpeg:** Uma ferramenta de linha de comando utilizada para converter áudio, vídeo e outros tipos de mídia."
