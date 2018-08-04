import discord
import datetime
import pytz
from discord.ext.commands import Bot
from wowapi import WowApi as wow

BOT_PREFIX = "!"
TOKEN = ""

client = Bot(command_prefix=BOT_PREFIX)


@client.command(description="Looks up a World of Warcraft character",
                brief="neerrrrdddssss.",
                aliases=['wow', 'c', 'armory'],
                pass_context=False)
async def char(char_name: str, char_realm: str):
    char_profile = wow.get_character_profile('us', char_realm, char_name, fields='guild')
    char_url = "https://worldofwarcraft.com/en-us/character/" + char_realm.lower() + "/" + char_name.lower()

    char_avatar = "http://render-us.worldofwarcraft.com/character/" + char_profile['thumbnail']
    char_main = char_avatar.replace('avatar', 'main')
    char_inset = char_avatar.replace('avatar', 'inset')

    embed = discord.Embed(title="<" + char_profile['guild']['name'] + ">, " + char_realm.capitalize(),
                          colour=discord.Colour(0x457b86),
                          url=char_url,
                          description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque blandit est est, id tincidunt ipsum porttitor nec. Pellentesque laoreet ligula ut lorem tempus, quis sagittis mauris sollicitudin.",
                          timestamp=datetime.datetime.now(pytz.timezone('US/Pacific')))

    embed.set_image(url=char_main)
    embed.set_thumbnail(url=char_inset)
    embed.set_author(name=char_name.capitalize() + " (" + str(char_profile['level']) + ")", url=char_url,
                     icon_url=char_avatar)
    embed.set_footer(text="butts", icon_url="https://i.imgur.com/JhcBs0o.png")

    embed.add_field(name="<:alliance:472975393872150542>", value="ding", inline=True)
    embed.add_field(name="<:horde:472975380299644959>", value="dong", inline=True)

    await client.say(embed=embed)


client.run(TOKEN)
