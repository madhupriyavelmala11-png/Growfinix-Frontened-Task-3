import React from "react";

const ProductCard = ({ product }) => {
  const { name, category, brand, price, rating, stock, description } = product;

  // Star rating rendering helper
  const renderStars = (rating) => {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    const stars = [];

    for (let i = 0; i < 5; i++) {
      if (i < fullStars) {
        stars.push(
          <span key={i} className="star filled">
            ★
          </span>,
        );
      } else if (i === fullStars && hasHalfStar) {
        stars.push(
          <span key={i} className="star half">
            ★
          </span>,
        );
      } else {
        stars.push(
          <span key={i} className="star empty">
            ★
          </span>,
        );
      }
    }
    return stars;
  };

  const getStockClass = (stockStatus) => {
    if (stockStatus === "In Stock") return "stock-in";
    if (stockStatus === "Low Stock") return "stock-low";
    return "stock-out";
  };

  return (
    <div className="product-card">
      <div className="product-image-container">
        {product.image ? (
          <img
            src={product.image}
            alt={name}
            className="product-image"
            loading="lazy"
          />
        ) : (
          <div className="product-image-placeholder">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
              className="placeholder-icon"
            >
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
              <circle cx="8.5" cy="8.5" r="1.5"></circle>
              <polyline points="21 15 16 10 5 21"></polyline>
            </svg>
          </div>
        )}
      </div>

      <div className="product-details">
        <div className="product-header">
          <span className="product-category">{category}</span>
          <span className={`product-stock ${getStockClass(stock)}`}>
            {stock}
          </span>
        </div>

        <h3 className="product-title">{name}</h3>
        <p className="product-brand">by {brand}</p>

        <p className="product-description">{description}</p>

        <div className="product-footer">
          <div
            className="product-rating"
            aria-label={`Rating: ${rating} out of 5 stars`}
          >
            {renderStars(rating)}
            <span className="rating-value">{rating.toFixed(1)}</span>
          </div>
          <div className="product-price">₹{price.toFixed(2)}</div>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
