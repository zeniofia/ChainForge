# test_chainforge.py
"""
Tests for ChainForge module.
"""

import unittest
from chainforge import ChainForge

class TestChainForge(unittest.TestCase):
    """Test cases for ChainForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainForge()
        self.assertIsInstance(instance, ChainForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
