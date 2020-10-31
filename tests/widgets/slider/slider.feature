Feature: Slider Widget
   Slider Widget on https://demoqa.com/slider

  Scenario Outline: Slider position matches the value in the input field
    When I move the slider to <position>
    Then the input should be <value>

    Examples:
      | position | value |
      | 25       | 25    |
      | 50       | 50    |

   Scenario Outline: Enter a position moves the slider
     When I enter <value>
     Then the slider should move to <position>

     Examples:
      | position | value |
      | 10       | 10    |
      | 50       | 50    |

   Scenario: range_slide_value increases when slid right
     When range_slider value > 0 if slider is moved right
     Then range_slider value < than original