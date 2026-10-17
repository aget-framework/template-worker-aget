"""Shared pytest configuration for this template's tests."""

# --------------------------------------------------------------------------
# Repository-location isolation (gmelli/aget-aget#3019; same list as core's tests/conftest.py)
#
# git obeys these variables in every command, whatever folder it runs in. A hook run from a linked
# worktree hands the suite an absolute GIT_DIR, so a test that runs `git init/config/add/commit` in a
# scratch folder acts on the repository GIT_DIR names instead; GIT_CONFIG redirects `git config` writes
# to the file it names. They are removed here, at import, before any test module is collected. A test
# that needs one sets it itself. Falsifier: tests/test_conftest_git_env_isolation.py
# --------------------------------------------------------------------------
import os as _os
import tempfile as _tempfile

REPO_LOCATION_VARS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_COMMON_DIR", "GIT_INDEX_FILE",
                      "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES",
                      "GIT_NAMESPACE", "GIT_PREFIX", "GIT_CONFIG")
for _var in REPO_LOCATION_VARS:
    _os.environ.pop(_var, None)

# git also searches upward for a repository from a folder that is not one. When the temp folder sits inside a
# working tree (a harness that keeps TMPDIR in its checkout), a test running git in a non-repository scratch
# folder would commit into the enclosing repository. Stop that search at the temp root.
_tmp_root = _tempfile.gettempdir()
_ceilings = [_tmp_root, _os.path.realpath(_tmp_root)] + [p for p in _os.environ.get("GIT_CEILING_DIRECTORIES", "").split(_os.pathsep) if p]
_os.environ["GIT_CEILING_DIRECTORIES"] = _os.pathsep.join(dict.fromkeys(_ceilings))
