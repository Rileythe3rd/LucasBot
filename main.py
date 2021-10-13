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
    if payload.message_id == 892927752179687467:
        print('sensed')
        guild_id = payload.guild_id
        guild = client.get_guild(guild_id)
        role = guild.get_role(892925554326638603)
        member = payload.member
        await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.message_id == 892927752179687467:
        print('reaction removed')
        guild_id = payload.guild_id
        guild = client.get_guild(guild_id)
        role = guild.get_role(892925554326638603)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.remove_roles(role)

        #The reason member is more complicated here is because await needs this extra info to remove roles


client.run(os.environ['TOKEN'])

