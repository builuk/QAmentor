Feature: Check titles on all pages in ua language
  As unregistered user
  I want to check all button in header
  So I can click on any button in the header
  and redirect to relevant page and titles.

  Background:
    When I open Homepage
    Then I switch to ua language
    Given I see title "site_title_ua"

  Scenario: Title on About page in ua
    Then I click on About button
    Given I see title "about_title_ua"

  Scenario Outline: Titles on on ua language pages
    Then I click on "<button>" button
    Given I see title "<title>"
    Examples:
      | button                      | title                     |
      | path_delivery_and_payment   | delivery_and_payment_ua   |
      | path_return_and_replacement | return_and_replacement_ua |
      | path_contacts               | contacts_ua               |
      | path_help                   | help_ua                   |
