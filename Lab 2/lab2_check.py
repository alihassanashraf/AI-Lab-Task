"""Automated checks for Lab 2 classroom-agent requirements."""

import unittest

from lab2_model import ClassroomAgent


class TestClassroomAgent(unittest.TestCase):
    def test_empty_room_has_priority_over_high_temperature(self):
        agent = ClassroomAgent()
        target, send = agent.act(29, False)
        self.assertEqual(target, "ECO")
        self.assertTrue(send)

    def test_empty_room_has_priority_over_low_temperature(self):
        agent = ClassroomAgent()
        target, send = agent.act(10, False)
        self.assertEqual(target, "ECO")
        self.assertTrue(send)

    def test_exact_temperature_boundaries_are_idle_when_occupied(self):
        agent = ClassroomAgent()
        self.assertEqual(agent.act(20, True), ("IDLE", True))
        # The previous target is already IDLE, so the second boundary produces no command.
        self.assertEqual(agent.act(26, True), ("IDLE", False))

    def test_duplicate_target_is_not_sent_twice(self):
        agent = ClassroomAgent()
        self.assertEqual(agent.act(29, True), ("COOL", True))
        self.assertEqual(agent.act(29, True), ("COOL", False))

    def test_mode_transition_sends_a_new_command(self):
        agent = ClassroomAgent()
        self.assertEqual(agent.act(29, True), ("COOL", True))
        self.assertEqual(agent.act(24, True), ("IDLE", True))

    def test_required_full_trace(self):
        percepts = [
            (29, True),
            (29, True),
            (20, True),
            (26, True),
            (19, True),
            (29, False),
            (29, False),
            (24, True),
            (24, True),
        ]
        expected_targets = [
            "COOL", "COOL", "IDLE", "IDLE", "WARM", "ECO", "ECO", "IDLE", "IDLE"
        ]
        expected_send = [True, False, True, False, True, True, False, True, False]

        agent = ClassroomAgent()
        actual = [agent.act(*percept) for percept in percepts]
        self.assertEqual([item[0] for item in actual], expected_targets)
        self.assertEqual([item[1] for item in actual], expected_send)

    def test_temperature_input_must_be_numeric(self):
        agent = ClassroomAgent()
        with self.assertRaises(TypeError):
            agent.act("29", True)

    def test_occupancy_input_must_be_boolean(self):
        agent = ClassroomAgent()
        with self.assertRaises(TypeError):
            agent.act(29, 1)

    def test_noise_around_upper_threshold_causes_mode_changes(self):
        agent = ClassroomAgent()
        results = [
            agent.act(25.9, True),
            agent.act(26.1, True),
            agent.act(25.9, True),
            agent.act(26.1, True),
        ]
        self.assertEqual(
            results,
            [("IDLE", True), ("COOL", True), ("IDLE", True), ("COOL", True)],
        )


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClassroomAgent)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
