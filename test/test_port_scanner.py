import pytest
import socket
from unittest.mock import patch, MagicMock
from src.port_scanner import scan_port, port_scanner

@pytest.fixture
def mock_socket():
    """Mocks the socket module's socket() instance."""
    with patch("socket.socket", autospec=True) as mock_socket:
        mock_instance = mock_socket.return_value.__enter__.return_value
        yield mock_instance



@patch("src.port_scanner.scan_port")
def test_port_scanner(mock_scan):
    """Test that the port_scanner function calls scan_port correctly."""
    target = "127.0.0.1"
    ports = range(80, 83)
    port_scanner(target, ports)
    
    mock_scan.assert_any_call(target, 80)
    mock_scan.assert_any_call(target, 81)
    mock_scan.assert_any_call(target, 82)

def test_scan_port_open(mock_socket):
    """Test that an open port is detected correctly."""
    mock_socket.connect_ex.return_value = 0
    scan_port("127.0.0.1", 80)
    mock_socket.connect_ex.assert_called_with(("127.0.0.1", 80))

def test_scan_port_closed(mock_socket):
    """Test that a closed port is detected correctly."""
    mock_socket.connect_ex.return_value = 1
    scan_port("127.0.0.1", 81)
    mock_socket.connect_ex.assert_called_with(("127.0.0.1", 81))

def test_scan_port_exception(mock_socket):
    """Test that socket exceptions are handled correctly."""
    mock_socket.connect_ex.side_effect = socket.error("Mocked error")
    scan_port("127.0.0.1", 82)
    mock_socket.connect_ex.assert_called_with(("127.0.0.1", 82))

