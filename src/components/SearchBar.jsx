import React from "react";

const SearchBar = ({ searchTerm, onSearchChange }) => {
  return (
    <div className="search-bar">
      <div className="search-input-wrapper">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="search-icon"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fillRule="evenodd"
            d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
            clipRule="evenodd"
          />
        </svg>
        <input
          type="text"
          placeholder="Search products by name, brand, or category..."
          value={searchTerm}
          onChange={(e) => onSearchChange(e.target.value)}
          className="search-input"
          aria-label="Search products"
        />
        {searchTerm && (
          <button
            className="clear-search-btn"
            onClick={() => onSearchChange("")}
            aria-label="Clear search"
          >
            &times;
          </button>
        )}
      </div>
    </div>
  );
};

export default SearchBar;
