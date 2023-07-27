import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="recent donations"))

@bot.event
async def on_message(message):
    if message.author.bot:  # Ignore messages from bots to avoid potential loops
        return

    # Replace 'YOUR_CHANNEL_ID' with the ID of the desired channel
    desired_channel_id = YOUR_CHANNEL_ID
    if message.channel.id != desired_channel_id:
        return

    text = message.content.strip().lower()  # Get the message content in lowercase

    # Replace 'YOUR_SERVER_ID' and 'YOUR_ROLE_ID' with your actual values
    server = bot.get_guild(YOUR_SERVER_ID)
    role_to_give = discord.utils.get(server.roles, id=YOUR_ROLE_ID)

    if text in [member.name.lower() for member in server.members]:
        member = discord.utils.get(server.members, name=text)
        if member is not None:
            try:
                await member.add_roles(role_to_give)
                print(f'Gave role to {member.name} for being mentioned.')
                # Add the checkmark emoji ✅
                await message.add_reaction('✅')
            except discord.Forbidden:
                print(f"Failed to give role to {member.name}. Missing Permissions.")
                # Add the X emoji ❌
                await message.add_reaction('❌')
            except discord.HTTPException:
                print(f"Failed to give role to {member.name}. HTTP Exception.")
                # Add the X emoji ❌
                await message.add_reaction('❌')

    await bot.process_commands(message)  # Process other commands if any

# Replace 'YOUR_SERVER_ID' with the actual ID of your server
YOUR_SERVER_ID = 112998032189

# Replace 'YOUR_ROLE_ID' with the actual ID of the role you want to give
YOUR_ROLE_ID = 11299945306

# Replace 'YOUR_CHANNEL_ID' with the actual ID of the channel you want the bot to listen to
YOUR_CHANNEL_ID = 11300305620

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
