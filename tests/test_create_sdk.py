import json
import types
import sys
from pathlib import Path

import pytest


def import_create_sdk(monkeypatch):
    try:
        from app.user_commands import create_sdk
        return create_sdk
    except Exception as e:
        if isinstance(e, ModuleNotFoundError) and e.name.startswith('rich'):
            rich = types.ModuleType("rich")
            console = types.ModuleType("rich.console")
            console.Console = object
            panel = types.ModuleType("rich.panel")
            panel.Panel = object
            prompt = types.ModuleType("rich.prompt")
            class DummyPrompt:
                @staticmethod
                def ask(*a, **kw):
                    return ""
            prompt.Prompt = DummyPrompt
            table = types.ModuleType("rich.table")
            table.Table = object
            tree = types.ModuleType("rich.tree")
            tree.Tree = object
            markdown = types.ModuleType("rich.markdown")
            markdown.Markdown = object
            traceback_mod = types.ModuleType("rich.traceback")
            traceback_mod.install = lambda: None
            rich.console = console
            rich.panel = panel
            rich.prompt = prompt
            rich.table = table
            rich.tree = tree
            rich.markdown = markdown
            rich.traceback = traceback_mod
            rich.box = object()
            modules = {
                'rich': rich,
                'rich.console': console,
                'rich.panel': panel,
                'rich.prompt': prompt,
                'rich.table': table,
                'rich.tree': tree,
                'rich.markdown': markdown,
                'rich.traceback': traceback_mod,
                'rich.box': rich.box,
            }
            sys.modules.update(modules)
            from app.user_commands import create_sdk
            return create_sdk
        else:
            raise


@pytest.fixture
def create_sdk_module(monkeypatch):
    return import_create_sdk(monkeypatch)


@pytest.fixture
def temp_output_dir(tmp_path, monkeypatch, create_sdk_module):
    out_dir = tmp_path / "output_sdk"
    monkeypatch.setattr(create_sdk_module, "OUTPUT_BASE_DIR", out_dir)
    return out_dir


def test_build_command_creates_directory(temp_output_dir, tmp_path, create_sdk_module):
    spec = tmp_path / "spec.yaml"
    spec.write_text("openapi: 3.0")
    pkg_name = create_sdk_module.sanitize_sdk_name("mysdk")
    cmd = create_sdk_module.build_command(spec, "mysdk", pkg_name)
    assert temp_output_dir.joinpath("mysdk").exists()
    assert cmd == [
        "openapi-python-client", "generate",
        "--path", str(spec),
        "--output-path", str(temp_output_dir / "mysdk"),
        "--meta", "poetry",
        "--overwrite",
        "--package-name", pkg_name,
    ]


def test_registry_short_name_for_spec(create_sdk_module):
    registry = {"foo": {"openapi_name": "My_API"}}
    spec = Path("My_API.yaml")
    assert create_sdk_module.registry_short_name_for_spec(spec, registry) == "foo"
    assert create_sdk_module.registry_short_name_for_spec(Path("Other.yaml"), registry) is None


def test_save_and_load_registry(tmp_path, monkeypatch, create_sdk_module):
    file = tmp_path / "reg.json"
    monkeypatch.setattr(create_sdk_module, "PLATFORM_REGISTRY_FILE", file)
    data = {"k": {"openapi_name": "v"}}
    create_sdk_module.save_registry(data)
    assert json.loads(file.read_text()) == data
    assert create_sdk_module.load_registry() == data
