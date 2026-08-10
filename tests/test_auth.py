from services.auth_service import GmailAuthService

gmail = GmailAuthService().authenticate()

print("====================================")
print(" Gmail Authentication Successful")
print("====================================")
print(gmail)