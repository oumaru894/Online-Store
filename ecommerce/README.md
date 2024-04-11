 Tittle:
        Bah watch

    Video Dema:
                https://youtu.be/Eb9VYPgnZ0Q

    Description:
                Project Overview:
This project is a B2C (Business-to-Consumer) e-commerce web application that specializes in selling watches and jewelry. It is developed using the Flask web framework, SQL (Structured Query Language) for database operations, and JavaScript for interactive features. The primary purpose of this app is to enable users to purchase watches and jewelry online.

Key Features and Functionality:

User Authentication: The application includes a user authentication system. Users can create an account if they don't have one or log in if they are returning customers. This authentication system ensures that only authenticated users can place orders.

Product Catalog: The store's catalog consists of watches and bracelets. Users can browse through the available products, view product details, and add items to their shopping cart.

Shopping Cart: Users can add products to their shopping cart, view the contents of the cart, update the quantity of items, and remove items from the cart. Even if a user is not logged in, they can still interact with the cart functionality, making it user-friendly.

Order Placement: To place an order, users must log in. Once logged in, they can proceed to the checkout process, where they confirm their order and choose a payment method.

Payment Gateway: The application supports payments through Orange Money, a payment method provided by a GSM company. This choice of payment gateway is due to regional limitations that prevent the use of other payment gateways like PayPal or Google Pay.

Backend Database: The backend of the application uses SQLite as the database system. SQLite is a lightweight, file-based database system, and it's utilized for storing and managing data related to users, products, orders, and more.

SQLAlchemy: SQLAlchemy is used for database interactions within the application. It simplifies the process of querying and interacting with the SQLite database.

Frontend and JavaScript: JavaScript is used on the frontend to provide interactive features and enhance user experience. For example, it may be used for dynamically updating the cart without requiring a page refresh.

Pagination: The application likely includes pagination to efficiently display a large number of products, making it easier for users to navigate the product catalog.

Security: The application follows security best practices, including password hashing and validation to protect user accounts. It also likely implements CSRF protection and session management for secure user interactions.

Responsive Design: The user interface of the application is designed to be responsive, ensuring that it works well on various devices, including desktops, tablets, and mobile phones.

Orders and Invoices: After placing an order, users receive an invoice that includes details about the items purchased, the total cost, and other relevant information.

Overall, this e-commerce application provides users in the specified region with the ability to browse, select, and purchase watches and jewelry. It offers a secure and user-friendly shopping experience while accommodating regional payment constraints through the use of Orange Money. Additionally, the application takes advantage of Flask, SQL, and JavaScript to provide a dynamic and feature-rich online store for customers.




    TODO:
        1,when load home, click the on the store in the navigation bar
        2,click on an item of your choice and view it as a single item
            a, add to cart
            b, choice quantity to add to cart
        3, after adding all your items to cart, click on the cart icon in the navigation bar to view them.
        4, click on order to order them
        5, the payment is done through orange money, which is the local transaction gateway in community
        6, take note of the account name and number to send the amount.
