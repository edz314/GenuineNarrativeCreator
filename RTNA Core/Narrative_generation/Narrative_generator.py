# core/narrative_generation/narrative_generator.py

from core.narrative_structuring import NarrativeStructuring
from core.character_manager import CharacterManager
from core.world_manager import WorldManager
from core.narrative_generation.event_generator import EventGenerator
from core.llm_integration import LLMIntegration
from core.risk_assessment.relationship_risk_factor import RelationshipRiskFactor
from core.escalation_manager import EscalationManager

class NarrativeGenerator:
    """
    Generates narrative text, handles events, dialogue, and risk assessment.
    """

    def __init__(self, narrative_structuring: NarrativeStructuring, 
                 character_manager: CharacterManager, 
                 world_manager: WorldManager, 
                 escalation_manager: EscalationManager): 
        """Initializes NarrativeGenerator."""
        self.narrative_structuring = narrative_structuring
        self.character_manager = character_manager
        self.world_manager = world_manager
        self.event_generator = EventGenerator() 
        self.escalation_manager = escalation_manager
        self.risk_factor_calculator = RelationshipRiskFactor("Game Purpose", "User Profile Placeholder")  
        self.llm = LLMIntegration(provider="huggingface", model_name="gpt2")  # Or your chosen LLM

    def generate_narrative(self, player_action: str, current_location: str) -> str:
        """Generates narrative text based on player action and location."""
        player = self.character_manager.get_player()
        location_details = self.world_manager.get_location_details(current_location)

        # 1. Generate Event:
        event = self.event_generator.generate_event(player_action, player, location_details)

        # 2. Apply Event Consequences:
        self._apply_event_consequences(event, player, current_location)

        # 3. Collect Interaction Data (placeholder)
        interaction_data = {}  # Get data from event, dialogue, etc.

        # 4. Calculate Risk:
        risk_factor = self.risk_factor_calculator.calculate_risk(interaction_data)  

        # 5. Escalate if Needed:
        if self.risk_factor_calculator.is_escalation_required(risk_factor):
            self.escalation_manager.escalate_conversation(interaction_data)
            return "Conversation escalated to a specialist." # Or a similar message

        # 6. Generate Dialogue (using LLM):
        if self._should_generate_dialogue(event, player, location_details):
            dialogue = self._generate_dialogue_with_llm(event, player, location_details)
        else: 
            dialogue = ""

        # 7. Structure Narrative (include event and dialogue):
        structured_narrative = self.narrative_structuring.structure_narrative(
            player_action, player, location_details, event, dialogue
        )

        # 8. Generate Text from Structure:
        narrative_text = self._generate_text_from_structure(structured_narrative)
        return narrative_text

    def _apply_event_consequences(self, event: dict, player: Character, current_location: str):
        """Applies the consequences of an event."""
        for consequence in event["consequences"]:
            if consequence["type"] == "health_change":
                self.character_manager.update_character_health(player.name, consequence["amount"])
            elif consequence["type"] == "item_add":
                self.character_manager.add_item_to_inventory(player.name, consequence["item"])
            elif consequence["type"] == "move_location":
                new_location = consequence["location"]
                current_location = new_location  # Update the player's location
                print(f"Moving player to {new_location}") # Placeholder for more detailed logic
            elif consequence["type"] == "trigger_event":
                new_event_type = consequence["event_type"]
                # Add logic here to trigger a new event of the specified type
                print(f"Triggering new event of type: {new_event_type}") # Placeholder 
            elif consequence["type"] == "change_character_stat":
                stat_name = consequence["stat"]
                amount = consequence["amount"]
                player.change_stat(stat_name, amount) 
            # ... add logic for handling other consequence types ...

    def _should_generate_dialogue(self, event, player, location):
        """Determines if dialogue should be generated for the given context."""
        # Implement your logic here - when should dialogue occur?
        # Example:
        if event["type"] in ["encounter_creature", "find_item"]: 
            return True
        return False

    def _generate_dialogue_with_llm(self, event, player, location) -> str:
        """Generates dialogue using the LLM."""
        # Construct a prompt for the LLM based on context
        prompt = self._create_dialogue_prompt(event, player, location)

        # Generate dialogue using the LLM 
        dialogue = self.llm.generate_text(prompt, max_tokens=50)  # Adjust max_tokens as needed
        return dialogue

    def _create_dialogue_prompt(self, event, player, location) -> str:
        """Creates a prompt for the LLM based on the current context."""
        # Example prompt:
        prompt = f"{player.name} is in the {location.name}. "
        if event["type"] == "encounter_creature":
            creature = event.get("creature", "a creature")
            prompt += f"{creature} says: "
        elif event["type"] == "find_item":
            item = event.get("item", "something")
            prompt += f"{player.name} thinks: "
        return prompt 

    def _generate_text_from_structure(self, structured_narrative: dict) -> str:
        """Generates text from the structured narrative."""
        narrative_text = f"{structured_narrative['introduction']}\n"
        for event_desc in structured_narrative['events']:
            narrative_text += f"- {event_desc}\n"
        if structured_narrative["dialogue"]:
            narrative_text += f"\"{structured_narrative['dialogue']}\"\n"
        narrative_text += f"{structured_narrative['conclusion']}"
        return narrative_text
