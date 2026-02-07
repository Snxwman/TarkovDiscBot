import { REST, Routes } from 'discord.js';
import fs from 'node:fs';
import path from 'node:path';
import { slashCommands } from './commands'

const commands = [];

for (const command of slashCommands) {
    if ('data' in command && 'execute' in command) {
        commands.push(command.data.toJSON());
        console.log(`[REGISTRATION] Found command: /${command.data.name}`);
    } else {
        console.log(`[WARNING] The command ${command} is missing a required "data" or "execute" property.`);
    }
}

// Construct and prepare an instance of the REST module
const rest = new REST().setToken(process.env.TOKEN);

// Deploy commands
(async () => {
    try {
        console.log(`Started refreshing ${commands.length} application (/) commands.`);

        // The put method is used to fully refresh all commands in the guild with the current set
        const data = await rest.put(
            Routes.applicationGuildCommands(process.env.CLIENT_ID, process.env.GUILD_ID),
            { body: commands }
        );

        console.log(`Successfully reloaded ${data.length} application (/) commands.`);
    } catch (error) {
        // And of course, make sure you catch and log any errors!
        console.error(error);
    }
})();
