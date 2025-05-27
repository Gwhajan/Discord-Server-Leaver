import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"\n✓ Logged in as {bot.user} ({bot.user.id})")
    await leave_non_admin_servers()

async def leave_non_admin_servers():
    left = 0
    total = 0

    for guild in bot.guilds:
        total += 1
        member = guild.get_member(bot.user.id)

        if member is None:
            print(f" Could not get member info in '{guild.name}'. Skipping...")
            continue

        if member.guild_permissions.administrator:
            print(f" Staying in '{guild.name}' (Admin permissions).")
            continue

        try:
            await guild.leave()
            print(f" Left '{guild.name}' (No Admin).")
            left += 1
        except Exception as e:
            print(f":x: Failed to leave '{guild.name}': {e}")

    print(f"\n✓  Finished: Left {left} of {total} servers.")
    await bot.close()
    
bot.run("Token", bot=False)


