Feature: Check titles on all pages in ua language
  As unregistered user
  I want to check all button in header
  So I can click on any button in the header
  and redirect to relevant page and titles.

  Scenario Outline: Different window size
    When I open Homepage custom size screen "<size>"
    Then I switch to ua language
    Given I see title "site_title_ua"
    Examples:
      | size         |
      | default_size |
      | mobile_size  |
      | tablet_size  |
