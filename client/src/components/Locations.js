import React, { useState, useEffect } from 'react';
import videoBg from '../assets/locationvid.mov';
import './Location.css';

function Locations() {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/landmarks')
      .then(response => response.json())
      .then(data => {
        console.log(data)
        setLocations(data)})
  }, []);

  const handleDeleteLocation = id => {
    console.log("Locations before deletion:", locations);
    fetch(`/landmarks/${id}`, {
      method: 'DELETE',
    })
      .then(() => {
        setLocations(locations.filter(location => location.id !== id));
        console.log("Locations after deletion:", locations);
      });
  };
  
  return (
    <div className="fullscreen-bg">
      <video autoPlay muted loop className="fullscreen-bg__video">
        <source src={videoBg} type="video/mp4" />
      </video>
      <div className="location-container">
        <h2>Landmarks</h2>
        {locations.map(location => (
          <div key={location.id} className="location-item">
            <h3>{location.name}</h3>
            <p>{location.description}</p>
            <img src={location.image_url} alt={location.name} />
            <button onClick={() => handleDeleteLocation(location.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Locations;
