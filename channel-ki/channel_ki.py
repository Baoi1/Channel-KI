import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and after.channel.id == 1225597984234930306:
        guild = member.guild
        # Erstellen eines neuen Voice-Channels für den Benutzer mit dem Namen des Benutzers
        channel_name = f"{member.display_name}'s Channel"
        channel = await guild.create_voice_channel(channel_name)
        # Benutzer in den neu erstellten Kanal bewegen
        await member.move_to(channel)

# Ersetzen Sie YOUR_VOICE_CHANNEL_ID durch die ID des Voice-Channels, in den Benutzer eintreten müssen

bot.run('MTIyNTUzNDM1NTM3MjM4MDMyMg.Guy4Yx.4zx-1HF4w4m2AssUZakonY_I7vbMSJFHEygfJ0')
