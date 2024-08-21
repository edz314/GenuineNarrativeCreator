# tests/test_rtna_core.py

import unittest
from rtna_core.narrative_generation.narrative_generator import NarrativeGenerator
from rtna_core.narrative_generation.narrative_structuring import NarrativeStructuring
from rtna_core.data_analysis.data_collector import DataCollector
from rtna_core.data_analysis.data_analyzer import DataAnalyzer
from rtna_core.feedback_loop.feedback_processor import FeedbackProcessor
from rtna_core.game_integration.game_integrator import GameIntegrator

class TestRTNCore(unittest.TestCase):

    def setUp(self):
        self.narrative_structuring = NarrativeStructuring()
        self.narrative_generator = NarrativeGenerator(self.narrative_structuring)
        self.data_collector = DataCollector()
        self.data_analyzer = DataAnalyzer()
        self.feedback_processor = FeedbackProcessor(self.narrative_generator, self.narrative_structuring)
        self.game_integrator = GameIntegrator(self.narrative_generator, self.data_collector, self.feedback_processor)

    def test_narrative_generation(self):
        player_actions = ["explore forest", "find treasure chest"]
        advertiser_input = {"product": "energy drink", "context": "exploration"}
        narrative_text = self.narrative_generator.generate_narrative(player_actions, advertiser_input)
        self.assertIsInstance(narrative_text, str)

    def test_data_collection(self):
        player_action = "use item"
        narrative_context = "exploring a dark cave"
        advertiser_input = {"product": "flashlight", "context": "exploration"}
        self.data_collector.collect_data(player_action, narrative_context, advertiser_input)
        data = self.data_collector.get_data()
        self.assertEqual(len(data), 1)

    def test_data_analysis(self):
        data = [
            {"brand_immersion": 0.8, "engagement": 0.9},
            {"brand_immersion": 0.7, "engagement": 0.8}
        ]
        analysis_results = self.data_analyzer.analyze_data(data)
        self.assertIsInstance(analysis_results, dict)

    def test_feedback_processing(self):
        analysis_results = {"brand_immersion": 0.4, "engagement": 0.6}
        player_actions = ["explore forest", "find treasure chest"]
        advertiser_input = {"product": "energy drink", "context": "exploration"}
        adapted_narrative_text = self.feedback_processor.process_feedback(analysis_results, player_actions, advertiser_input)
        self.assertIsInstance(adapted_narrative_text, str)

    def test_game_integration(self):
        # This test will depend on the specific game engine being used
        # You'll need to implement a mock game engine or use a specific game engine
        # for testing
        pass

if __name__ == '__main__':
    unittest.main()
