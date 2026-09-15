# Dynamic Product Display Grid

A responsive web application that displays product information dynamically using JSON data. The project includes search, category filtering, and sorting features to make it easy for users to find and organize products.

## About the Project

This project was developed as part of **Task 3: Dynamic Data Display Grid**.

The main goal of the project is to demonstrate how JSON data can be loaded and displayed dynamically in a responsive grid. Instead of creating each product card manually, the application generates the cards from the available data.

Users can search for products, filter them by category, and sort them based on different criteria.

## Features

- Dynamic product cards generated from JSON data
- Search products by name, brand, or category
- Filter products by category
- Sort products by:
  - Name (A-Z)
  - Name (Z-A)
  - Price (Low to High)
  - Price (High to Low)
  - Rating (High to Low)
- Displays the number of products currently shown
- Clear filters option
- Empty state when no products are found
- Responsive design for desktop, tablet, and mobile
- Clean and user-friendly interface
- Reusable React components

## Technologies Used

- React
- JavaScript
- HTML
- CSS
- Vite
- JSON

## Project Structure

```text
dynamic-product-grid/
│
├── public/
│
├── src/
│   ├── components/
│   ├── data/
│   │   └── products.json
│   ├── App.jsx
│   ├── App.css
│   └── main.jsx
│
├── index.html
├── package.json
├── package-lock.json
├── vite.config.js
└── README.md
