import subprocess

from behave import *


use_step_matcher("re")


@when("the user run klickbrick 'hello'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    args = "poetry run klickbrick hello".split()
    context.response = subprocess.run(args, capture_output=True, text=True).stdout


@then("the CLI prints 'Hello World'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert "Hello World\n" == context.response

