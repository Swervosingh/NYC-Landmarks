import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <div className="navbar-container">
      <nav>
        <ul>
          <li><Link to="/" className="button">↪ Home</Link></li>
          <li><Link to="/locations" className="button">Landmarks</Link></li>
          <li><Link to="/pictures" className="button">Form ↩</Link></li>
          
          <li><Link to="/map" className="button">Map</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;

