# Furniture Store Web Application 🛋️
🚀 [Click Here to View the Project](https://homora-tawny.vercel.app/)


This project is a furniture store web application built using Flask (Python) and demonstrates web development fundamentals including routing, templating, database integration, frontend styling, and interactive JavaScript features.

---

## 📖 Table of Contents
1. [Features](#features-✨)
2. [Technologies Used](#technologies-used-🛠️)
3. [Project Structure](#project-structure-📂)
4. [Installation](#installation-⚙️)
5. [Usage](#usage-🚀)
6. [Screenshots](#screenshots-🖼️)
7. [Future Improvements](#future-improvements-🔮)
8. [Learning Outcomes](#learning-outcomes-📚)
9. [Contributing](#contributing-🤝)
10. [Acknowledgements](#acknowledgements-🙏)
11. [License](#license-📄)
12. [Author](#author-👩‍💻)

---

## Features ✨
- **Add to Cart**: Items can be added to a shopping cart for later purchase.
- **Responsive Layout**: Built with Bootstrap to support both desktop and mobile screens.
- **Dynamic Content**: Uses Flask templates (`Jinja2`) to render products dynamically from the database.
- **Animations**: Smooth scrolling and reveal animations enhance the user experience.
- **Database Support**: SQLite stores product information such as names, prices, and images.
- **Clean UI**: Organized card-based design for better readability and browsing.

---

## Technologies Used 🛠️
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite
- **JavaScript:** Scroll animations (`scroll-effect.js`)
- **Version Control:** Git & GitHub
- **Tools:** VS Code, GitHub Desktop

---

## Project Structure 📂
```
project/
│── app.py              # Flask application entry point
│── database.db         # SQLite database
│
│── static/             # Static files (CSS, JS, Images)
│   ├── style.css       # Custom styles
│   ├── scroll-effect.js# Scroll animation script
│   ├── kitchen_photos/ # Kitchen images
│   ├── bedroom_photos/ # Bedroom images
│   ├── dressing_photos/# Dressing room images
│   └── Home_photos/    # Homepage images
│
│── templates/          # HTML templates
│   ├── layout.html     # Base template
│   ├── index.html      # Homepage
│   ├── kitchens.html   # Kitchens category
│   ├── bedrooms.html   # Bedrooms category
│   └── ...             # Other pages
│
└── README.md           # Project documentation
```

---

## Installation ⚙️
Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the app**
   ```bash
   flask run
   ```
   Or:
   ```bash
   python app.py
   ```

---

## Usage 🚀
1. Open your browser and go to: `http://127.0.0.1:5000/`.
2. Browse the available categories (Kitchens, Bedrooms, Dressing Rooms, etc.).
3. Add desired items to the shopping cart.
4. Continue browsing or proceed to checkout (future implementation).

---

## Screenshots 🖼️
> <img width="1353" height="642" alt="image" src="https://github.com/user-attachments/assets/3fb1dc06-93a8-4348-839a-e0e24f1f209d" />


- **Homepage**: Overview of categories with featured furniture.
- **Kitchens Page**: Displays available kitchens with prices and images.
- **Bedrooms Page**: Showcases bedroom furniture items.
- **Cart**: A list of items added by the user.

---

## Future Improvements 🔮
- Add **User Authentication** (sign up, login, logout).
- Implement a **checkout system** with payment integration.
- Build an **Admin Dashboard** to manage products.
- Add a **search and filter system** for products.
- Store user carts in the database instead of session.
- Improve the UI with animations and better navigation.

---

## Learning Outcomes 📚
By building this project, I learned:
- How to structure a **Flask application** with routes and templates.
- Using **Jinja2 templating** to pass data from backend to frontend.
- Managing **static files** (CSS, JS, Images) in Flask.
- Designing a database schema and using **SQLite** with Python.
- Building a **responsive layout** using Bootstrap.
- Adding **JavaScript effects** to improve the user experience.
- Using **Git & GitHub** for version control and collaboration.

---

## Contributing 🤝

Contributions are always welcome! If you’d like to improve this project, follow these steps:

1. **Fork the repository**
   Click the "Fork" button at the top right of this page to create your own copy of the repository.

2. **Clone your forked repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

3. **Create a new branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make your changes**
   Add your code, fix bugs, or enhance documentation.

5. **Commit your changes**
   ```bash
   git commit -m "Add new feature: YourFeatureName"
   ```

6. **Push to your branch**
   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Open a Pull Request**
   Go to the original repository and click on **New Pull Request** to submit your changes.

---

### Contribution Guidelines 📌
- Write clean, readable, and well-documented code.
- Make sure your code is tested before submitting.
- Keep commits descriptive and meaningful.
- Respect the coding style used in this project.
- If you’re fixing a bug, link the related issue in your PR.

---

## Acknowledgements 🙏
Special thanks to:
- The **Flask** community for great documentation and tutorials.
- **Bootstrap** for making responsive design easy.
- Everyone who contributes to open-source projects ❤️.

---

## License 📄
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.

---

## Author 👩‍💻
Developed with ❤️ by **Shaimaa** ✨
