import React from 'react';
import videoBg from '../assets/nycvideo.mp4';
import './Home.css';

function Home() {
  return (
    <div className="fullscreen-bg">
      <video autoPlay muted loop className="fullscreen-bg__video">
        <source src={videoBg} type="video/mp4" />
        
      </video>
      <div className="content">
        <h2>Welcome to the NYC Landmarks Website!</h2>
        <h3>Explore famous landmarks to visit in New York City.</h3>
      </div>
    </div>
  );
}

export default Home;
