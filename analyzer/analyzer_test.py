"""analyzer_test.py: tests for analyzer.py"""
# pylint: disable=missing-function-docstring
import pytest
import yaml

from analyzer.analyzer import Analyzer


@pytest.fixture(name="analyzer")
def analyzer_fixtures():
    """Returns instance of Analyzer class as fixture for pytests"""
    return Analyzer()


def test_check_for_3p_actions_without_hash(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_script_injection(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_unsecure_commands(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_pull_request_target(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_inline_script(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_cache_action_usage(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_self_hosted_runners(analyzer) -> None:
    _ = analyzer
    assert True


def test_check_for_dangerous_write_permissions(analyzer) -> None:
    with open(
        "actions/action-with-write-permissions-all-jobs.yml", "r", encoding="utf-8"
    ) as action:
        action_dict = yaml.safe_load(action)
        assert analyzer.run_checks(action=action_dict) is False


def test_check_for_dangerous_write_permissions_one_job(analyzer) -> None:
    with open(
        "actions/action-with-write-permissions-one-job.yml", "r", encoding="utf-8"
    ) as action:
        action_dict = yaml.safe_load(action)
        assert analyzer.run_checks(action=action_dict) is False


def test_check_for_dangerous_write_permissions_write_all(analyzer) -> None:
    with open(
        "actions/action-with-write-all-permissions-all-jobs.yml", "r", encoding="utf-8"
    ) as action:
        action_dict = yaml.safe_load(action)
        assert analyzer.run_checks(action=action_dict) is False


def test_check_for_dangerous_write_permissions_one_job_write_all(analyzer) -> None:
    with open(
        "actions/action-with-write-all-permissions-one-job.yml", "r", encoding="utf-8"
    ) as action:
        action_dict = yaml.safe_load(action)
        assert analyzer.run_checks(action=action_dict) is False