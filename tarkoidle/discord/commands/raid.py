import asyncio
from random import randint

import arc
from arc import GatewayClient as ArcGatewayClient
from arc import GatewayContext as ArcGatewayContext
from arc import GatewayPlugin as ArcGatewayPlugin

from tarkoidle.discord.bot import TarkoIdleBot
from tarkoidle.utils.emoji import SPINNER

plugin = ArcGatewayPlugin('raid')
arc_client = TarkoIdleBot.arc_client

maps: dict[str, int] = {
    'Ground Zero': 60,
    'Streets of Tarkov': 50,
    'Interchange': 35,
    'Customs': 40,
    'Factory': 25,
    'The Lab': 15,
    'Woods': 38,
    'Shoreline': 32,
    'Lighthouse': 18,
}

map_names: list[str] = list(maps.keys())


@plugin.include
@arc.slash_command('raid', 'Queue into a raid.')
async def raid(
    ctx: ArcGatewayContext,
    raid_map: arc.Option[str, arc.StrParams('Select a map', choices=map_names)],
) -> None:
    _ = await ctx.respond(f'{ctx.user.display_name} is raiding on {raid_map}')

    raid_time = randint(3, 9)  # noqa: S311
    raid_msg = await ctx.respond(f'{SPINNER} Raid ends in {raid_time} seconds')
    while raid_time > 0:
        await asyncio.sleep(1)
        raid_time -= 1
        raid_msg = await raid_msg.edit(f'{SPINNER} Raid ends in {raid_time} seconds')

    surv = randint(0, 100)  # noqa: S311
    if surv > maps[raid_map]:
        _ = await raid_msg.edit(f'{ctx.user.display_name} died on {raid_map}')
        await asyncio.sleep(2)
        _ = await ctx.respond('dumbass...')
    else:
        _ = await raid_msg.edit(f'{ctx.user.display_name} survived the raid on {raid_map}')


@arc.loader
def load(client: ArcGatewayClient) -> None:
    _ = client.add_plugin(plugin)
