import hikari
import arc
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.token')
APP_TOKEN = os.getenv('APP_TOKEN')

bot = hikari.GatewayBot(token=APP_TOKEN)
client = arc.GatewayClient(bot)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    """If a non-bot user mentions your bot, respond with 'I love cookie!'."""

    # Do not respond to bots nor webhooks pinging us, only user accounts
    if not event.is_human:
        return

    me = bot.get_me()

    if me.id in event.message.user_mentions_ids:
        await event.message.respond("I love cookie!")

@client.include
@arc.slash_command("hi", "Say hi to someone!")
async def hi_slash(
    ctx: arc.GatewayClient,
    user: arc.Option[hikari.User, arc.UserParams("The user to say hi to")]
) -> None:
    await ctx.respond(f"Hey {user.mention}!")