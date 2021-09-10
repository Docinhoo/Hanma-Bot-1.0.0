#Segurança do codigo no Replit Token Oculto
from decouple import config

#Biblioteca principal do Discord + setações para funcionamento
import discord
from discord.ext import commands
intents = discord.Intents().all()
bot = commands.Bot(command_prefix = "a$", intents = intents)

#Saber se o bot está ativo pelo terminal
@bot.event
async def on_ready():
    print("Estou pronto! Eu sou o", bot.user)

#Mensagens de boas vindas para novos membros e adição do cargo inicial
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Novatos')
    await member.add_roles(role)
    canalboasvindas = bot.get_channel(880082985959981056)
    regras = bot.get_channel(880083121435967548)
    intro = bot.get_channel(880083212834066462)
    inicio = discord.Embed(
    title = f'Eae novato beleza?',
    description = f'Então  {member.mention}, na Toman vc tem que escolher uma divisão para permanecer no servidor, escolha a sua e divirta-se!',
    colour = 6684672
    )
    inicio.set_author(name="Cc: Draken, vice comandante da Toman")
    inicio.add_field(name="\nENTRE EM UMA DIVISÃO:\n", value=f"\n{intro.mention}\n")
    inicio.add_field(name="\nLEIA AS REGRAS!\n", value=f"\n{regras.mention}\n")
    inicio.set_image(url='https://c.tenor.com/gmciOFywerkAAAAd/tokyo-revengers-draken.gif')
    await canalboasvindas.send(embed = inicio)

#censura de palavrões
bad_words = {'cu','puta','foder'}
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  message_split =message.content.split(" ")
  for message_word in message_split:
    for bad_word in bad_words:
      if bad_word == message_word.lower():
        await message.delete()
        await message.channel.send("Escreva algo melhor seu merda!")

  await bot.process_commands(message)

#Escolha de cargo feita pelo usuario por meio de reação
@bot.event
async def on_reaction_add(reaction, user):
  print(reaction.emoji)
  if reaction.emoji == '1️⃣':
    role = user.guild.get_role(880090595538894869)
    await user.add_roles(role)
    first = user.guild.get_role(882389737497829506)
    await user.remove_roles(first)
  elif reaction.emoji == '2️⃣':
    role = user.guild.get_role(880090912175308950)
    await user.add_roles(role)
    first = user.guild.get_role(882389737497829506)
    await user.remove_roles(first)
  elif reaction.emoji == '3️⃣':
    role = user.guild.get_role(880091202807005235)
    await user.add_roles(role)
    first = user.guild.get_role(882389737497829506)
    await user.remove_roles(first)
  elif reaction.emoji == '4️⃣':
    role = user.guild.get_role(880091411574304878)
    await user.add_roles(role)
    first = user.guild.get_role(882389737497829506)
    await user.remove_roles(first)

#comando de dizer no servidor basico
@bot.command(name="oi")
async def send_message(ctx):
  name = ctx.author.name
  response = "Ola, " + name
  await ctx.send(response)

#comando de versão
@bot.command(name="versao")
async def version(ctx):
  await ctx.send("Atual versão do Hanma: 1.0.0")

#help 
@bot.command(name="ajuda")
async def help(ctx):
  try:
    hanma = discord.Embed( 
      title="Principais comandos para usuários:",
      description="Hanma Bot desenvolvido apenas para o servidor da Toman e atual está na sua versão 1.0.0",
      colour= 2551930
      )
    hanma.add_field(name="$regras", value="regras do servidor")
    hanma.add_field(name="$oi", value="receber um oi do Bot")
    hanma.add_field(name="$ajuda", value="informações do Hanma")
    hanma.add_field(name="$versao", value="versao atual do hanma")
    await ctx.author.send(embed = hanma)
  except discord.errors.Forbidden:
    await ctx.send("Habilite receber mensagens privada de qualquer pessoa no servidor(Opções > Privacidade)")
#embed das divisões
@bot.command(name="divisao")
async def send_embed(ctx):
  teste = discord.Embed(
    title = 'Escolha a sua divisão',
    description = 'No servidor da Toman você pode escolher entre as 4 principais divisões, cada uma delas tem uma função dentro do servidor e suas próprias caracteristicas\n',
    colour = 6684672
    )
  teste.set_author(name="Vice comandante da Toman, Draken", icon_url= 'https://uploads.spiritfanfiction.com/fanfics/capitulos/202107/meu-pequeno-anjinho--draken-e-leitor-22699268-210720211210.jpg'
  )
  teste.add_field(name="1ª Divisão", value="A 1ª divisão enxerga longe, possui uma visão privilegiada e vasta. Sendo assim, trará soluções e práticas inovadoras para o servidor. Costuma ter uma boa visão geral da situação, usando sua intuição e sua criatividade para fazer a diferença.\n", inline = False )
  teste.add_field(name="2ª Divisão", value="Determinados e focados, o perfil da 2ª divisão compreende as pessoas que são mais ligadas a desafio, múltiplas funções e foco em resultado.\nExecutam suas funções de forma organizada,com rapidez e qualidade. Contudo, sendo bastantes autossuficientes, o trabalho em grupo pode ser um empecilho.", inline = False )
  teste.add_field(name="3ª Divisão",value="Brincalhão, carismático e carinhoso, o perfil da 3ª divisão representa os profissionais que preferem trabalhar em equipe, com muita colaboração e de forma harmônica. No geral, são pessoas fáceis de lidar, extrovertidos e persuasivos.\n", inline = False )
  teste.add_field(name="4ª Divisão", value="A 4ª divisão tem como características de personalidade ser fiel à sua matilha, ser meticuloso e organizado. Realiza suas tarefas de forma planejada, definindo regras e com responsabilidade.\n", inline = False)

  teste.set_footer(
   text="Feito por Draken."
  )
  await ctx.send(embed = teste)

#embed das divisões
@bot.command(name="regras")
async def rule_embed(ctx):
  regra = discord.Embed(
    title = '*10 REGRAS GERAIS DA TOMAN*',
    description = 'A infração das regras pode gerar 4 tipos de consequencias: **leves, medias, graves e InstaBan**\n',
    colour = 6684672
    )
  regra.set_author(name="Cc: Mikey Sano, líder geral da Toman")
  regra.add_field(name="1ª Regra", value="Não ficar militando ou enchendo o saco tanto no Chat geral, quanto no privado.\nInfração: **Media**", inline = False)
  regra.add_field(name="2ª Regra", value="Não ficar falando merda, discurso idiotas ou spam.\nInfração: **Média**", inline = False)
  regra.add_field(name="3ª Regra", value="Respeitar hierarquias dentro do servidor.\nInfração: **Leve**", inline = False)
  regra.add_field(name="4ª Regra", value="Não fazer perguntas de maneira idiota.\nInfração: **Leve**", inline = False)
  regra.add_field(name="5ª Regra", value="Não fazer piada palha.\nInfração: **Leve**", inline = False)
  regra.add_field(name="6ª Regra", value="Gostar de BlackPink.\nInfração: **Leve**", inline = False)
  regra.add_field(name="7ª Regra", value="Não apoiar o bolsonaro.\nInfração: **InstaBan e ainda é xingado**", inline = False)
  regra.add_field(name="8ª Regra", value="Não sair e entrar toda hora no servidor.\nInfração: **Média**", inline = False)
  regra.add_field(name="9ª Regra", value="Abusar de cargos majoritários.\nInfração: **Grave**", inline = False)
  regra.add_field(name="10ª Regra", value="Não se chamar Eduardo Bettiol.\nInfração: **InstaBan**", inline = False)
  regra.set_footer(text="*Ademais, cada divisão tem autonomia de colocar regras proprias dada aprovação pelo Lider ou Vice-lider da Toman*")
  await ctx.send(embed = regra)




#BOT INICIANDO
TOKEN = config ("TOKEN")
bot.run(TOKEN)
