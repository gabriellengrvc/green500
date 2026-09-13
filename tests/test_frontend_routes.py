from pathlib import Path

from green500 import web


def test_root_serves_built_react_dashboard():
    response = web.index()
    path = Path(response.path)

    assert path == web.STATIC_DIR / "dashboard/index.html"
    assert path.is_file()
    assert "/static/dashboard/assets/" in path.read_text(encoding="utf-8")


def test_data_route_preserves_source_interface():
    response = web.data_portal()
    path = Path(response.path)

    assert path == web.STATIC_DIR / "index.html"
    assert path.is_file()
    assert 'id="source-dialog"' in path.read_text(encoding="utf-8")
