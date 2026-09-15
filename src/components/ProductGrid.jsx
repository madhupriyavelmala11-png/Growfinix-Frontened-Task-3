import React from "react";
import ProductCard from "./ProductCard";

const ProductGrid = ({ products, onClearFilters }) => {
  if (!products || products.length === 0) {
    return (
      <div className="empty-state">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="empty-icon"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <h3>No products found</h3>
        <p>
          We couldn't find anything matching your search and filter criteria.
        </p>
        <button className="clear-filters-btn" onClick={onClearFilters}>
          Clear Filters
        </button>
      </div>
    );
  }

  return (
    <div className="product-grid">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductGrid;
