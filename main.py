import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import math
import time

finalper = False
tab = ["Kacper","Marcin","Łukasz"]

intents = discord.Intents().all()
client = commands.Bot(command_prefix='?', intents=intents)
print("bot włączony")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="ILoveArkadiuszOrłowski"))

@client.command(pass_context=True)
async def change_nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nick został zmieniony na {member.mention} ')

@client.command()
async def wstawaj(ctx):
  await ctx.send("Wstałem")

@client.command()
async def set_bot_status(ctx, status):
    await client.change_presence(activity=discord.Game(name=status))

@client.command()
async def losowa_liczba(ctx):
    await ctx.send(random.randint(0,99))

@client.command()
#@has_permissions(administrator=True)
async def gayrate(ctx, text):
  per = str(random.randint(0,100))+"%"
  embed = discord.Embed(title="Sprawdzamy:",description=text)
  embed.add_field(name="Jest gejem w:",value=per, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def ship(ctx, ship1, ship2):
  love = str(random.randint(0,100))+"%"
  embed=discord.Embed(title="Ship:", description= ship1 + " ❤️ " + ship2, color=0xff00ff)
  embed.add_field(name="Poziom miłości:", value=love, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def tab_add(ctx, text):
  tab.append(text)
  await ctx.send("Dodano")

@client.command()
async def tab_check(ctx):
 try:
  for i in tab:
    time.sleep(1)
    await ctx.send(i)
 except:
   await ctx.send("Nie ma nic na liście")

@client.command()
async def tab_clear(ctx):
    tab.clear()
    await ctx.send("Wyczyszczono")
  ##per = str(random.randint(0,100))+"%"
#embed=discord.Embed(title="Sprawdzamy:", description="@Fairshooter#2137")
# embed.add_field(name="Jest gejem w:", value="93%", inline=False)
 #await ctx.send(embed=embed)

  

@client.command()
async def pomoc(ctx):
  embed=discord.Embed(title="Komendy",  
  description="Komendy do bota Fair", 
  color=0x7b00ff)
  embed.add_field(name="?losowa_liczba", value="losuje liczbę", 
  inline=False)
  embed.add_field(name="?siema", value="witasz się z botem", inline=False)
  embed.add_field(name="?test",value="test",inline=False)
  embed.add_field(name="?gayrate <osoba>", value="sprawdza poziom geja", inline=False)
  embed.set_footer(text="okienko można wywołać za pomocą komendy ?pomoc")
  await ctx.send(embed=embed)

@client.command()
async def siema(ctx):
    siema = ["Dzieńdobry","Yo","Hej","Siema","Cześć","Witam"]
    await ctx.send(random.choice(siema))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Zabrakło argumentu :rolling_eyes:.')
    #if isinstance(error, commands.MissingPermissions):
        #await ctx.send("You dont have all the requirements :angry:")

#bans a user with a reason

async def ban(ctx, member : discord.Member, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)   
      
#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run("MTAyNDY5NjQxMzg0NzgyMjM0Ng.GrzBNZ.bfQtB4r7qrdyeM5meVaNiILp5em0ru0g6jkaDo")