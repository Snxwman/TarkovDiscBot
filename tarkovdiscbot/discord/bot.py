from __future__ import annotations

import os

from arc import GatewayClient as ArcGatewayClient
from dotenv import load_dotenv
from hikari import GatewayBot as HikariGatewayBot
from hikari import GuildJoinEvent, GuildLeaveEvent, Intents
from miru import Client as MiruClient


class TarkoIdleBot:
    hikari_client: HikariGatewayBot
    arc_client: ArcGatewayClient
    miru_client: MiruClient
    # config: BotConfig

    def __init__(self):
        if not load_dotenv(dotenv_path='.token'):
            err_msg = 'Failed to load env file'
            raise ValueError(err_msg)

        if (APP_TOKEN := os.getenv('APP_TOKEN')) is None:
            err_msg = 'Could not read APP_TOKEN'
            raise ValueError(err_msg)

        TarkoIdleBot.hikari_client = HikariGatewayBot(token=APP_TOKEN, intents=Intents.ALL)

        TarkoIdleBot.arc_client = ArcGatewayClient(TarkoIdleBot.hikari_client)
        TarkoIdleBot.miru_client = MiruClient.from_arc(TarkoIdleBot.arc_client)

        TarkoIdleBot.arc_client.load_extensions_from('tarkovdiscbot/discord/commands')

        @TarkoIdleBot.hikari_client.listen()
        async def _(event: GuildJoinEvent):
            print(f'Bot joined guild: {event.guild_id}')

        @TarkoIdleBot.hikari_client.listen()
        async def _(event: GuildLeaveEvent):
            print(f'Bot left guild: {event.guild_id}')

    @staticmethod
    def run():
        TarkoIdleBot.hikari_client.run()

