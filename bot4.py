#C:\Users\vdocv\OneDrive\_GKG090717\GKG WORK STUFF\Coding_032420\Python Training\discordbot\

import discord
from discord.ext import commands
import json
import random

#class MyClient(discord.Client):
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    #print(self.user.name)
    #print(self.user.id)
    print('------')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='.help'))
    print('Bot is ready to go!')

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
        
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='.help'))
    print('Bot is ready to go!')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = "."

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"This bots prefix has been set to {prefix}")

client.remove_command('help')


#.help
@client.command()
async def help (ctx):
    await ctx.send('Use these to help: \n`prefix (new prefix)` , `hello bot` , `ball (question)`\n`purge (number)` , `invite` , `tank (@user)`\n`kick (@user)` , `ban (@user)` , `issues`')

#.invite
@client.command()
async def invite (ctx):
    await ctx.send('Invite me with this link: https://discord.com/api/oauth2/authorize?client_id=738169795849224273&permissions=8&scope=bot')

#.issues
@client.command()
async def issues (ctx):
    await ctx.send('Join this discord to state issues: https://discord.gg/aFEK5UG')

#.hello
@client.command()
async def hello (ctx, *, question):
    responses = ['Hello there','Hello, how are you', 'Hey hey']
    await ctx.send(f'{random.choice(responses)} {ctx.message.author.mention} ')

#.ball
@client.command()
async def ball (ctx, *, question):
    responses = ['As I see it, yes.','Ask again later.',
 'Better not tell you now.',
 'Cannot predict now.',
 'Concentrate and ask again.',
 'Don’t count on it.',
 'It is certain.',
 'It is decidedly so.',
 'Most likely.',
 'My reply is no.',
 'My sources say no.',
 'Outlook not so good.',
 'Outlook good.',
 'Reply hazy, try again.',
 'Signs point to yes.',
 'Very doubtful.',
 'Without a doubt.',
 'Yes.',
 'Yes – definitely.',
 'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)} ')

#.purge
@client.command()
async def purge(ctx, *, number:int=None):
    if ctx.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send('You must enter a number')
            else:
                deleted = await ctx.message.channel.purge(limit=number+1)
                await ctx.send(f'Messages purged by {ctx.message.author.mention}: {number} ')
        except:
            await ctx.send("I can't purge messages here :(")
    else:
        await ctx.send('You do not have permissions to use this command.')

#.kick
@client.command()
async def kick(ctx, user: discord.Member, * , reason=None):
    if user.guild_permissions.manage_messages:
        await ctx.send('I cant kick this user because they are an admin/mod.')
    elif ctx.author.guild_permissions.kick_members:
        if reason is None:
            await ctx.guild.kick(user=user, reason='None')
            await ctx.send(f'{user} has been kicked by {ctx.message.author.mention}')
        else:
            await ctx.guild.kick(user=user, reason=reason)
            await ctx.send(f'{user} has been kicked by {ctx.message.author.mention}')
    else:
        await ctx.send('You do not have permissions to use this command.')

#.ban
@client.command()
async def ban(ctx, user: discord.Member, * , reason=None):
    if user.guild_permissions.manage_messages:
        await ctx.send('I cant ban this user because they are an admin/mod.')
    elif ctx.author.guild_permissions.ban_members:
        if reason is None:
            await ctx.guild.ban(user=user, reason='None')
            await ctx.send(f'{user} has been banned by {ctx.message.author.mention}')
        else:
            await ctx.guild.ban(user=user, reason=reason)
            await ctx.send(f'{user} has been banned by {ctx.message.author.mention}')
    else:
        await ctx.send('You do not have permissions to use this command.')

#.tank
@client.command()
async def tank (ctx, *, question):
    responses = ['has been destroyed!' , 'has been tanked!']
    await ctx.send(f'Bam {question}, {random.choice(responses)} ')

#on join
@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
        await guild.system_channel.send(to_send)

#on leave
@client.event
async def on_member_remove(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Goodbye {0.mention} we hoped you enjoyed your stay :('.format(member, guild)
        await guild.system_channel.send(to_send)

client.run('NzM4MTQzMjY5NTk4MjY1NDU2.XyHnfQ.UVYvHcrdWsoTcBjJlkOoWg2a62c')
