import os
import shutil

# Define the current structure and the desired structure
structure_map = {
    "RTNA Core/Narrative_generation/Narrative_generator.py": "narrative/generation/Narrative_generator.py",
    "RTNA Core/Narrative_generation/PromptManager.py": "narrative/generation/PromptManager.py",
    "RTNA Core/Narrative_generation/Narrative_structuring.py": "narrative/generation/Narrative_structuring.py",
    "RTNA Core/Narrative_generation/action_executor.py": "narrative/generation/action_executor.py",
    "RTNA Core/Narrative_generation/escalation_manager.py": "narrative/generation/escalation_manager.py",
    "RTNA Core/Narrative_generation/event_generator.py": "narrative/generation/event_generator.py",
    "RTNA Core/Narrative_generation/character.py": "core/data_management/character.py",
    "RTNA Core/Narrative_generation/dialogue.py": "core/data_management/dialogue.py",
    "RTNA Core/Narrative_generation/world_manager.py": "core/data_management/world_manager.py",
    "RTNA Core/data_analysis/data_analyzer.py": "core/analysis/data_analyzer.py",
    "RTNA Core/data_analysis/data_collector.py": "core/analysis/data_collector.py",
    "RTNA Core/feedback_loop/feedback_processor.py": "core/feedback/feedback_processor.py",
    "RTNA Core/game_integration/game_integrator.py": "core/game_integration/game_integrator.py",
    "RTNA Core/utils/logging.py": "core/utils/logging.py",
    "RTNA Core/utils/text_processing.py": "core/utils/text_processing.py",
    "data/lore.py": "narrative/lore/lore.py",
    "rtna_advertising/advertiser_input/advertiser_input_processor.py": "advertising/advertiser_input_processor.py",
    "rtna_advertising/reporting/report_generator.py": "advertising/report_generator.py",
    "rtna_user_interface/user_interface.py": "interface/user_interface.py",
}

def create_directories(path):
    """
    Create the directory structure for the given path if it does not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(src, dst):
    """
    Move a file from src to dst, creating any necessary directories.
    """
    create_directories(os.path.dirname(dst))
    shutil.move(src, dst)

def restructure_codebase(structure_map):
    """
    Restructure the codebase according to the structure map.
    """
    for src, dst in structure_map.items():
        if os.path.exists(src):
            print(f"Moving {src} to {dst}")
            move_file(src, dst)
        else:
            print(f"Source file {src} does not exist and cannot be moved.")

if __name__ == "__main__":
    restructure_codebase(structure_map)
