# entrega-2-twitter
Entrega 2 de Carlos García Geronis A01748393 y Patricio Mondragon Fernandez A01748352 

Design Pattern: Builder
The Builder pattern is used to build complex objects step by step. In the provided code, the Builder pattern is implemented in the TweetBuilder and UserBuilder classes.

Design Pattern: Factory Method
The Factory Method pattern is used to encapsulate the creation of objects in a separate class, allowing subclasses to decide which particular class to instantiate. In the code provided, the Factory Method pattern is implemented in the UserFactory class.

Design Pattern: Singleton
The Singleton pattern is used to ensure that a class has a single instance and provide a global access point to this instance. In the code provided, the Singleton pattern is implemented in the AuthenticationManager class.

SOLID practices
Single Responsibility Principle (SRP): Each class in the code has a single responsibility. For example, the EventRegistration class is responsible for managing and displaying registered events, the AuthenticationManager class is responsible for managing user authentication, the TwitterApp class is responsible for managing the publication and display of tweets, etc.

Open/Closed Principle (OCP): The code can be extended to add new functionality without modifying the existing code. For example, a new user class or new functionality can be added to the tweeting system without modifying existing classes.

Dependency Inversion Principle (DIP): Classes depend on abstractions instead of depending on concrete implementations. For example, the TwitterApp class depends on the AuthenticationManager interface instead of depending on a concrete implementation.


FOR MORE INFORMATION, YOU CAN CHECK THE PDF ...
