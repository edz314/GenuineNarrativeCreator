class RelationshipRiskFactor:
    """
    Calculates the relationship risk factor based on various inputs such as user interactions, 
    emotional tone, frequency of interaction, and other relevant metrics.
    This risk factor can be used to determine if an escalation is necessary.
    """

    def __init__(self, base_risk=0.1):
        """
        Initializes the RelationshipRiskFactor with a base risk level.

        Args:
            base_risk (float): The base risk level, serving as the starting point for calculations.
        """
        self.base_risk = base_risk
        self.risk_modifiers = {
            'emotional_tone': self._evaluate_emotional_tone,
            'interaction_frequency': self._evaluate_interaction_frequency,
            'sensitive_information': self._evaluate_sensitive_information,
            'interaction_duration': self._evaluate_interaction_duration
        }

    def calculate_risk(self, interaction_data):
        """
        Calculates the overall risk factor based on the interaction data provided.

        Args:
            interaction_data (dict): A dictionary containing various metrics from the interaction.

        Returns:
            float: The calculated risk factor, a value between 0 and 1.
        """
        risk_score = self.base_risk

        for key, value in interaction_data.items():
            if key in self.risk_modifiers:
                risk_score += self.risk_modifiers[key](value)

        # Ensure the risk score stays within the range [0, 1]
        return min(max(risk_score, 0.0), 1.0)

    def _evaluate_emotional_tone(self, tone_score):
        """
        Evaluates the emotional tone of the interaction and adjusts the risk score.

        Args:
            tone_score (float): A score representing the emotional tone of the interaction (e.g., -1 for negative, 0 for neutral, 1 for positive).

        Returns:
            float: A risk adjustment based on the emotional tone.
        """
        if tone_score < 0:
            return 0.2  # Increase risk for negative emotional tone
        elif tone_score > 0:
            return -0.1  # Decrease risk for positive emotional tone
        return 0.0  # Neutral tone does not affect risk

    def _evaluate_interaction_frequency(self, frequency_score):
        """
        Evaluates the frequency of interactions and adjusts the risk score.

        Args:
            frequency_score (float): A score representing how frequently the user interacts with the system.

        Returns:
            float: A risk adjustment based on interaction frequency.
        """
        if frequency_score > 5:  # High frequency
            return 0.1
        elif frequency_score < 1:  # Low frequency
            return -0.05
        return 0.0  # Normal frequency does not affect risk

    def _evaluate_sensitive_information(self, sensitive_info_flag):
        """
        Evaluates the presence of sensitive information in the interaction.

        Args:
            sensitive_info_flag (bool): A flag indicating whether sensitive information was disclosed.

        Returns:
            float: A risk adjustment based on the presence of sensitive information.
        """
        return 0.3 if sensitive_info_flag else 0.0

    def _evaluate_interaction_duration(self, duration):
        """
        Evaluates the duration of the interaction and adjusts the risk score.

        Args:
            duration (float): The duration of the interaction in minutes.

        Returns:
            float: A risk adjustment based on interaction duration.
        """
        if duration > 30:  # Long interaction
            return 0.2
        elif duration < 5:  # Very short interaction
            return -0.1
        return 0.0  # Normal duration does not affect risk

    def add_risk_modifier(self, modifier_name, modifier_function):
        """
        Adds a custom risk modifier to the assessment process.

        Args:
            modifier_name (str): The name of the risk modifier.
            modifier_function (function): The function that calculates the risk adjustment.

        Raises:
            ValueError: If the modifier function is not callable.
        """
        if callable(modifier_function):
            self.risk_modifiers[modifier_name] = modifier_function
        else:
            raise ValueError("Modifier function must be callable.")

    def remove_risk_modifier(self, modifier_name):
        """
        Removes an existing risk modifier from the assessment process.

        Args:
            modifier_name (str): The name of the risk modifier to remove.

        Raises:
            KeyError: If the modifier does not exist.
        """
        if modifier_name in self.risk_modifiers:
            del self.risk_modifiers[modifier_name]
        else:
            raise KeyError(f"No such risk modifier: {modifier_name}")

    def update_base_risk(self, new_base_risk):
        """
        Updates the base risk level for the assessment.

        Args:
            new_base_risk (float): The new base risk level.
        """
        if 0 <= new_base_risk <= 1:
            self.base_risk = new_base_risk
        else:
            raise ValueError("Base risk must be between 0 and 1.")
