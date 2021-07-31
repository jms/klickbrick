# Created by jms at 7/31/21
Feature: hello


  Scenario: Hello Command
    When the user run klickbrick 'hello'
    Then the CLI prints 'hello world'
