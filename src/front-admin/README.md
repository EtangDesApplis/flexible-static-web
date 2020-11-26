# Calendar React
https://demo.mobiscroll.com/react/eventcalendar/dots-colors-labels#

# Secure with keycloak
https://scalac.io/user-authentication-keycloak-1/

## Keycloak behinds nginx proxy

Source: https://keycloak.discourse.group/t/keycloak-in-docker-behind-reverse-proxy/1195/12

Keycloak container env variable:
```
PROXY_ADDRESS_FORWARDING=true
```

nginx proxy pass set up (no split)
```
location ^~ /auth/ {
            proxy_pass http://localhost:32033;
            proxy_set_header X-Forwarded-For $host;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection ‘upgrade’;
            proxy_set_header Host $host;
          }
```

# To build
```
docker build -t etangdesapplis/demo-site-front-admin .
```
