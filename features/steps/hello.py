from behave import *

use_step_matcher("re")


@when("the user run klickbrick 'hello'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: When the user run klickbrick \'hello\'')
    pass


@then("the CLI prints 'hello world'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Then the CLI prints \'hello world\'')
    pass
