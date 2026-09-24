import pytest
import http.client
from threading import Thread
from http.server import ThreadingHTTPServer
from jev_ultrafast.demo import Handler, main  # Adjust path if needed

@pytest.fixture(scope="module")
def local_demo_server():
    """Spins up the demo server Handler on an ephemeral port for integration testing."""
    # Bind to port 0 to let the OS assign a free port automatically
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_port
    
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    
    yield f"127.0.0.1:{port}"
    
    server.shutdown()
    server.server_close()

def test_demo_post_forbidden_missing_token(local_demo_server):
    """Assert that a POST request missing valid token/origin tags returns a 403 Forbidden response."""
    conn = http.client.HTTPConnection(local_demo_server)
    headers = {"Origin": "http://malicious-site.com"}
    
    # Send a payload missing valid structural parameters
    conn.request("POST", "/", body=b"{}", headers=headers)
    response = conn.getresponse()
    
    assert response.status == 403
    conn.close()
