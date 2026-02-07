// Source: https://github.com/KevinNovak/Discord-Bot-TypeScript-Template/blob/b2ef8effaa4ed5b1a0ed57adaf5ec7ab1483fc89/src/constants/discord-limits.ts

export class DiscordLimits {
    public static readonly ACTIVE_THREADS_PER_GUILD = 1000;
    public static readonly CHANNELS_PER_GUILD = 500;
    public static readonly CHOICES_PER_AUTOCOMPLETE = 25;
    public static readonly EMBEDS_PER_MESSAGE = 10;
    public static readonly EMBED_COMBINED_LENGTH = 6000;
    public static readonly EMBED_DESCRIPTION_LENGTH = 4096;
    public static readonly EMBED_FIELD_NAME_LENGTH = 256;
    public static readonly EMBED_FOOTER_LENGTH = 2048;
    public static readonly EMBED_TITLE_LENGTH = 256;
    public static readonly FIELDS_PER_EMBED = 25;
    public static readonly GUILDS_PER_SHARD = 2500;
    public static readonly PINS_PER_CHANNEL = 250;
    public static readonly ROLES_PER_GUILD = 250;
    public static readonly COMPONENTS_PER_MODAL = 5
}
