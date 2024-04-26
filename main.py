import discord
import youtube_dl

# Define as intenções do bot
intents = discord.Intents.default()
intents.voice_states = True
intents.messages = True
intents.message_content = True

# Cria o cliente Discord com as intenções especificadas
client = discord.Client(intents=intents)

players = {}
COR = 0xFF007F
repeat_mode = False

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")
    print("===================")

@client.event
async def on_message(message):
    global repeat_mode
    
    if message.author == client.user:
        return

    if message.content.startswith('&entrar'):
        if message.author.voice:
            channel = message.author.voice.channel
            try:
                await channel.connect()
                embed = discord.Embed(
                    description="**Hmm... Oi.** - Vocês olham para o lado e ela está ali.",
                    color=COR
                )
                await message.channel.send(embed=embed)
            except discord.ClientException as error:
                await message.channel.send(f"Erro: {error}")
        else:
                embed = discord.Embed(
                    description="**Você não tá na call, você é burro?** - Olhar de julgamento...",
                    color=COR
                )
                await message.channel.send(embed=embed)

    if message.content.startswith('&sair'):
        if message.guild.voice_client:
            await message.guild.voice_client.disconnect()
            embed = discord.Embed(
                description="Vocês olham para o lado e ela não está ali mais.",
                color=COR
            )
            await message.channel.send(embed=embed)

    if message.content.startswith('&p '):
        yt_url = message.content[3:]
        if not message.guild.voice_client:
            if message.author.voice:
                channel = message.author.voice.channel
                try:
                    await channel.connect()
                except discord.ClientException as error:
                    await message.channel.send(f"Erro: {error}")
            else:
                embed = discord.Embed(
                    description="**Você não tá na call, você é burro?** - Olhar de julgamento...",
                    color=COR
                )
                await message.channel.send(embed=embed)
                return

        voice_client = message.guild.voice_client
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        options = {
            'format': 'bestaudio/best',
            'quiet': True,
            'verbose': True,  # Habilita o modo verbose
        }
        ydl = youtube_dl.YoutubeDL(options)
        info = ydl.extract_info(f"ytsearch:{yt_url}", download=False)
        if 'entries' in info and info['entries']:
            url2 = info['entries'][0]['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            if voice_client.is_playing():
                voice_client.stop()  # Para a música atual
            voice_client.play(source, after=lambda e: repeat_check(e, voice_client, url2))
            embed = discord.Embed(
                    description="**VAMO BOTAR PRA... Minha mãe não gosta que eu fale essas coisas.**",
                    color=COR
            )
            await message.channel.send(embed=embed)
            embed = discord.Embed(
                    description=f"**Depois dessa vou tocar a do Thomas:** {info['entries'][0]['title']}",
                    color=COR
            )
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                    description="**Esse link não existe ou tá estragado, muda.**",
                    color=COR
            )
            await message.channel.send(embed=embed)

    if message.content.startswith('&parar'):
        if message.guild.voice_client and message.guild.voice_client.is_playing():
            message.guild.voice_client.pause()
            embed = discord.Embed(
                description="**PARA!!!** - Ellen tropeça no fio.",
                color=COR
            )
            await message.channel.send(embed=embed)

    if message.content.startswith('&voltar'):
        if message.guild.voice_client and message.guild.voice_client.is_paused():
            message.guild.voice_client.resume()
            embed = discord.Embed(
                description="**VOLTA!!!** - Ellen religou o fio.",
                color=COR
            )
            await message.channel.send(embed=embed)

    if message.content.startswith('&repeat'):
        repeat_mode = not repeat_mode
        embed = discord.Embed(
            description=f"{'**Vai tocar várias vezes a mesma... que chato.**' if repeat_mode else '**Hmm... Chega de repetir, tá chato.**'}",
            color=COR
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('&help'):
        embed = discord.Embed(
            description="**Hmm... Aqui, escolhe:**\n",
            color=COR
        )
        embed.add_field(name="&entrar", value="Entra no canal de voz do usuário", inline=False)
        embed.add_field(name="&sair", value="Sai do canal de voz e para a música", inline=False)
        embed.add_field(name="&p [link]", value="Toca a música do YouTube", inline=False)
        embed.add_field(name="&parar", value="Pausa a música", inline=False)
        embed.add_field(name="&voltar", value="Retoma a música pausada", inline=False)
        embed.add_field(name="&repeat", value="Ativa/desativa o modo de repetição", inline=False)
        embed.add_field(name="&help", value="Mostra todos os comandos disponíveis", inline=False)
        await message.channel.send(embed=embed)

def repeat_check(error, voice_client, url):
    global repeat_mode
    if not error:
        if repeat_mode and voice_client.is_connected() and not voice_client.is_playing():
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            source = discord.FFmpegOpusAudio(url, **FFMPEG_OPTIONS)
            voice_client.play(source, after=lambda e: repeat_check(e, voice_client, url))

client.run('token')