import frontend
import backend

frontend.main()

backend1 = backend.PasswordManagerBE()
backend1.save_data("udemy","random@gmail.com","15421")
print(backend1.generate_password())