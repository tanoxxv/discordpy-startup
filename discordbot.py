from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_message(message):
    try:
        if message.aauthor.bot:
            return
        await bot.process_commands(message)
       except Exception:
        await message.channe1.send(f'```\n{traceback.format_exc()}\n```')

@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
