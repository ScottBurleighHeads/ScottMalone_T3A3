### T3A3 - Implement a System with Data and Application Layers.

Validation: In the crud resource the method option will only allow the certain request that is associated with it. for example method = [get]
The ORM helps prevent SQL injection prevention. User name and password are the basic first step to authentification. Bcrypt was used to hash the 
password to reduce brute force penetration. It is common for systems to have multi layers. So multi-layers can be made up like this: 

- First level basic: Username and password
- Second level: sha256
- Third level: bcrypt
- Fourth level: encryption/decryption

Out of the all the levels the bcrypt is the most important because the others are more likely to be hacked by brute force. Bcrypt has a parameter called salt that can be adjusted. As computers get more powerful as too the salt can get more powerful. hashes are only given in one direction. Once their made they cant be unmade. Oftern hashs will have other components attached to  the front of them so even if a hacker hacks one user the other users will be safe.

JWT give the user an access token that can be given a timelimit for a user to use so the user does not need to keep logging in. You should never store private 
information in your token. JWT are just encoded and can be decoded. JWT token is made up of a hash with three parts:
- header 
- payload 
- Signature JWT_SECRET_KEY

The signature cannot be change. Otherwise it will be invalidated. The hacker cannot generate the same hash if the secret is different. Thats the end of validation. Remember Authentification is about proving who you are.

Lets look into Authorisation:

Authorisation is different to authentification. Once you have proven who you are through authentification you will then need certain authorization to view or maked changes on the application. Authorisation is to associate 

