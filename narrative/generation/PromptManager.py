from narrative.generation.narrative_structuring import NarrativeStructuring
from narrative.lore.lore import Lore

class PromptManager:
    """
    Manages the creation, formatting, and adaptation of prompts sent to the LLMs for narrative generation.
    Utilizes lore information to ensure that prompts are consistent with the game world and characters.
    """

    def __init__(self, narrative_structuring: NarrativeStructuring, context_manager):
        """
        Initializes the PromptManager with dependencies on narrative structuring, context management, and lore.

        Args:
            narrative_structuring (NarrativeStructuring): Handles the structure of the narrative.
            context_manager (ContextManager): Tracks narrative context to inform prompt construction.
        """
        self.narrative_structuring = narrative_structuring
        self.context_manager = context_manager
        self.lore = Lore()  # Initialize Lore to access world and character information
        self.prompt_templates = self._load_templates()

    def _load_templates(self):
        """
        Loads and stores various prompt templates for different scenarios.

        Returns:
            dict: A dictionary of prompt templates keyed by scenario type.
        """
        # Example templates - these would be more detailed in practice
        return {
            "dialogue": "Character {character_name} says: {dialogue}",
            "action": "In the {location}, {character_name} {action_description}",
            "description": "The {location} is {location_description}. {character_name} observes {object_description}."
        }

    def create_prompt(self, scenario, character, current_state):
        """
        Creates a prompt based on the scenario, character, and current state of the narrative.

        Args:
            scenario (str): The type of scenario (e.g., "dialogue", "action").
            character (Character): The character involved in the scenario.
            current_state (dict): The current state of the narrative, including location, recent actions, etc.

        Returns:
            str: The formatted prompt ready to be sent to the LLM.
        """
        template = self.prompt_templates.get(scenario)
        if not template:
            raise ValueError(f"Unknown scenario: {scenario}")

        # Retrieve relevant lore information
        character_backstory = self.lore.get_character_backstory(character.name)
        world_rules = self.lore.get_world_rules()
        location_description = current_state.get("world_state", {}).get("location_description", "")

        # Use the template to create a prompt, incorporating lore information
        prompt = template.format(
            character_name=character.name,
            dialogue=current_state.get('dialogue', ''),
            location=current_state.get('location', ''),
            action_description=current_state.get('action_description', ''),
            location_description=location_description,
            object_description=current_state.get('object_description', '')
        )

        # Integrate character backstory and world rules into the prompt for more context
        prompt += f" {character.name}'s background: {character_backstory['backstory']}. "
        prompt += f"World rules to consider: {', '.join(world_rules.values())}."

        return prompt

    def adapt_prompt(self, base_prompt, tone=None, urgency=None):
        """
        Adapts a prompt by altering its tone or adding urgency based on the narrative needs.

        Args:
            base_prompt (str): The base prompt to adapt.
            tone (str, optional): The desired tone (e.g., "serious", "lighthearted").
            urgency (str, optional): The urgency level (e.g., "urgent", "casual").

        Returns:
            str: The adapted prompt.
        """
        if tone:
            base_prompt += f" [Tone: {tone}]"
        if urgency:
            base_prompt += f" [Urgency: {urgency}]"
        return base_prompt

    def add_custom_template(self, scenario_name, template_string):
        """
        Adds a custom prompt template for a specific scenario.

        Args:
            scenario_name (str): The name of the scenario.
            template_string (str): The template string to use for the scenario.
        """
        self.prompt_templates[scenario_name] = template_string

    def remove_template(self, scenario_name):
        """
        Removes an existing prompt template.

        Args:
            scenario_name (str): The name of the scenario to remove the template for.
        """
        if scenario_name in self.prompt_templates:
            del self.prompt_templates[scenario_name]
        else:
            raise KeyError(f"No such template: {scenario_name}")
