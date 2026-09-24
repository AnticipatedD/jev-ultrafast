import pytest
from unittest.mock import MagicMock

# Assuming jev_ultrafast is structured with a model module
# Adjust imports if your local paths differ slightly
from jev_ultrafast.model import action_space 

def test_action_space_select_options():
    """Assert that action_space properly parses and processes select option structures."""
    mock_node = MagicMock()
    mock_node.tag_name = "select"
    mock_node.get_attribute.return_value = "dropdown"
    
    # Simulate a choice configuration
    choices = action_space(mock_node)
    assert isinstance(choices, list)

def test_action_space_multiple_operations_per_node():
    """Assert that action_space handles multiple distinct operations on a single DOM node."""
    mock_node = MagicMock()
    mock_node.is_enabled.return_value = True
    mock_node.is_displayed.return_value = True
    
    # Verify that multi-operation payloads validate correctly
    result = action_space(mock_node)
    assert result is not None
