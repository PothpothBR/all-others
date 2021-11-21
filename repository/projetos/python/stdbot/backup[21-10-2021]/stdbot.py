# para dados basicos <nome do bot> <porta do servidor> <info de status>
import sys

args = {}

for i in range(len(sys.argv)):
    try:
        if sys.argv[i].lower() == "-bot":
            args.update({"bot": sys.argv[i+1]})
        if sys.argv[i].lower() == "-ip":
            args.update({"ip": sys.argv[i+1]})
        if sys.argv[i].lower() == "-port":
            args.update({"port": sys.argv[i+1]})
    except:
        print("    argumentos inseridos invalidos")

#para reiniciar o sistema
import os

# para a contagem de tempo ativo, e data formatada
from timer import *

# conexao de servico interno entre os boots
from botconnection import Network, SERVER

# sistema de gerenciamento de dados
from datalog import DataManager

# conexao com o discord
import discord
from discord.ext import tasks
import asyncio

# import com a colecao de token de acesso dos bots
from tokens import TOKEN

def reboot():
    os.execl(sys.executable, sys.executable, *sys.argv)

net = Network(args["ip"], args["port"], SERVER)

# inicia o gerenciador de data
data = DataManager("{}.data".format(sys.argv[1]), "bots.log")

# inicia o relogio de atividade do bot
up_timer = Timer("uptime", 5)

# inicia o cliente discord
client = discord.Client()


async def bot_uptime():
    uptime = up_timer.tick()
    await client.change_presence(activity=discord.Game(name="Up time: {}:{}:{}".format(uptime[0], uptime[1], uptime[2])))


@tasks.loop(seconds=5)
async def main_loop():
    await bot_uptime()


@client.event
async def on_ready():
    print("    Iniciando bot {} em {}".format(client.user.name, strdate()))
    main_loop.start()
    await client.get_channel(845377674116726834).send(":sunglasses: voltei baby!")


@client.event
async def on_message(message):
    if message.channel.id == 845377674116726834:
        is_in_message = lambda key: key in message.content
        if is_in_message(sys.argv[1]):
            getalias = message.content.lower().startswith
            id = message.author.display_name

            if getalias(".ping"):
                await message.channel.send("Latência %.4fms" % client.latency)

            if getalias(".stop"):
                print("    Encerrando {} em {}".format(client.user.name, strdate()))
                await message.channel.send(":cry: seu pedido é uma ordem. estou saindo...")
                asyncio.get_event_loop().stop()

            if getalias(".reboot"):
                print("    Reiniciando {} em {}".format(client.user.name, strdate()))
                data.shutdown()
                await message.channel.send(":expressionless: vou esfriar a cabeça, já volto...\n")
                asyncio.get_event_loop().stop()
                reboot()

            if getalias(".status"):
                await message.channel.send("enviando requisição de status para o servidor...\n")
                net.send(0, "status")
                msg = hostedClient.recv()
                await message.channel.send("resposta recebida com id: {}, status: {}\n".format(msg[0], msg[1]))

asyncio.get_event_loop().create_task(client.start(TOKEN[args["bot"]], reconnect=True))
asyncio.get_event_loop().run_forever()
