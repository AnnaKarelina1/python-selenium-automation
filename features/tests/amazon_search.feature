# Created by annakarelina at 3/30/21
Feature:  Amazon search test
  # Enter feature description here

#  Scenario Outline: User can search for a product
#    Given Open Amazon page
#    When Input <search_word> into Amazon search field
#    When Click on Amazon search icon
#    Then Product results for <search_result> are shown on Amazon
#    Then Verify <search_word> in URL
#    Examples:
#      |search_word  | search_result|
#      | Dress       | "Dress"      |
#      | Mug         | "Mug"        |
#      | Watches     |"Watches"     |

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Mug into Amazon search field
    When Click on Amazon search icon
    Then Product results for "Mug" are shown on Amazon
    Then Verify Mug in URL