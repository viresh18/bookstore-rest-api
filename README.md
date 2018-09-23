<p align="center">
 <h1>RESTful API for an Online Bookstore </h1>
 <p>


# Table of contents
1. [Problem Statement](#problem)
2. [Accessible Link](#accessible)
3. [Routes Table](#route)

## Problem <a name="problem"></a>
### Design a RESTful API for an online bookstore which can be used to manage different products.

* Details: Implementation of a RESTful API for an online store. It would support addition, deletion, editing and searching a book. It will also support authentication (only authenticated users can add / view / edit / delete items). This API is created speculatively for a web developer who will use it to create a website. There are some example scenarios included along with the expected request / response objects.

## Accessible Link <a name="accessible"></a>
* Running Git Repository of the app: [https://github.com/viresh18/bookstore-rest-api)

## Routes Table <a name="route"></a>
HTTP Verb | Path | Action | Used for
--- | --- | --- | ---
`GET` | `/api/profile` | `list` | `UserProfileViewSet`
`POST` | `/api/profile` | `create` | `UserProfileViewSet`
`POST` | `/api/login` | `login` | `LoginViewSet`
`GET` | `/api/books` | `list` | `BooksViewSet`
`POST` | `/api/books` | `create` | `BooksViewSet`
`PUT` | `/api/books/:id` | `update` | `BooksViewSet`
`DELETE` | `/api/books/:id` | `destroy` | `BooksViewSet`
