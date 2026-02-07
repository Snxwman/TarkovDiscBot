import {
    CommandInteraction,
    LabelBuilder,
    MessageFlags,
    ModalBuilder,
    ModalSubmitInteraction,
    SlashCommandBuilder,
    StringSelectMenuBuilder,
    StringSelectMenuOptionBuilder,
    TextDisplayBuilder,
    TextInputBuilder,
    TextInputStyle,
    type PermissionsString,
} from "discord.js";
import { CommandDeferType, type Command } from "../interfaces/command";
import type { EventData } from "../models/internal";
import { emoji, gameInfo } from "../constants/";

// TODO: Find/build a markdown message builder
// TODO: Support localization
// TODO: Username reservations
//   - Reserve Discord usernames of people already in the server
//   - Reserve usernames used in the previous wipe
// TODO: Commands to test registration failure modes
// TODO: Extract manual formatting to helper functions
// TODO: Add email account verification functionality
// TODO: Make registration flow launchable from a button

// QUESTION: Would this be better implemented as a user command (right click on bot)?
//
// QUESTION: Should there be some method of external TarkoIdle account ownership (eg. email login code)?
// Would enable the following:
//   - Playing the game on the same TarkoIdle account from multiple Discord accounts
//   - Transfering TarkoIdle characters to other Discord accounts
//   - Recovering a TarkoIdle account in the event of Discord account access loss
//   - Having components of the game outside of Discord (eg. complex raid control, better stash management, better UI, etc.)
// Methods:
//   - Password: Standard, lowest security (on user), may require handling lost passwords or resets
//   - Email login code: Requires running an email service (probably best option, but may cost money)
//   - Account code: Irrecoverable on loss, requires nothing from our side after creation, is it regeneratable?
//
// QUESTION: Feature to anonymously request a username from another player? (probably not)

// export class RegisterSlashCommand implements Command {
//     public name = 'register';
//     public deferType = CommandDeferType.HIDDEN;
//     public requireClientPerms: PermissionsString[] = [];
//     public async execute(interaction: CommandInteraction, data: EventData): Promise<void> {
//     }
// }

type RegisterPartialData = {
    username?: string
    faction?: 'BEAR' | 'USEC'
    email?: string
}

// TODO: Add error explanation text (RegistrationClosed, ServerError, UnknownError, UserBanned, UserHasAccount)
// QUESTION: Should email recovery be optional (lean yes)
// ---: Code entry field (eg. invite, special version for boosters, etc.) - make this its own command
function RegisterModal(
    interaction: CommandInteraction,
    data?: RegisterPartialData,
    error?: string
): ModalBuilder {
    const withPartialData = data !== undefined ? true : false;

    const fieldExplanationText = [
        '💡A custom username will obscure your Discord username when shown to other players within the game.\n',
        '⚠️Usernames may **ONLY** contain Latin letters (a-z, A-Z), numbers, underscores, and/or dashes.',
    ].join('\n');

    const errorText = [
        '```ansi',
        '[1;31mAn ERROR occured during registration[0m',
        `[1;31m${error}[0m`,
        '```',
    ].join('\n');

    let infoText = error === undefined ? fieldExplanationText : error + '\n' + fieldExplanationText;

    const infoTextDisplay = new TextDisplayBuilder()
        .setContent(infoText);

    const emailLabel = new LabelBuilder()
        .setLabel('Email')
        .setDescription('Your email is only used to recover or transfer your account.')
        .setTextInputComponent(() => {
            let emailInput = new TextInputBuilder()
                .setCustomId('emailSubmit')
                .setRequired(true)
                .setMinLength(6)
                .setMaxLength(254)
                .setStyle(TextInputStyle.Short);

            emailInput = withPartialData && data?.email !== undefined
                ? emailInput.setValue(data.email)
                : emailInput.setPlaceholder('Enter your email address');
            
            return emailInput;
        })

    const usernameLabel = new LabelBuilder()
        .setLabel('Username')
        .setDescription('Select a custom username or leave blank to use your Discord username.')
        .setTextInputComponent(() => {
            let usernameInput = new TextInputBuilder()
                .setCustomId('usernameSubmit')
                .setRequired(false)
                .setMinLength(4)
                .setMaxLength(16)
                .setStyle(TextInputStyle.Short);

            usernameInput = withPartialData && data?.username !== undefined
                ? usernameInput.setValue(data.username)
                : usernameInput.setPlaceholder(interaction.user.displayName);

            return usernameInput;
        })

    const factionLabel = new LabelBuilder()
        .setLabel('Faction')
        .setDescription('Select your PMC character\'s Faction (no current effect on gameplay).')
        .setStringSelectMenuComponent(
            new StringSelectMenuBuilder()
                .setCustomId('factionSubmit')
                .setPlaceholder('Select a faction')
                .setRequired(true)
                .setMinValues(1)
                .setMaxValues(1)
                .addOptions(
                    new StringSelectMenuOptionBuilder()
                        .setLabel('BEAR')
                        .setValue('BEAR')
                        .setDescription('Battle Encounter Assault Regiment')
                        .setEmoji(emoji.BEAR)
                        .setDefault(withPartialData && data?.faction === 'BEAR' ? true : false),
                    new StringSelectMenuOptionBuilder()
                        .setLabel('USEC')
                        .setValue('USEC')
                        .setDescription('United Security')
                        .setEmoji(emoji.USEC)
                        .setDefault(withPartialData && data?.faction === 'USEC' ? true : false)
                )
        )

    const gameInfoTextDisplay = new TextDisplayBuilder()
        .setContent([
            `-# **Version:** ${gameInfo.botVersion} (bot) | ${gameInfo.gameVersion} (game)`,
            `-# **Wipe Date:** ${gameInfo.lastWipe}`,
        ].join('\n'))


    let modalId = `${interaction.user.id}::${interaction.guildId}::register`;
    modalId = withPartialData ? modalId + '::retry' : modalId;

    return new ModalBuilder()
        .setCustomId(modalId)
        .setTitle('TarkoIdle Account Registration')
        .addTextDisplayComponents(infoTextDisplay)
        .addLabelComponents(emailLabel)  // TODO: Enable when ready
        .addLabelComponents(usernameLabel)
        .addLabelComponents(factionLabel)
        .addTextDisplayComponents(gameInfoTextDisplay)
}

// TODO: Info about how long an email may take
// TODO: Info about what to do if not recieved after X mins
function EmailVerificationModal(email: string) {
    const modal = new ModalBuilder()
        .setCustomId('emailVerificationModal')
        .setTitle('TarkoIdle Email Verification')

    const codeInputLabel = new LabelBuilder()
        .setLabel('Enter the code sent to your email')
        .setDescription(`Sent to: ${email}`)
        .setTextInputComponent(
            new TextInputBuilder()
                .setCustomId('codeSubmit')
                .setPlaceholder('Enter verification code')
                .setRequired(true)
                .setMinLength(8)
                .setMaxLength(8)
                .setStyle(TextInputStyle.Short)
        )

    return modal
        .addLabelComponents(codeInputLabel)
}

export const RegisterCommand = {
    data: new SlashCommandBuilder()
        .setName('register')
        .setDescription('Register a new TarkoIdle account.'),
    // TODO: Username validation (eg. vulgar/banned words and invalid characters)
    // TODO: Return existing or created account to user
    async execute(interaction: CommandInteraction): Promise<void> {

        // TODO: Endpoint needs to be protected (for internal use only)
        // TODO: Check cache first
        const discord_id: string = interaction.user.id;
        const response = await fetch(`https://api.tarkoidle.com/internal/user/dicord/${discord_id}`);

        // TODO: Return existing account to user
        if (response.status === 200) {
            await interaction.reply({
                content: 'You already have a TarkoIdle account',
                flags: MessageFlags.Ephemeral
            });
            return;
        }

        await interaction.showModal(RegisterModal(interaction));
    },
    // TODO: Show email verification modal
    async onSubmit(interaction: ModalSubmitInteraction): Promise<void> {
        // TODO: Check which modal was just submitted by custom id
        // TODO: Process data
        // TODO: On error, follow up with message with button to relaunch modal
        const modalId = interaction.customId;
        interaction.deferReply();

        // let emailSubmission = interaction.fields.getTextInputValue('emailSubmit');  // TODO: Enable when ready
        let usernameSubmission = interaction.fields.getTextInputValue('usernameSubmit');
        let factionSubmission = interaction.fields.getStringSelectValues('factionSubmit')[0] ?? '';
        let discordData = {};
        
        // Should be unreachable (here as a type guard)
        if (factionSubmission !== 'BEAR' && factionSubmission !== 'USEC') {
            await interaction.followUp({
                content: [
                    '```ansi',
                    '[1;31mAn irrecoverable error occured (invalid value for faction recieved).[0m',
                    '[1;31mTry registering again from the beginning.[0m',
                    '```',
                ].join('\n'),
                flags: MessageFlags.Ephemeral,
            });
            // TODO: Have the bot notify devs
            return;
        }

        // TODO: Extract user data scraping to an external function
        const response = await fetch('https://api.tarkoidle.com/register', {
            method: 'POST',
            body: JSON.stringify({
                username: usernameSubmission,
                faction: factionSubmission,
                // email: '',  // TODO: Enable when ready
                dicord: {
                    id: '',
                    global_username: '',
                    global_avatar: '',
                    global_banner: '',
                    server_username: '',
                    server_avatar: '',
                    created_timestamp: '',
                    dm_channel: '',
                    hex_accent_color: '',
                    guild_tag_badge_url: '',
                },
                metadata: {},
            })
        });

        let error: string | null = null;

        switch (response.status) {
            case 201:  // Created: New account successfuly created
                break;
            case 400:  // Bad Request: Validation error in registration data (usually username checks failed)
                error = '';
                break;
            case 403:  // Forbidden: User is moderated (banned, timedout, etc.)
                error = '';
                break;
            case 409:  // Conflict: An account is already associated with this Discord id
                error = '';
                break;
            case 500:  // Internal Server Error: Server failed
                error = '';
                break;
            case 503:  // Service Unavailable: Registration is closed
                error = '';
                break;
            default:   // Unknown error (anything else)
                error = '';
                break;
        }

        if (error !== null) {
            const errorText = [
                '```ansi',
                '[1;31mAn ERROR occured during registration[0m',
                `[1;31m${error}[0m`,
                '```',
            ].join('\n');

            // TODO: Add text prompting button click to retry register modal
            // TODO: Add button to restart modal
            await interaction.followUp({
                content: errorText,
                flags: MessageFlags.Ephemeral,
            });
        }
    }
}
