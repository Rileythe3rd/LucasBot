import discord
import os



client = discord.Client(intents=discord.Intents.all())


# I want my bot to welcome people, private message them and force them to read the rules
@client.event
async def on_ready():
    print('Ready. Logged in as: {0.user}'.format(client))


@client.event
async def on_member_join(member: discord.Member):
    print("Recognised that a member called " + member.name + " joined")
    await member.send('Welcome. Before proceeding any further, you will read the rules.')


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    print(payload)
    if payload.message_id == 892927752179687467:
        print('sensed')
        guild_id = payload.guild_id
        guild = client.get_guild(guild_id)
        role = guild.get_role(892925554326638603)
        member = payload.member
        await member.add_roles(role)




#I understand why we need all the extra infor. The add role function uses it


    # how do i write an if case for the channel being reacted in

    # need to find the guild, the channel, the message, who reacted


client.run(os.environ['TOKEN'])

