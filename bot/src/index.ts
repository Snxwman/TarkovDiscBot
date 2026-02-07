// Require the necessary discord.js classes
import fs from 'node:fs'
import path from 'node:path'
import { Client, Collection, Events, GatewayIntentBits, InteractionType, MessageFlags, type InteractionReplyOptions} from 'discord.js';
// import type { Command } from './interfaces/command';
import { slashCommands } from './commands/index.ts';

declare module "bun" {
    interface Env {
        TOKEN: string;
        CLIENT_ID: string;
        GUILD_ID: string;
    }
}

// declare module "discord.js" {
//     interface Client<Ready extends boolean = boolean> extends BaseClient {
//         commands: Collection<string, Command>;
//     }
// }

// Bot starup
const BOT_NAME = 'TarkoIdle Bot';
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
client.once(Events.ClientReady, (readyClient) => {
    console.log(`[${BOT_NAME}] - READY - Logged in as ${readyClient.user.tag}`);
});

// Command handler
client.commands = new Collection();

for (const command of slashCommands) {
    if ('data' in command && 'execute' in command) {
        client.commands.set(command.data.name, command);
        console.log(`Found command: /${command.data.name}`);
    } else {
        console.error(`[WARNING] The command at ${command} is missing a required 'data' or 'execute' property.`);
    }
}

client.on(Events.InteractionCreate, async (interaction) => {
    const command = interaction.client.commands.get(interaction.commandName);
    if (!command) {
        console.error(`No command matching ${interaction.commandName} was found.`);
        return;
    }

    switch (interaction.type) {
        case InteractionType.ModalSubmit:
            command.onSubmit(interaction);
            return;

        case InteractionType.ApplicationCommand:
            try {
                await command.execute(interaction);
            } catch (error) {
                console.error(error);

                const errorMessage: InteractionReplyOptions = {
                    content: 'There was an error while executing this command!',
                    flags: MessageFlags.Ephemeral,
                }

                if (interaction.replied || interaction.deferred) {
                    await interaction.followUp(errorMessage);
                } else {
                    await interaction.reply(errorMessage);
                }
            }
            return;

        default:
            return;
    }
});

// Log in to Discord with your client's token
client.login(process.env.TOKEN);
