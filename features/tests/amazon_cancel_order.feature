# Created by annakarelina at 4/3/21
Feature: Cancel order items feature
  # Enter feature description here

  Scenario: User can cancel orders and items

    Given Open Amazon Help page
    When Input Cancel order into "Search the help library" and click
    Then Verify Cancel Items or Orders is present

