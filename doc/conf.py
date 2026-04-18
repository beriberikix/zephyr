# Zephyr documentation build configuration file.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
import sys
import textwrap
from pathlib import Path

ZEPHYR_BASE = Path(__file__).resolve().parents[1]
ZEPHYR_BUILD = Path(os.environ.get("OUTPUT_DIR")).resolve()

# Add the '_extensions' directory to sys.path, to enable finding Sphinx
# extensions within.
sys.path.insert(0, str(ZEPHYR_BASE / "doc" / "_extensions"))

# Add the '_scripts' directory to sys.path, to enable finding utility
# modules.
sys.path.insert(0, str(ZEPHYR_BASE / "doc" / "_scripts"))

# Add the directory which contains the runners package as well,
# for autodoc directives on runners.xyz.
sys.path.insert(0, str(ZEPHYR_BASE / "scripts" / "west_commands"))

# Add the directory which contains the pytest-twister-pytest
sys.path.insert(0, str(ZEPHYR_BASE / "scripts" / "pylib" / "pytest-twister-harness" / "src"))

import redirects  # noqa: E402

try:
    import west as west_found
except ImportError:
    west_found = False

# -- Project --------------------------------------------------------------

project = "Zephyr Project"
copyright = "2015-2026 Zephyr Project members and individual contributors"
author = "The Zephyr Project Contributors"

# parse version from 'VERSION' file
with open(ZEPHYR_BASE / "VERSION") as f:
    m = re.match(
        (
            r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
            + r"^VERSION_MINOR\s*=\s*(\d+)$\n"
            + r"^PATCHLEVEL\s*=\s*(\d+)$\n"
            + r"^VERSION_TWEAK\s*=\s*\d+$\n"
            + r"^EXTRAVERSION\s*=\s*(.*)$"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract kernel version\n")
        version = "Unknown"
    else:
        major, minor, patch, extra = m.groups(1)
        version = ".".join((major, minor, patch))
        if extra:
            version += "-" + extra

release = version

# parse SDK version from 'SDK_VERSION' file
with open(ZEPHYR_BASE / "SDK_VERSION") as f:
    sdk_version = f.read().strip()

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.autodoc",
    "sphinx.ext.graphviz",
    "sphinxcontrib.jquery",
    "sphinxcontrib.programoutput",
    "zephyr.application",
    "zephyr.html_redirects",
    "zephyr.kconfig",
    "zephyr.dtcompatible-role",
    "zephyr.link-roles",
    "sphinx_tabs.tabs",
    "sphinx_sitemap",
    "zephyr.doxyrunner",
    "zephyr.doxybridge",
    "zephyr.doxytooltip",
    "zephyr.gh_utils",
    "zephyr.manifest_projects_table",
    "notfound.extension",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "zephyr.external_content",
    "zephyr.domain",
    "zephyr.api_overview",
    "sphinx_llm.txt",
]
