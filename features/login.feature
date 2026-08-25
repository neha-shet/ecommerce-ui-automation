Feature: Login functionality
  As a registered SauceDemo user
  I want to attempt logging into the application with various credentials
  So that valid users gain access while invalid or locked-out attempts receive appropriate error messages

  @smoke @regression
  Scenario: Successful login with valid credentials
    Given the user is on the SauceDemo login page
    When the user enters username "standard_user" and password "secret_sauce"
    And the user clicks the login button
    Then the Products page should be displayed

  @regression
  Scenario Outline: Failed login with invalid or missing credentials
    Given the user is on the SauceDemo login page
    When the user enters username "<username>" and password "<password>"
    And the user clicks the login button
    Then the login error message "<expected_error>" should be displayed

    Examples:
      | username        | password     | expected_error                                                            |
      | invalid_user    | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | standard_user   | wrong_pass   | Epic sadface: Username and password do not match any user in this service |
      |                 | secret_sauce | Epic sadface: Username is required                                       |
      | standard_user   |              | Epic sadface: Password is required                                       |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                      |
