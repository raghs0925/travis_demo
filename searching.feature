Feature: Verify negative search term

  Scenario: search for laptops normally
     Given we have navigated to "amazon.com"
      when we search for "laptop"
      then we will find results

  Scenario: search for laptops without laptops
     Given we have navigated to "amazon.com"
      when we search for "laptop -laptop"
      then we will find 0 results

