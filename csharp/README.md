## ASP.NET MVC
MVC is a design pattern used to decouple user-interface (view), data (model), and application logic (controller). 
This pattern helps to achieve separation of concerns.

Using the MVC pattern for websites, requests are routed to a Controller that is responsible for working with the 
Model to perform actions and/or retrieve data. The Controller chooses the View to display and provides it with 
the Model. The View renders the final page, based on the data in the Model.

Controller is the entry point where user interacts. Controller decides which model to call and what data to pass to
which view and show it to the user.

ASP.NET MVC is server-based framework and pages are rendered on server. 

## ASP.NET Razor
It is the template engine to render views. Razor is used to dynamically generate web content on the server.
You can cleanly mix server code with client side content and code.
Razor is server-based framework and pages are rendered on server. 


## Blazor
Blazor apps are composed of Razor components: segments of reusable, web UI implemented using C#, HTML, and CSS. 
Both client and server code are written in C#, allowing shared code and libraries. 
Razor components can be rendered or prerendered from views and pages.
Reusable UI components such as Kendo UI available for Blazor.
Blazor can run on server side (Blazor server) or client side (Blazor WebAssembly).
For server side, communication between client and server is done through SignalR. Every interaction involves network hop. 
If network fails, app stops working.
For client side, Blazor app and .Net dependencies are downloaded to client. If client wants to interact with backend, it can use webAPI or SignalR. 
Download size is larger, app takes longer to load.

## Entity Framework Core
EF Core is a data access technology. It serves as an ORM. Work with DB using .NET objects.
Data access is performed using a model. A model contains an entity class and context object that represents session with DB. Context object allows querying and saving data.
EF Migrations are used to create DB and update DB schema.
Can retrieve data using LINQ (Language Integrated Query). 

## Dependency Injection (IoC)
DI is a software design pattern, which is a technique for achieving Inversion of Control (IoC) between classes and their dependencies.
Instead of making objects like Employee emp = new Employee(); where concrete classes are used for object making. We use Interfaces.
IEmployee _emp; this _emp is passed to a constructor where Framework is responsible for creating instance and disposing it.
Register dependencies in a service container (IServiceProvider). Services are typically registered in the app's Program.cs file.
With a scoped service we get the same instance within the scope of a given http request but a new instance across different http requests.
With a transient service, a new instance is provided every time an instance is requested whether it is in the scope of same http request or across different http requests.
With Singleton service, there is only a single instance. An instance is created, when service is first requested and that single instance single instance will be used by all subsequent http request throughout the application.
