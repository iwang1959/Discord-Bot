import os
import discord #import discord package
import emoji
import json
import requests
from discord.ext import commands

from keep_alive import keep_alive
my_secret = os.environ['TOKEN']

client = discord.Client()
#Client object, connection to discord

bot = commands.Bot(command_prefix='!')



def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "  - " + json_data[0]['a']
  return(quote)

@bot.command()
async def info(ctx):
  await ctx.send("Server: " + str(ctx.guild))
  await ctx.send("User: " + str(ctx.author))
  #await ctx.send(ctx.message.id)


@bot.command()
async def punch(ctx, arg):
  await ctx.send(f'Punched {arg}')


@bot.command()
async def double_punch(ctx, arg1, arg2):
  await ctx.send(f'Punched {arg1} and {arg2}')



@client.event
async def on_ready():#function in discord package, triggered when bot goes online
  print("Bot is online")


@client.event
async def on_message(message):#the parameter message stores content of the message, author, channel

  if message.author == client.user:#Checks if bot is respnding to itself
    return

  #if message.content.lower() == "morning":
   # await message.channel.send("Good Morning " + str(message.author))

  if ("morning" or "gm")in message.content.lower():
    await message.channel.send("Good Morning " + str(message.author))

  if "night" in message.content.lower():
    await message.channel.send("Good night " + str(message.author))

  if "hello" in message.content.lower():
    await message.channel.send("Hello! " + str(message.author))

  


  if message.content.startswith("$quote") or message.content.startswith("$Quote"):
    quote = getQuote()
    await message.channel.send(quote)


#Popular Discord Emojis
  if message.content == "cool":
    await message.add_reaction(emoji.emojize(':thumbs_up:'))
  elif message.content == "nice":
    await message.add_reaction(emoji.emojize(':thumbs_up:'))

  if message.content == "see":
    await message.add_reaction(emoji.emojize(':eyes:'))
  elif message.content == "eyes":
    await message.add_reaction(emoji.emojize(':eyes:'))
  elif message.content == "sight":
    await message.add_reaction(emoji.emojize(':eyes:'))

  if "lol" in message.content.lower():
    await message.add_reaction(emoji.emojize(':grinning_squinting_face:'))
  elif "xd" in message.content.lower():
    await message.add_reaction(emoji.emojize(':grinning_squinting_face:'))
  elif "laughing" in message.content.lower():
    await message.add_reaction(emoji.emojize(':grinning_squinting_face:'))


  if "100" in message.content.lower():
    await message.add_reaction(emoji.emojize(':hundred_points:'))
  elif "Keep It 100" in message.content.lower():
    await message.add_reaction(emoji.emojize(':hundred_points:'))
  elif "perfect score" in message.content.lower():
    await message.add_reaction(emoji.emojize(':hundred_points:'))


  if "watermelon" in message.content.lower():
    await message.add_reaction(emoji.emojize(':watermelon:'))
  elif "melon" in message.content.lower():
    await message.add_reaction(emoji.emojize(':watermelon:'))


  if "cutlery" in message.content.lower():
    await message.add_reaction(emoji.emojize(':fork_and_knife:'))
  elif "sliverware" in message.content.lower():
    await message.add_reaction(emoji.emojize(':fork_and_knife:'))
  elif "fork" in message.content.lower():
    await message.add_reaction(emoji.emojize(':fork_and_knife:'))
  elif "knife" in message.content.lower():
    await message.add_reaction(emoji.emojize(':fork_and_knife:'))


  if "yum" in message.content.lower():
    await message.add_reaction(emoji.emojize(':face_savoring_food:'))
  elif "goofy" in message.content.lower():
    await message.add_reaction(emoji.emojize(':face_savoring_food:'))
  elif "hungry" in message.content.lower():
    await message.add_reaction(emoji.emojize(':face_savoring_food:'))
  elif "delicious" in message.content.lower():
    await message.add_reaction(emoji.emojize(':face_savoring_food:'))


  if "wailing" in message.content.lower():
    await message.add_reaction(emoji.emojize(':weary_face:'))
  elif "weary" in message.content.lower():
    await message.add_reaction(emoji.emojize(':weary_face:'))
  elif "distraught" in message.content.lower():
    await message.add_reaction(emoji.emojize(':weary_face:'))


  if "exhausted" in message.content.lower():
    await message.add_reaction(emoji.emojize(':tired_face:'))
  elif "annoy" in message.content.lower():
    await message.add_reaction(emoji.emojize(':tired_face:'))
  elif "sleepy" in message.content.lower():
    await message.add_reaction(emoji.emojize(':tired_face:'))
  elif "tired" in message.content.lower():
    await message.add_reaction(emoji.emojize(':tired_face:'))


  if "poop" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))
  elif "stink" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))
  elif "hankey" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))
  elif "smile" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))
  elif "dog dirt" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))
  elif "choco" in message.content.lower():
    await message.add_reaction(emoji.emojize(':pile_of_poo:'))



@client.event
async def on_reaction_add(reaction, user):
  await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')



@client.event
async def on_message_edit(before, after):
  await before.channel.send(
    f'{before.author} edited a message.\n'
    f'Before: {before.content}\n'
    f'After: {after.content}\n'
    f'Sorry no editing messsages on this server'
  )




keep_alive()
client.run(my_secret)
#bot.run(my_secret)




