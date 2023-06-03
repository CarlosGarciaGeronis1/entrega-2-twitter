import datetime
import unittest

####Capa de dominio####

class Evento:
    def __init__(self, username, tipo, hora):
        self.username = username
        self.tipo = tipo
        self.hora = hora


class RegistroEventos:
    def __init__(self):
        self.eventos = []

    def registrarEvento(self, username, tipo, hora):
        evento = Evento(username, tipo, hora)
        self.eventos.append(evento)

    def displayEventos(self):
        for i in range(1, len(self.eventos)):
            print("Evento:\n")
            print(self.eventos[i].username)
            print("Tipo de evento:" + self.eventos[i].tipo+"\n")
            




# Clase para representar un tweet
class Tweet:
    def __init__(self):
        self.username = None
        self.content = None
        self.hora = None
        self.tweetPadre = None
        self.replies = None
        """self.username = username
        self.content = content
        self.timestamp = datetime.datetime.now()
        self.replies = []"""

    def setUsername(self, username):
        self.username = username

    def setContent(self, content):
        self.content = content

    def setHora(self, hora):
        self.hora = hora

    def setTweetPadre(self, tweetPadre):
        self.tweetPadre = tweetPadre

    def setReplies(self, replies):
        self.replies = replies

    

    def add_reply(self, reply):
        self.replies.append(reply)

    def display(self):
        if self.tweetPadre == True:
            print("##TWEET##")
            print(f"Usuario: {self.username}")
            print(f"Contenido: {self.content}")
            print(f"Fecha y hora: {self.hora}\n")
            print("Respuestas:\n")
            for reply in self.replies:
                reply.display()
            print()
        else:
            print(f"Usuario: {self.username}")
            print(f"Contenido: {self.content}")
            print(f"Fecha y hora: {self.hora}\n")
            

class TweetBuilder:
    def __init__(self):
        self.tweet = Tweet()
        

    def addUsername(self, username):
        self.tweet.setUsername(username)
        return self
    
    def addContent(self, content):
        self.tweet.setContent(content)
        return self
    
    def addHora(self, hora):
        self.tweet.setHora(hora)
        return self
    
    def addTweetPadre(self, tweetPadre):
        self.tweet.setTweetPadre(tweetPadre)
        return self
    
    def addReplies(self, replies):
        self.tweet.setReplies(replies)
        return self
    def build(self):
        return self.tweet


    # Clase para representar un usuario
class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.superUser = None

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setSuperUser(self, superUser):
        self.superUser = superUser

#Builder de la clase User
class UserBuilder:
    def __init__(self):
        self.user = User()

    def addUsername(self, username):
        self.user.setUsername(username)
        return self
    
    def addPassword(self, password):
        self.user.setPassword(password)
        return self
    
    def addSuperUser(self, superUser):
        self.user.setSuperUser(superUser)
        return self
    
    def build(self):
        return self.user
    

class UserFactory:
    @staticmethod
    def createSuperUser(username, password):
        return UserBuilder().addUsername(username).addPassword(password).addSuperUser(True).build()
    @staticmethod
    def createNormalUser(normalUsername, normalPassword):
        return UserBuilder().addUsername(normalUsername).addPassword(normalPassword).addSuperUser(False).build()


####Capa de aplicacion####


# Clase para gestionar la autenticación de usuarios
class AuthenticationManager:
    def __init__(self):
        self.users = []
        self.registroEventos = RegistroEventos()

    def register(self, username, password, superUser):
        if superUser == "1":
            userFactory = UserFactory()
            user = userFactory.createSuperUser(username, password)
        else:
            userFactory = UserFactory()
            user = userFactory.createNormalUser(username, password)


        self.users.append(user)
        print("Registro exitoso!\n")
        return user 

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Inicio de sesión exitoso!\n")
                self.registroEventos.registrarEvento(user.username, "Se loggeó", datetime.datetime.now())
                return user

        print("Credenciales inválidas. Por favor, intenta de nuevo.")

        
    

# Clase para gestionar la publicación y visualización de tweets
class TwitterApp:
    def __init__(self, authentication_manager, registroEventos):
        self.authentication_manager = authentication_manager
        self.registroEventos = registroEventos
        self.tweets = []

    def post_tweet(self, user, content):
        #tweet = Tweet(user.username, content)
        if user.superUser == True:
            tweet = TweetBuilder().addUsername(user.username + " (Super)" ).addContent(content).addHora(datetime.datetime.now()).addTweetPadre(True).addReplies([]).build()
            self.registroEventos.registrarEvento(user.username + " (super)", "Posteó un tweet", datetime.datetime.now())
        else:
            tweet = TweetBuilder().addUsername(user.username).addContent(content).addHora(datetime.datetime.now()).addTweetPadre(True).addReplies([]).build()
            self.registroEventos.registrarEvento(user.username, "Posteó un tweet", datetime.datetime.now())
        self.tweets.append(tweet)
        print("Tweet publicado con éxito!")

    def view_tweets(self):
        for i, tweet in enumerate(self.tweets):
            print(f"Índice: {i}")
            tweet.display()

    def reply_to_tweet(self, user, tweet_index, content):
        if tweet_index >= 0 and tweet_index < len(self.tweets):
            tweet = self.tweets[tweet_index]
            if user.superUser == True:
                reply = TweetBuilder().addUsername(user.username + " (super)").addContent(content).addHora(datetime.datetime.now()).addTweetPadre(False).addReplies([]).build()
                self.registroEventos.registrarEvento(user.username +"(super)" , "Posteó un reply", datetime.datetime.now())

            else:
                reply = TweetBuilder().addUsername(user.username).addContent(content).addHora(datetime.datetime.now()).addTweetPadre(False).addReplies([]).build()
                self.registroEventos.registrarEvento(user.username, "Posteó un reply", datetime.datetime.now())

            
            tweet.add_reply(reply)
            print("Respuesta agregada con éxito!\n")
        else:
            print("El índice de tweet no es válido.\n")


def twitter_menu(user, twitter_app):
    while True:
        print("=== Twitter Reloaded ===")
        print("1. Publicar un tweet")
        print("2. Ver tweets")
        print("3. Responder a un tweet")
        print("4. Ver log de eventos")
        print("5. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            content = input("Escribe tu tweet: ")
            twitter_app.post_tweet(user, content)
        elif choice == "2":
            twitter_app.view_tweets()
        elif choice == "3":
            tweet_index = int(input("Ingresa el índice del tweet al que deseas responder: "))
            content = input("Escribe tu respuesta: ")
            twitter_app.reply_to_tweet(user, tweet_index, content)
        elif choice == "4":
            twitter_app.registroEventos.displayEventos()
        elif choice == "5":
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Función principal para ejecutar la aplicación
def main():
    authentication_manager = AuthenticationManager()
    registroEventos = RegistroEventos()
    #Se agregan usuarios dummy para los tweets dummy

    user1 = authentication_manager.register("Patricio", "patricio", "1")
    user2 = authentication_manager.register("Carlos", "carlos", "2")
    user3 =authentication_manager.register("Juan", "juan", "1")
    user4 = authentication_manager.register("Roberto", "roberto", "1")
    user5 = authentication_manager.register("Ernesto", "ernesto", "2")

    #Se crea una instancia de twitter app
    twitter_app = TwitterApp(authentication_manager, registroEventos)

    #Se agregan dummy tweets para el ejemplo
    twitter_app.post_tweet(user1, "Buenos dias grupo")
    twitter_app.post_tweet(user2, "Hoy no me siento muy bien...")
    twitter_app.post_tweet(user3, "Voten por el pan")
    twitter_app.post_tweet(user4, "¿Que opinan de la nueva peli de flash?")
    twitter_app.post_tweet(user5, "Estoy harto de la escuela")
    print("\n\n\n\n\n")

     
     

    while True:
        print("=== Twitter Reloaded ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir\n\n")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            user = authentication_manager.login(username, password)
            if user:
                twitter_menu(user, twitter_app)
                break
        elif choice == "2":
            superUser = input("¿Quieres ser un super usuario? 1 = si, 2 = no:")
            if superUser != "1" and superUser != "2":
                print("Opcion no valida. Por favor, intenta de nuevo")
                
            else:
                username = input("Elige un nombre de usuario: ")
                password = input("Elige una contraseña: ")
                user = authentication_manager.register(username, password, superUser)
                continue

        elif choice == "3":
            return
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")



# Ejecutar la aplicación
if __name__ == "__main__":
    main()