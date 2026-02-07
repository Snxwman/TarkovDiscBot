import type { CommandInteraction, ModalSubmitInteraction } from "discord.js";
import type { EventData } from "../models/internal";

export interface ModalFlow {
    name: string;
    cooldown?: number;
    execute(interaction: CommandInteraction, data?: EventData): Promise<void>;
    onSubmit(interaction: ModalSubmitInteraction, data?: EventData): Promise<void>;
}
