import React, { useState, useEffect, useMemo } from "react";
import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import FilterControls from "./components/FilterControls";
import ProductGrid from "./components/ProductGrid";
import productsData from "./data/products.json";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All Categories");
  const [sortOption, setSortOption] = useState("default");
  const [isLoading, setIsLoading] = useState(true);

  // Extract unique categories for the filter dropdown
  const categories = useMemo(() => {
    const allCategories = productsData.map((p) => p.category);
    return [...new Set(allCategories)].sort();
  }, []);

  // Simulate loading data
  useEffect(() => {
    const timer = setTimeout(() => {
      setProducts(productsData);
      setIsLoading(false);
    }, 600);
    return () => clearTimeout(timer);
  }, []);

  // Apply search, filter, and sorting
  const filteredAndSortedProducts = useMemo(() => {
    let result = [...products];

    // 1. Search Filter
    if (searchTerm.trim() !== "") {
      const lowercasedTerm = searchTerm.toLowerCase();
      result = result.filter(
        (product) =>
          product.name.toLowerCase().includes(lowercasedTerm) ||
          product.brand.toLowerCase().includes(lowercasedTerm) ||
          product.category.toLowerCase().includes(lowercasedTerm),
      );
    }

    // 2. Category Filter
    if (selectedCategory !== "All Categories") {
      result = result.filter(
        (product) => product.category === selectedCategory,
      );
    }

    // 3. Sorting
    result.sort((a, b) => {
      switch (sortOption) {
        case "name-asc":
          return a.name.localeCompare(b.name);
        case "name-desc":
          return b.name.localeCompare(a.name);
        case "price-asc":
          return a.price - b.price;
        case "price-desc":
          return b.price - a.price;
        case "rating-desc":
          return b.rating - a.rating;
        default:
          // Keep original order (by ID)
          return a.id - b.id;
      }
    });

    return result;
  }, [products, searchTerm, selectedCategory, sortOption]);

  const handleClearFilters = () => {
    setSearchTerm("");
    setSelectedCategory("All Categories");
    setSortOption("default");
  };

  return (
    <div className="app-container">
      <Header />

      <main className="main-content">
        <div className="controls-section">
          <SearchBar searchTerm={searchTerm} onSearchChange={setSearchTerm} />
          <FilterControls
            categories={categories}
            selectedCategory={selectedCategory}
            onCategoryChange={setSelectedCategory}
            sortOption={sortOption}
            onSortChange={setSortOption}
          />
        </div>

        <div className="results-info">
          {!isLoading && (
            <p className="product-count">
              Showing {filteredAndSortedProducts.length} of {products.length}{" "}
              products
            </p>
          )}
        </div>

        {isLoading ? (
          <div className="loading-state">
            <div className="spinner"></div>
            <p>Loading products...</p>
          </div>
        ) : (
          <ProductGrid
            products={filteredAndSortedProducts}
            onClearFilters={handleClearFilters}
          />
        )}
      </main>
    </div>
  );
}

export default App;
