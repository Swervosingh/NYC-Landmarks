import React from 'react';
import './Map.css'; // Make sure to import the CSS file

function MapPage() {
  return (
    <div className="MapPage">
      
      <div className="button-container">
        <a href="https://www.google.com/maps/@40.6865662,-73.8392843,16z?entry=ttu" className="button">Click Me</a>
      </div>
    </div>
  );
}

export default MapPage;
