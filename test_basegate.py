# test_basegate.py
"""
Tests for BaseGate module.
"""

import unittest
from basegate import BaseGate

class TestBaseGate(unittest.TestCase):
    """Test cases for BaseGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BaseGate()
        self.assertIsInstance(instance, BaseGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BaseGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
