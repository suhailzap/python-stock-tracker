# python-stock-tracker
Now you can test this streamlined application locally.

    Navigate & Build:
    Bash

cd python-stock-tracker
docker build -t stock-tracker:local .

Run:
Bash

docker run -d -p 5000:5000 --name stock-app stock-tracker:local

Test:

    Open your browser to: http://localhost:5000

    You should be redirected to the login page.

    Log in with user/password.

    You should see the professional, colorful dashboard.

Cleanup:
Bash

docker stop stock-app && docker rm stock-app
