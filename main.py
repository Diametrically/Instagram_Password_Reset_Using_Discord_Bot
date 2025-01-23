import discord
import uuid
import random
import requests
import json
from discord.ext import commands

# Your Discord bot token
DISCORD_TOKEN = '         ' # Enter your Discord Bot Token

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all(), case_insensitive=True, self_bot=True)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')



@bot.command()
async def reset(ctx, user):
    guid = str(uuid.uuid4())
    url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
    header = {
        "user-agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; 'huawei/google; Nexus 6P; angler; angler; en_US)",
        "Content-Type": "application/x-www-form-urlencoded"}


    # For send Password Reset Using Mail
    if"@" in user:
        payload1 = {f"_csrftoken=QsH54d5BufeHPDczQuauI3Qt7G0M8ixs&user_email={user}&guid={guid}&device_id={guid}"}
        response = requests.post(url, verify=False, headers=header, data=payload1).text
        print(response)

        if "obfuscated_email" in response:
            response_info = (f"{response}")
            embed = discord.Embed(
                colour=discord.Colour.dark_green(),
                title="Sent Password Reset To"
            )
            embed.set_author(name=f'{user}')
            embed.add_field(name="", value=response_info)
            await ctx.reply(embed=embed)
        elif "Sorry, we can't send you a link to reset your password" in response:
            error = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="Sorry, there was a problem. Please contact Instagram.")
            error.set_author(name=f'{user}')
            await ctx.reply(embed=error)
        elif "The link you followed may be broken, or the page may have been removed." in response:
            error1 = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="User Not Found.")
            error1.set_author(name=f'{user}')
            await ctx.reply(embed=error1)

        else:
            error2 = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="Rate_Limit. Please try after sometime")
            error2.set_author(name=f'{user}')
            await ctx.reply(embed=error2)
    else:
        payload = f"_csrftoken=QsH54d5BufeHPDczQuauI3Qt7G0M8ixs&username={user}&guid={guid}&device_id={guid}"
        response = requests.post(url, verify=False, headers=header, data=payload).text
        print(response)

        if "obfuscated_email" in response:
            response_info = (f"{response}")
            embed = discord.Embed(
                colour=discord.Colour.dark_green(),
                title="Sent Password Reset To"
            )
            embed.set_author(name=f'@{user}')
            embed.add_field(name="", value=response_info)
            await ctx.reply(embed=embed)
        elif "Sorry, we can't send you a link to reset your password" in response:
            error = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="Sorry, there was a problem. Please contact Instagram.")
            error.set_author(name=f'@{user}')
            await ctx.reply(embed=error)
        elif "The link you followed may be broken, or the page may have been removed." in response:
            error1 = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="User Not Found.")
            error1.set_author(name=f'@{user}')
            await ctx.reply(embed=error1)

        else:
            error2 = discord.Embed(
                colour=discord.Colour.dark_red(),
                title="Rate_Limit. Please try after some time")
            error2.set_author(name=f'@{user}')
            await ctx.reply(embed=error2)





bot.run(DISCORD_TOKEN)