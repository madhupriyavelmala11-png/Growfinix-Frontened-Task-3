import React from "react";

const FilterControls = ({
  categories,
  selectedCategory,
  onCategoryChange,
  sortOption,
  onSortChange,
}) => {
  return (
    <div className="filter-controls">
      <div className="filter-group">
        <label htmlFor="category-select" className="filter-label">
          Category:
        </label>
        <select
          id="category-select"
          value={selectedCategory}
          onChange={(e) => onCategoryChange(e.target.value)}
          className="filter-select"
        >
          <option value="All Categories">All Categories</option>
          {categories.map((category, index) => (
            <option key={index} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>

      <div className="filter-group">
        <label htmlFor="sort-select" className="filter-label">
          Sort By:
        </label>
        <select
          id="sort-select"
          value={sortOption}
          onChange={(e) => onSortChange(e.target.value)}
          className="filter-select"
        >
          <option value="default">Default</option>
          <option value="name-asc">Name: A–Z</option>
          <option value="name-desc">Name: Z–A</option>
          <option value="price-asc">Price: Low to High</option>
          <option value="price-desc">Price: High to Low</option>
          <option value="rating-desc">Rating: High to Low</option>
        </select>
      </div>
    </div>
  );
};

export default FilterControls;
