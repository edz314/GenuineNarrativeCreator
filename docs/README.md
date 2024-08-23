# GenuineNarrativeCreator

**GenuineNarrativeCreator** is a modular framework designed to create dynamic and immersive narratives in real-time, integrating with various game engines and narrative systems. The project is structured to facilitate ease of development, maintenance, and scalability.

## Project Structure

The project is heriarchically structured, details are found in this file:

[docs/file_structure.mermaid](https://github.com/edz314/GenuineNarrativeCreator/blob/main/docs/file_structure.mermaid)

Directory Breakdown

narrative/

    generation/: Contains all modules related to the generation and structuring of narratives. This includes the core narrative generation logic, prompt management, and action execution.
    
    lore/: Manages the game's lore, ensuring consistency across the narrative.

core/

    data_management/: Manages game data, including character management and world state management.
    
    analysis/: Handles data analysis tasks, including collecting and analyzing data for improving narrative outcomes.
    
    feedback/: Processes feedback from the narrative and gameplay, feeding it back into the system for dynamic adjustments.
    
    integration/: Manages integration with different game engines (e.g., Pygame, Unity).
    
    utils/: Contains utility scripts for tasks like data loading and logging.

advertising/

    Handles advertising-related components, including processing advertiser inputs and generating reports.

interface/

    Manages the user interface components for interacting with the narrative system.

data/

    Contains configuration files in YAML format that define characters, dialogue, and world data.

docs/

    Contains project documentation, including this README, the license, and any architectural or requirement documents.

tests/

    Contains test cases for the different modules within the project, ensuring robustness and reliability.

Setup and Installation

To set up the project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/username/GenuineNarrativeCreator.git
cd GenuineNarrativeCreator
Install dependencies:

Ensure you have Python 3.8+ installed, then run:

bash
Copy code
pip install -r docs/requirements.txt
Run the tests:

To verify that everything is working correctly, run the test suite:

bash
Copy code
pytest tests/
Run the application:

To start the narrative generation process, run the main script:

bash
Copy code
python main.py

Usage

Once the application is running, you can interact with the narrative system through the user interface or integrate it with your game engine of choice. The narrative/generation/ and core/integration/ modules provide the core functionality to manage and generate immersive narratives based on player input and real-time data.

Contributing

We welcome contributions to improve this project! Please fork the repository, create a new branch, and submit a pull request. Ensure that all new features are covered by appropriate tests.
