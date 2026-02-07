import type {
    ApplicationCommandOptionChoiceData,
    AutocompleteFocusedOption,
    AutocompleteInteraction,
    CommandInteraction,
    PermissionsString
} from "discord.js";
import type { EventData } from "../models/internal";

export interface Command {
    name: string;
    cooldown?: number;  // TODO: needs better type
    deferType: CommandDeferType;
    requireClientPerms: PermissionsString[];
    autocomplete?(
        interation: AutocompleteInteraction,
        option: AutocompleteFocusedOption
    ): Promise<ApplicationCommandOptionChoiceData[]>;
    execute(interaction: CommandInteraction, data?: EventData): Promise<void>;
}

export enum CommandDeferType {
    PUBLIC = 'PUBLIC',
    HIDDEN = 'HIDDEN',
    NONE = 'NONE',
}
