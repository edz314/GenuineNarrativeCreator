class AdvertiserInputProcessor:
    """
    Processes advertiser inputs to ensure they are valid, relevant, and in a format suitable for
    integration into the game's real-time narrative generation. Handles complex data structures,
    supports multiple advertising strategies, and ensures compliance with data standards.
    """

    def __init__(self):
        """
        Initializes the AdvertiserInputProcessor with default validation rules and processing strategies.
        """
        self.required_fields = ["product_name", "product_description", "target_audience"]
        self.optional_fields = ["campaign_duration", "placement_strategy", "branding_guidelines"]
        self.supported_strategies = ["immersive_integration", "product_placement", "interactive_advertising"]

    def process_input(self, advertiser_input):
        """
        Processes the advertiser input by validating and transforming it into a format that can be
        used in the narrative generation process.

        Args:
            advertiser_input (dict): A dictionary containing all the details provided by the advertiser.
            
        Returns:
            dict: A dictionary with processed data ready for use by other modules.

        Raises:
            ValueError: If the input is missing required fields or contains invalid data.
        """
        # Validate the input data
        self._validate_input(advertiser_input)

        # Process and transform the data
        processed_input = self._transform_input(advertiser_input)

        # Return the processed input ready for narrative integration
        return processed_input

    def _validate_input(self, advertiser_input):
        """
        Validates the advertiser input to ensure all required fields are present and data is valid.

        Args:
            advertiser_input (dict): The input data from the advertiser.

        Raises:
            ValueError: If any required fields are missing or if the data is invalid.
        """
        missing_fields = [field for field in self.required_fields if field not in advertiser_input]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        if 'placement_strategy' in advertiser_input and advertiser_input['placement_strategy'] not in self.supported_strategies:
            raise ValueError(f"Unsupported placement strategy: {advertiser_input['placement_strategy']}")

        # Add additional validation logic as needed (e.g., data types, field length, etc.)
        for field in advertiser_input:
            if not isinstance(advertiser_input[field], (str, int, float, dict, list)):
                raise ValueError(f"Invalid data type for field {field}: {type(advertiser_input[field])}")

    def _transform_input(self, advertiser_input):
        """
        Transforms the validated input into a structured format suitable for narrative generation.

        Args:
            advertiser_input (dict): The validated input data.

        Returns:
            dict: The transformed data ready for integration into the narrative.
        """
        # Example transformation: Create a narrative-friendly product descriptor
        product_descriptor = f"{advertiser_input['product_name']} - {advertiser_input['product_description']}"
        transformed_data = {
            "product_descriptor": product_descriptor,
            "target_audience": advertiser_input.get("target_audience"),
            "placement_strategy": advertiser_input.get("placement_strategy", "immersive_integration"),
            "branding_guidelines": advertiser_input.get("branding_guidelines", {}),
            "campaign_duration": advertiser_input.get("campaign_duration", "default_duration")
        }

        # Further transformation logic could be added here based on narrative needs
        # For example, adjust product descriptors based on target audience or customize narrative hooks

        return transformed_data

    def add_supported_strategy(self, strategy_name):
        """
        Adds a new supported placement strategy to the processor.

        Args:
            strategy_name (str): The name of the strategy to add.
        """
        if strategy_name not in self.supported_strategies:
            self.supported_strategies.append(strategy_name)

    def remove_supported_strategy(self, strategy_name):
        """
        Removes a supported placement strategy from the processor.

        Args:
            strategy_name (str): The name of the strategy to remove.
        """
        if strategy_name in self.supported_strategies:
            self.supported_strategies.remove(strategy_name)

    def update_required_fields(self, new_required_fields):
        """
        Updates the list of required fields that the advertiser input must contain.

        Args:
            new_required_fields (list): A list of new required fields.
        """
        if isinstance(new_required_fields, list) and all(isinstance(field, str) for field in new_required_fields):
            self.required_fields = new_required_fields
        else:
            raise ValueError("new_required_fields must be a list of strings.")

    def update_optional_fields(self, new_optional_fields):
        """
        Updates the list of optional fields that the advertiser input may contain.

        Args:
            new_optional_fields (list): A list of new optional fields.
        """
        if isinstance(new_optional_fields, list) and all(isinstance(field, str) for field in new_optional_fields):
            self.optional_fields = new_optional_fields
        else:
            raise ValueError("new_optional_fields must be a list of strings.")

    def reset_to_default(self):
        """
        Resets the processor's configuration to its default state.
        """
        self.required_fields = ["product_name", "product_description", "target_audience"]
        self.optional_fields = ["campaign_duration", "placement_strategy", "branding_guidelines"]
        self.supported_strategies = ["immersive_integration", "product_placement", "interactive_advertising"]
