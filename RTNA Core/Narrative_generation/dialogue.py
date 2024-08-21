# core/narrative_generation/dialogue.py

from core.llm_integration import LLMIntegration

class DialogueManager:
    """
    Manages and generates dialogue for the game using an LLM specifically for dialogue.
    """

    def __init__(self, provider="huggingface", model_name="microsoft/DialoGPT-medium", api_key=None):
        """Initializes the DialogueManager with an LLM for dialogue generation."""
        self.llm = LLMIntegration(provider=provider, model_name=model_name, api_key=api_key)

    def generate_dialogue(self, event: dict, player: Character, location: Location) -> str:
        """
        Generates dialogue using the LLM based on the event and context.

        Args:
            event: The current event dictionary.
            player: The player character object.
            location: The current location object.

        Returns:
            A string containing the generated dialogue.
        """
        prompt = self._create_dialogue_prompt(event, player, location)
        dialogue = self.llm.generate_text(prompt, max_tokens=50)  # Adjust max_tokens as needed
        return dialogue

    def _create_dialogue_prompt(self, event: dict, player: Character, location: Location) -> str:
        """
        Creates a prompt for the LLM based on the event and game context.

        Args:
            event: The current event dictionary.
            player: The player character object.
            location: The current location object.

        Returns:
            A string containing the formatted prompt for the LLM.
        """
        prompt = f"{player.name} is in the {location.name}. "
        if event["type"] == "encounter_creature":
            creature = event.get("creature", "a creature")
            prompt += f"{creature} approaches and says: "  # Guide the LLM to generate creature dialogue
        elif event["type"] == "find_item":
            item = event.get("item", "something")
            prompt += f"{player.name}, examining the {item}, thinks: "  # Guide the LLM to generate player thoughts
        # Add more prompt variations based on different event types

        return prompt
