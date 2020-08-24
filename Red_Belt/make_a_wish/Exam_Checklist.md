For a red belt:
Login and Registration with validations
    <!-- -Validation errors should appear on the page -->
    <!-- -Logout feature - the user should not be able to enter the app if not logged in -->
Dashboard
    <!-- -Dashboard should say "Hello {{user}}" -->
    -Display all the wishes the logged user made that have not yet been granted in the top table
    -Each wish in the top table should have the remove, edit, and granted links
    -Display all the granted wishes and the users who made them in the bottom table
    -Display when the granted wishes were made and when they were granted
    -Clicking the granted link removes the wish from the top table and places it in the bottom table
Make a wish
    -Validations for empty input fields
    -Minimum length of three characters for the item and the description
    -Display errors with flash messages
    -Redirect back to the dashboard after making a wish or clicking the cancel button
    -The newly made wish should appear in the top table on the dashboard
Edit a wish
    -Same validations apply as when creating a wish
    -Redirect back to the dashboard after editing
    -The dashboard should show the changes made to the wish
HTML and CSS reflect the wireframe to at least 75% accuracy



<!-- <a href="https://google.com" class="button">Go to Google</a>
a.button {
    -webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;

    text-decoration: none;
    color: initial;
} -->